BEGIN;

CREATE SCHEMA IF NOT EXISTS hodom;

CREATE TYPE hodom.period_status AS ENUM (
  'open',
  'imported',
  'validated',
  'closed'
);

CREATE TYPE hodom.import_severity AS ENUM (
  'info',
  'warning',
  'error'
);

CREATE TABLE IF NOT EXISTS hodom.service_unit (
  id BIGSERIAL PRIMARY KEY,
  code TEXT NOT NULL UNIQUE,
  name TEXT NOT NULL,
  facility_name TEXT,
  default_bed_capacity INTEGER NOT NULL CHECK (default_bed_capacity >= 0),
  active BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS hodom.reporting_period (
  id BIGSERIAL PRIMARY KEY,
  service_unit_id BIGINT NOT NULL REFERENCES hodom.service_unit(id),
  year INTEGER NOT NULL CHECK (year BETWEEN 2000 AND 2100),
  month INTEGER NOT NULL CHECK (month BETWEEN 1 AND 12),
  status hodom.period_status NOT NULL DEFAULT 'open',
  source_label TEXT,
  imported_at TIMESTAMPTZ,
  validated_at TIMESTAMPTZ,
  closed_at TIMESTAMPTZ,
  notes TEXT,
  UNIQUE (service_unit_id, year, month)
);

CREATE TABLE IF NOT EXISTS hodom.bed_capacity_period (
  id BIGSERIAL PRIMARY KEY,
  service_unit_id BIGINT NOT NULL REFERENCES hodom.service_unit(id),
  starts_on DATE NOT NULL,
  ends_on DATE,
  bed_capacity INTEGER NOT NULL CHECK (bed_capacity >= 0),
  reason TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  CHECK (ends_on IS NULL OR ends_on >= starts_on)
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_hodom_bed_capacity_period_open
  ON hodom.bed_capacity_period(service_unit_id, starts_on)
  WHERE ends_on IS NULL;

CREATE TABLE IF NOT EXISTS hodom.daily_report (
  id BIGSERIAL PRIMARY KEY,
  service_unit_id BIGINT NOT NULL REFERENCES hodom.service_unit(id),
  reporting_period_id BIGINT REFERENCES hodom.reporting_period(id),
  report_date DATE NOT NULL,
  opening_census INTEGER NOT NULL CHECK (opening_census >= 0),
  admissions_total_reported INTEGER CHECK (admissions_total_reported IS NULL OR admissions_total_reported >= 0),
  discharges_total_reported INTEGER CHECK (discharges_total_reported IS NULL OR discharges_total_reported >= 0),
  same_day_inout_total INTEGER CHECK (same_day_inout_total IS NULL OR same_day_inout_total >= 0),
  beds_available_reported INTEGER CHECK (beds_available_reported IS NULL OR beds_available_reported >= 0),
  patient_stay_days_total INTEGER CHECK (patient_stay_days_total IS NULL OR patient_stay_days_total >= 0),
  patient_stay_days_beneficiary INTEGER CHECK (patient_stay_days_beneficiary IS NULL OR patient_stay_days_beneficiary >= 0),
  notes TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  UNIQUE (service_unit_id, report_date)
);

CREATE INDEX IF NOT EXISTS idx_hodom_daily_report_period
  ON hodom.daily_report(reporting_period_id, report_date);

CREATE TABLE IF NOT EXISTS hodom.admission_category (
  code TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  sort_order INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS hodom.discharge_category (
  code TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  sort_order INTEGER NOT NULL
);

INSERT INTO hodom.admission_category (code, name, sort_order)
VALUES
  ('urgency', 'Urgencia', 10),
  ('hospitalization', 'Hospitalizacion', 20),
  ('ambulatory', 'Ambulatorio', 30),
  ('urgency_law', 'Ley de Urgencia', 40),
  ('ugcc', 'UGCC', 50),
  ('transfer_in', 'Traslado de ingreso', 60)
ON CONFLICT (code) DO NOTHING;

INSERT INTO hodom.discharge_category (code, name, sort_order)
VALUES
  ('home_or_other_hospital', 'Alta al hogar / otro hospital', 10),
  ('transfer_out', 'Traslado a otro servicio', 20),
  ('deceased', 'Fallecidos', 30)
ON CONFLICT (code) DO NOTHING;

CREATE TABLE IF NOT EXISTS hodom.daily_admission_count (
  daily_report_id BIGINT NOT NULL REFERENCES hodom.daily_report(id) ON DELETE CASCADE,
  category_code TEXT NOT NULL REFERENCES hodom.admission_category(code),
  count INTEGER NOT NULL CHECK (count >= 0),
  PRIMARY KEY (daily_report_id, category_code)
);

CREATE TABLE IF NOT EXISTS hodom.daily_discharge_count (
  daily_report_id BIGINT NOT NULL REFERENCES hodom.daily_report(id) ON DELETE CASCADE,
  category_code TEXT NOT NULL REFERENCES hodom.discharge_category(code),
  count INTEGER NOT NULL CHECK (count >= 0),
  PRIMARY KEY (daily_report_id, category_code)
);

CREATE TABLE IF NOT EXISTS hodom.import_batch (
  id BIGSERIAL PRIMARY KEY,
  source_name TEXT NOT NULL,
  source_path TEXT,
  imported_by TEXT,
  imported_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  notes TEXT
);

CREATE TABLE IF NOT EXISTS hodom.import_issue (
  id BIGSERIAL PRIMARY KEY,
  import_batch_id BIGINT REFERENCES hodom.import_batch(id) ON DELETE CASCADE,
  service_unit_id BIGINT REFERENCES hodom.service_unit(id),
  reporting_period_id BIGINT REFERENCES hodom.reporting_period(id),
  report_date DATE,
  severity hodom.import_severity NOT NULL,
  issue_code TEXT NOT NULL,
  message TEXT NOT NULL,
  payload JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_hodom_import_issue_scope
  ON hodom.import_issue(import_batch_id, reporting_period_id, report_date);

CREATE OR REPLACE VIEW hodom.v_daily_report_resolved AS
WITH admission_breakdown AS (
  SELECT
    dr.id AS daily_report_id,
    COALESCE(SUM(dac.count), 0) AS admission_breakdown_total,
    COUNT(dac.category_code) AS admission_breakdown_rows
  FROM hodom.daily_report dr
  LEFT JOIN hodom.daily_admission_count dac ON dac.daily_report_id = dr.id
  GROUP BY dr.id
),
discharge_breakdown AS (
  SELECT
    dr.id AS daily_report_id,
    COALESCE(SUM(ddc.count), 0) AS discharge_breakdown_total,
    COUNT(ddc.category_code) AS discharge_breakdown_rows
  FROM hodom.daily_report dr
  LEFT JOIN hodom.daily_discharge_count ddc ON ddc.daily_report_id = dr.id
  GROUP BY dr.id
)
SELECT
  dr.id,
  dr.service_unit_id,
  dr.reporting_period_id,
  dr.report_date,
  dr.opening_census,
  CASE
    WHEN ab.admission_breakdown_rows > 0 THEN ab.admission_breakdown_total
    ELSE dr.admissions_total_reported
  END AS admissions_total_resolved,
  CASE
    WHEN db.discharge_breakdown_rows > 0 THEN db.discharge_breakdown_total
    ELSE dr.discharges_total_reported
  END AS discharges_total_resolved,
  dr.same_day_inout_total,
  COALESCE(
    dr.beds_available_reported,
    (
      SELECT bcp.bed_capacity
      FROM hodom.bed_capacity_period bcp
      WHERE bcp.service_unit_id = dr.service_unit_id
        AND bcp.starts_on <= dr.report_date
        AND (bcp.ends_on IS NULL OR bcp.ends_on >= dr.report_date)
      ORDER BY bcp.starts_on DESC
      LIMIT 1
    ),
    su.default_bed_capacity
  ) AS beds_available_resolved,
  CASE
    WHEN
      dr.opening_census IS NOT NULL
      AND (
        CASE
          WHEN ab.admission_breakdown_rows > 0 THEN ab.admission_breakdown_total
          ELSE dr.admissions_total_reported
        END
      ) IS NOT NULL
      AND (
        CASE
          WHEN db.discharge_breakdown_rows > 0 THEN db.discharge_breakdown_total
          ELSE dr.discharges_total_reported
        END
      ) IS NOT NULL
    THEN
      dr.opening_census
      + (
        CASE
          WHEN ab.admission_breakdown_rows > 0 THEN ab.admission_breakdown_total
          ELSE dr.admissions_total_reported
        END
      )
      - (
        CASE
          WHEN db.discharge_breakdown_rows > 0 THEN db.discharge_breakdown_total
          ELSE dr.discharges_total_reported
        END
      )
    ELSE NULL
  END AS closing_census_resolved,
  dr.patient_stay_days_total,
  dr.patient_stay_days_beneficiary,
  CASE
    WHEN ab.admission_breakdown_rows > 0 THEN 'breakdown'
    WHEN dr.admissions_total_reported IS NOT NULL THEN 'reported_total'
    ELSE 'missing'
  END AS admissions_source_mode,
  CASE
    WHEN db.discharge_breakdown_rows > 0 THEN 'breakdown'
    WHEN dr.discharges_total_reported IS NOT NULL THEN 'reported_total'
    ELSE 'missing'
  END AS discharges_source_mode,
  dr.notes
FROM hodom.daily_report dr
JOIN hodom.service_unit su ON su.id = dr.service_unit_id
JOIN admission_breakdown ab ON ab.daily_report_id = dr.id
JOIN discharge_breakdown db ON db.daily_report_id = dr.id;

CREATE OR REPLACE VIEW hodom.v_monthly_summary AS
WITH daily AS (
  SELECT *
  FROM hodom.v_daily_report_resolved
),
aggregated AS (
  SELECT
    rp.id AS reporting_period_id,
    rp.service_unit_id,
    rp.year,
    rp.month,
    MIN(d.report_date) AS first_report_date,
    MAX(d.report_date) AS last_report_date,
    COUNT(*) AS day_count,
    SUM(COALESCE(d.admissions_total_resolved, 0)) AS admissions_total,
    SUM(COALESCE(d.discharges_total_resolved, 0)) AS discharges_total,
    SUM(COALESCE(d.patient_stay_days_total, 0)) AS patient_stay_days_total,
    SUM(COALESCE(d.patient_stay_days_beneficiary, 0)) AS patient_stay_days_beneficiary,
    SUM(COALESCE(d.beds_available_resolved, 0)) AS beds_available_total,
    SUM(COALESCE(d.closing_census_resolved, 0)) AS closing_census_accumulated
  FROM hodom.reporting_period rp
  JOIN daily d ON d.reporting_period_id = rp.id
  GROUP BY rp.id, rp.service_unit_id, rp.year, rp.month
)
SELECT
  a.reporting_period_id,
  a.service_unit_id,
  a.year,
  a.month,
  a.first_report_date,
  a.last_report_date,
  a.day_count,
  a.admissions_total,
  a.discharges_total,
  a.patient_stay_days_total,
  a.patient_stay_days_beneficiary,
  a.beds_available_total,
  a.closing_census_accumulated,
  (
    SELECT d.closing_census_resolved
    FROM daily d
    WHERE d.reporting_period_id = a.reporting_period_id
    ORDER BY d.report_date DESC
    LIMIT 1
  ) AS final_closing_census,
  (
    SELECT d.opening_census
    FROM daily d
    WHERE d.reporting_period_id = a.reporting_period_id
    ORDER BY d.report_date ASC
    LIMIT 1
  ) AS opening_census_first_day,
  CASE
    WHEN a.beds_available_total > 0
    THEN a.closing_census_accumulated::NUMERIC / a.beds_available_total
    ELSE NULL
  END AS occupancy_index,
  CASE
    WHEN a.discharges_total > 0
    THEN a.patient_stay_days_total::NUMERIC / a.discharges_total
    ELSE NULL
  END AS average_stay_days
FROM aggregated a;

COMMIT;
