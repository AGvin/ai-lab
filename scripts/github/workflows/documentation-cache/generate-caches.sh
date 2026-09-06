#!/usr/bin/env bash
set -uo pipefail
output_file="$RUNNER_TEMP/documentation-cache-output.txt"
set +e
if [[ "$USE_FINGERPRINTS" == "true" ]]; then
  python -m tools.documentation.metadata_tooling.cli cache --use-fingerprints 2>&1 | tee "$output_file"
  cli_status=${PIPESTATUS[0]}
else
  python -m tools.documentation.metadata_tooling.cli cache --no-use-fingerprints 2>&1 | tee "$output_file"
  cli_status=${PIPESTATUS[0]}
fi
set -e

if (( cli_status == 0 )); then
  echo "status=success" >> "$GITHUB_OUTPUT"
else
  echo "status=failure" >> "$GITHUB_OUTPUT"
fi

summary="$(grep -E '^cache: discovered=[0-9]+ processed=[0-9]+ rebuilt=[0-9]+ unchanged=[0-9]+ errors=[0-9]+$' "$output_file" | tail -n 1 || true)"
if [[ -n "$summary" ]]; then
  for field in discovered processed rebuilt unchanged errors; do
    value="$(sed -nE "s/.*${field}=([0-9]+).*/\\1/p" <<< "$summary")"
    echo "${field}=${value}" >> "$GITHUB_OUTPUT"
  done
fi

exit "$cli_status"
