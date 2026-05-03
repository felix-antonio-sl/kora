# Mapeo de tipos logicos a fisicos

| Logico | PostgreSQL | SQL Server | MySQL |
|--------|------------|------------|-------|
| `string(N)` | `VARCHAR(N)` | `NVARCHAR(N)` | `VARCHAR(N)` |
| `text` | `TEXT` | `NVARCHAR(MAX)` | `TEXT` |
| `integer` | `INTEGER` | `INT` | `INT` |
| `bigint` | `BIGINT` | `BIGINT` | `BIGINT` |
| `decimal(P,S)` | `NUMERIC(P,S)` | `DECIMAL(P,S)` | `DECIMAL(P,S)` |
| `float` | `DOUBLE PRECISION` | `FLOAT` | `DOUBLE` |
| `boolean` | `BOOLEAN` | `BIT` | `TINYINT(1)` |
| `date` | `DATE` | `DATE` | `DATE` |
| `timestamp` | `TIMESTAMP` | `DATETIME2` | `DATETIME` |
| `timestamptz` | `TIMESTAMPTZ` | `DATETIMEOFFSET` | (emular UTC + offset) |
| `uuid` | `UUID` | `UNIQUEIDENTIFIER` | `CHAR(36)` o `BINARY(16)` |
| `json` | `JSONB` (preferido) | `NVARCHAR(MAX) + CHECK ISJSON` | `JSON` |
| `enum(A,B,C)` | `TEXT + CHECK IN` o `CREATE TYPE` | `CHECK IN` | `ENUM(...)` |
| `bytea` | `BYTEA` | `VARBINARY(MAX)` | `BLOB` |
| `array<T>` | `T[]` nativo | tabla asociativa | tabla asociativa |

## Consideraciones por motor

### PostgreSQL 16+

- Preferir `JSONB` sobre `JSON` (binario, indexable).
- `TIMESTAMPTZ` por default para timestamps; almacena UTC y convierte segun session timezone.
- `UUID` como PK solo si existe razon (distributed system, privacy); sino `BIGINT IDENTITY`.
- `CITEXT` util para emails case-insensitive.
- Arrays nativos validos para listas cerradas (< 10 elementos).

### SQL Server 2022

- `NVARCHAR` por default para soporte Unicode.
- `DATETIME2(3)` preferido sobre `DATETIME`.
- `UNIQUEIDENTIFIER` genera con `NEWSEQUENTIALID()` para evitar fragmentacion de indice.
- `DATETIMEOFFSET` para timestamps con timezone explicito.

### MySQL 8+

- `utf8mb4` como charset default; evitar `utf8` legacy.
- `JSON` nativo con path expressions `JSON_EXTRACT()`.
- `ENUM` sigue valido pero considerar lookup table para extensibilidad.
- `TINYINT(1)` convencion para boolean.
