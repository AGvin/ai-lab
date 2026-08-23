# Documentation Requirements

## Requirements

- Present `teams/` for bounded multi-person working groups whose members share workflows, budgets, tools, repositories, datasets, knowledge, review responsibilities, or delivery goals.
- Keep team scenarios below organization scale: a team page may include shared administration and controls, but centralized organization-wide platform ownership, enterprise governance, compliance architecture, high concurrency, or cross-system policy belongs to `organizations/` when those concerns determine the route.
- Evaluate model routes against shared task distribution, collaboration/review patterns, data access, seat/API economics, usage variance, agent permissions, quality controls, and accepted-result cost rather than multiplying an individual recommendation by headcount.
- Distinguish team-level shared tools and workers from organization-wide gateways/platforms. When legacy material mixes both, keep bounded team workflow here and move central identity, budgets, logging, vendor contracts, and platform concerns to the applicable organization scenario.
- Require explicit sandboxing, least privilege, approval gates, and independent verification for team coding/agent workflows when models can execute commands or modify shared artifacts.
- Navigate only materialized direct-child scenarios; detailed model candidates, team-specific evaluation, trade-offs, and escalation triggers remain with the applicable scenario child.

## Validation

- Every materialized child is a shared team workflow and does not silently become an organization-wide platform or governance design.
- Team recommendations account for shared review, permissions, usage distribution, and total accepted-result cost rather than only per-user model quality.
- The page does not duplicate scenario content or create placeholders for approved but unauthored team routes.
