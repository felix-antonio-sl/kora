#!/usr/bin/env bash
# SubagentStop hook — vuelca el transcript de la sesion a .claude/trace/
# Disenado para canarios auditables: captura los tool calls de subagents
# antes de que la UI los colapse y se pierdan.
#
# Payload esperado (stdin JSON):
#   { session_id, transcript_path, hook_event_name, agent_type }
#
# Salida en $CLAUDE_PROJECT_DIR/.claude/trace/
#   ${TS}_${AGENT}_${SESSION}.main.jsonl        transcript del main
#   ${TS}_${AGENT}_${SESSION}.subagent-N.jsonl  transcripts de subagents (los
#                                                que contienen los tool calls
#                                                internos del subagente)
#   ${TS}_${AGENT}_${SESSION}.meta.json         metadata del evento
#
# Exit siempre 0 para no bloquear al runtime.

set -uo pipefail

if ! command -v jq >/dev/null 2>&1; then
  exit 0
fi

INPUT="$(cat)"
if [[ -z "$INPUT" ]]; then
  exit 0
fi

SESSION="$(jq -r '.session_id // "unknown"' <<<"$INPUT" 2>/dev/null || echo unknown)"
AGENT="$(jq -r '.agent_type // "unknown"' <<<"$INPUT" 2>/dev/null || echo unknown)"
TRANSCRIPT="$(jq -r '.transcript_path // ""' <<<"$INPUT" 2>/dev/null || echo "")"
EVENT="$(jq -r '.hook_event_name // "SubagentStop"' <<<"$INPUT" 2>/dev/null || echo SubagentStop)"

DUMP_DIR="${CLAUDE_PROJECT_DIR:-$PWD}/.claude/trace"
mkdir -p "$DUMP_DIR" || exit 0

TS="$(date -u +%Y%m%dT%H%M%SZ)"
SAFE_AGENT="${AGENT//[^A-Za-z0-9_.-]/_}"
SAFE_SESSION="${SESSION//[^A-Za-z0-9_.-]/_}"
BASE="${TS}_${SAFE_AGENT}_${SAFE_SESSION}"

if [[ -f "$TRANSCRIPT" ]]; then
  cp "$TRANSCRIPT" "${DUMP_DIR}/${BASE}.main.jsonl" 2>/dev/null || true

  # El transcript del subagent vive en <session-dir>/subagents/agent-*.jsonl
  # El main jsonl es <session-dir>.jsonl; la carpeta hermana lleva el mismo id sin .jsonl.
  SESSION_DIR="${TRANSCRIPT%.jsonl}"
  if [[ -d "${SESSION_DIR}/subagents" ]]; then
    IDX=0
    for SUB in "${SESSION_DIR}/subagents"/agent-*.jsonl; do
      [[ -f "$SUB" ]] || continue
      cp "$SUB" "${DUMP_DIR}/${BASE}.subagent-${IDX}.jsonl" 2>/dev/null || true
      IDX=$((IDX + 1))
    done
  fi
fi

jq -n \
  --arg session "$SESSION" \
  --arg agent "$AGENT" \
  --arg event "$EVENT" \
  --arg transcript "$TRANSCRIPT" \
  --arg captured "$TS" \
  '{session_id:$session, agent_type:$agent, event:$event, transcript_source:$transcript, captured_at:$captured}' \
  > "${DUMP_DIR}/${BASE}.meta.json" 2>/dev/null || true

exit 0
