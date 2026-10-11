# Documentation Requirements

## Requirements

- Present `testing/` as the development-tools index for software whose primary role is automated testing.
- Render every materialized direct-child testing tool once using validated child navigation; do not hard-code Playwright as the sole testing tool. Keep protocol test/debugging inspectors and security assessment scanners distinct from generic browser end-to-end tests.
- Keep generic workflow/integration automation under `software/automation/` rather than conflating it with test frameworks.

## Validation

- Every listed direct child resolves to a canonical software profile and navigation matches the live materialized set.
- The category does not classify testing software merely as AI-agent software because it exposes agent integrations.
