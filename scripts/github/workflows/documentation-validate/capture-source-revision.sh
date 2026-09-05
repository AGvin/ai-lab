#!/usr/bin/env bash
set -euo pipefail
echo "sha=$(git rev-parse HEAD)" >> "$GITHUB_OUTPUT"
