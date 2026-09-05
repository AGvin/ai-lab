#!/usr/bin/env bash
set -uo pipefail
output_file="$RUNNER_TEMP/documentation-validate-output.txt"
set +e
python -m tools.documentation.metadata_tooling.cli validate \
  --validate-schemas "$VALIDATE_SCHEMAS" \
  --validate-relations "$VALIDATE_RELATIONS" \
  --validate-cache "$VALIDATE_CACHE" \
  2>&1 | tee "$output_file"
cli_status=${PIPESTATUS[0]}
set -e

schemas_status="$(sed -nE 's/^schemas: (passed|failed|skipped)$/\1/p' "$output_file" | tail -n 1)"
relations_status="$(sed -nE 's/^relations: (passed|failed|skipped)$/\1/p' "$output_file" | tail -n 1)"
cache_status="$(sed -nE 's/^cache: (passed|failed|skipped)$/\1/p' "$output_file" | tail -n 1)"
echo "schemas=${schemas_status}" >> "$GITHUB_OUTPUT"
echo "relations=${relations_status}" >> "$GITHUB_OUTPUT"
echo "cache=${cache_status}" >> "$GITHUB_OUTPUT"

{
  echo "relation_statistics<<RELATION_STATISTICS"
  grep -E '^[a-z0-9-]+ / [a-z0-9-]+ — [0-9]+ / [0-9]+$' "$output_file" || true
  echo "RELATION_STATISTICS"
} >> "$GITHUB_OUTPUT"

exit "$cli_status"
