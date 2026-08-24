# Documentation Requirements

## Scenario Fit

- Present this scenario for organization-scale visual/sensor quality inspection on production lines or manufacturing cells where **defect detection/classification, line-speed latency, camera/sensor geometry, edge deployment, false reject/escape cost, process variation, drift, and safe downstream reject/hold actions** determine the AI route.
- Keep the scenario organization-scale. Generic creative/image understanding belongs elsewhere; supply/demand planning belongs in `supply-chain-and-demand-planning/`; broad industrial workflow automation belongs in `enterprise-workflow-automation/`.
- Do not turn this page into machine-vision hardware procurement guidance. It owns model/runtime/deployment selection and production acceptance for quality inspection.

## Production Quality System Remains Authoritative

- Keep manufacturing execution, quality management, inspection plans, control plans, work instructions, product/lot/serial identity, defect taxonomy, SPC, PLC/automation, and disposition systems authoritative.
- Use vision/AI models to detect/classify/localize/analyze defects and process conformance; do not let model memory redefine product specifications or acceptance criteria.
- Preserve product/line/station/camera/model/version/inspection result/defect/action identifiers for traceability.
- When AI output conflicts with deterministic measurement or approved quality rules, follow the defined quality escalation rather than model confidence.

## Fixed Inspection Problem Before Model Choice

- Define the inspected object/process, camera/sensor position, field of view, illumination, trigger, motion, line speed, product variants, expected defect classes, smallest relevant defect, and required decision latency before evaluating models.
- Separate classification, detection, segmentation, anomaly detection, OCR/mark verification, dimensional/metrology-like measurement, assembly-sequence verification, and video/process compliance because they require different evidence.
- Do not select a general-purpose VLM solely because it can describe an image; production inspection requires repeatable spatial/temporal performance and measurable error rates.
- Keep deterministic classical vision/measurement where it is simpler and more reliable; AI can complement rather than replace it.

## Integrated Industrial Vision Route

- Prefer an industrial vision/edge route when it integrates cameras, deterministic preprocessing, optimized inference, line automation, model lifecycle, and quality-system outputs under production latency/reliability requirements.
- Current Siemens Inspekto and Visual Inspection Cockpit/Industrial Edge are examples of production visual-inspection routes; Siemens also documents deployments combining AI semantic segmentation with classical vision logic directly on industrial edge computers.
- Current NVIDIA Metropolis/TAO/DeepStream provides a current visual-inspection stack for fine-tuning, optimization, real-time streaming inference, synthetic data, and production deployment.
- Treat vendor accuracy/ROI/case-study claims as eligibility evidence only; evaluate on the organization's own defects, line conditions, product mix, and acceptance cost.

## Image Acquisition Is Part of the Model

- Treat camera/sensor, lens, exposure, focus, depth of field, lighting, polarization, trigger timing, background, object pose, motion blur, resolution, and calibration as first-class inputs to inspection quality.
- A model change cannot reliably compensate for inconsistent illumination, missing field of view, motion blur, dirty optics, or insufficient spatial resolution.
- Preserve acquisition configuration/version with datasets and validation runs.
- Test realistic variation in illumination, surface finish, orientation, vibration, speed, wear, contamination, and environmental conditions.
- Use deterministic camera/lighting health checks where possible and distinguish acquisition failure from product defect.

## Defect Taxonomy and Acceptance Rules

- Define defect classes/severity, allowed/forbidden locations, size/tolerance, cosmetic versus functional impact, and product/variant-specific rules with quality owners.
- Preserve `unknown/unclassified/anomaly` states instead of forcing every observation into a known defect.
- Do not let model-generated labels silently redefine the quality taxonomy.
- Keep disposition/rework/scrap/hold rules deterministic and tied to approved quality policy.
- For continuous measurements/tolerances, use calibrated measurement methods where required rather than visual-language estimation.

## Training and Representative Data

- Build datasets from real production variation across product variants, lines/cameras, shifts, suppliers/material lots, environmental conditions, good units, and defect classes.
- Keep train/validation/test separation by relevant production groups to prevent leakage from near-identical sequential images or the same physical item.
- Preserve label definitions, annotation guidelines, reviewer agreement, dataset version, source line/time, and permitted data use.
- Rare defects require deliberate evaluation; do not infer production recall from a dataset dominated by good/common examples.
- Include hard negatives that resemble defects but should pass.

## Synthetic Data and Rare Defects

- Use synthetic defect generation/augmentation when real defect data is scarce only after validating that synthetic examples improve performance on independent real production data.
- Current NVIDIA Metropolis/Cosmos defect-generation workflows explicitly target rare-defect data scarcity and fine-tuning; treat this as a data-generation capability, not proof that synthetic realism transfers to the target line.
- Keep synthetic samples labeled/provenanced separately from real production samples.
- Avoid overfitting to generator artifacts or unrealistic defect geometry/lighting.
- Evaluate real-defect recall before production promotion.

## Anomaly Detection vs Known-Defect Models

- Use anomaly/one-class approaches when good samples are plentiful and unknown deviations matter; use supervised detection/classification when known defect taxonomy and labeled examples support it.
- Current Siemens Inspekto describes an anomaly-oriented approach trained from good samples; evaluate its false-positive/unknown-defect behavior on the exact production surface/variation.
- Do not assume anomaly detection means `all defects` are detected; normal production variation can create false rejects and some defects can look visually normal.
- Preserve unknown/anomaly review to decide whether the taxonomy/model requires updating.

## Classical Vision and AI Fusion

- Keep deterministic checks for barcodes/marks, dimensions, geometry, position, color thresholds, presence/absence, or other stable features when they are robust.
- Combine AI segmentation/detection with classical logic when it reduces false positives or encodes exact acceptance constraints.
- Current Siemens production evidence explicitly combines AI semantic segmentation with classical vision logic in line inspection.
- Make fusion order/rules/version explicit and evaluate end-to-end, not each model in isolation.
- Do not let an LLM reinterpret deterministic measurement tolerances during runtime.

## Edge and Real-Time Deployment

- Use edge/on-prem inference when line latency, connectivity, data locality, availability, or deterministic integration requires it.
- Measure complete sensor-to-decision latency including capture, preprocessing, transfer, inference, postprocessing, rule evaluation, PLC/action signaling, and queueing.
- Test sustained throughput at real line speed and peak/burst conditions.
- Define offline/degraded behavior if the AI service, camera, network, or accelerator fails.
- Core safe production behavior must not depend on an unavailable cloud model when the line cannot tolerate the delay/outage.

## Runtime and Hardware Fit

- Bind every deployment conclusion to exact camera streams/resolution/FPS, model artifact, precision, runtime/backend, accelerator, preprocessing, batch/concurrency, host resources, and thermal/power environment.
- Current NVIDIA TAO/DeepStream workflows explicitly optimize models for compute-constrained real-time edge deployment; treat current support matrices/runtime versions as mutable.
- Do not infer practical fit from TOPS, GPU name, model size, or single-image inference alone.
- Measure sustained end-to-end latency, dropped frames, accelerator utilization, memory, thermals, and production uptime.
- Keep unsupported/unmeasured hardware/runtime combinations `Unknown`.

## Multi-Camera and Video Inspection

- Treat synchronization, camera identity, tracking, occlusion, duplicate observations, temporal windows, event boundaries, and cross-camera state as explicit requirements.
- Video/process inspection can verify assembly sequence/SOP/safety behavior but must be evaluated on exact process variants and operator/environment conditions.
- Current NVIDIA factory/video-agent workflows support live video understanding and SOP/inspection use cases; treat generative descriptions as decision support unless deterministic production acceptance has been validated.
- Avoid using open-ended VLM summaries as the sole control signal for safety-critical process actions.

## False Rejects and Defect Escapes

- Measure false reject/scrap/rework cost and false negative/defect escape cost separately.
- Define acceptable thresholds by defect severity/product/customer risk rather than one global accuracy number.
- Report class-level precision/recall and confusion, not overall accuracy alone.
- Sample passed units to detect hidden false negatives.
- Maintain manual/secondary inspection for high-risk defects until evidence supports automation.

## Confidence and Review Routing

- Define review/hold thresholds from measured calibration/error cost, not arbitrary model confidence.
- Route uncertain/novel/low-quality-acquisition cases to human or secondary inspection.
- Sample high-confidence automatic pass/reject decisions for ongoing quality assurance.
- Preserve reviewed corrections as evaluation data.
- Do not allow the model to self-certify uncertain images.

## Production Actions

- Separate inspection verdict from physical/business actions such as reject gate, line stop, hold lot, rework route, scrap, supplier complaint, or MES/QMS record creation.
- Define action preconditions, latency, fail-safe behavior, confirmation/sensors, idempotency, and recovery.
- Use deterministic PLC/automation interlocks for safety/physical actions where appropriate.
- Do not allow a generic agent to directly manipulate machinery or safety controls from free-form vision output.
- Verify that commanded reject/hold action actually occurred and was associated with the correct unit/lot.

## Traceability and Audit

- Preserve image/video/evidence according to quality/privacy policy together with model/runtime/version, acquisition settings, result, confidence/score where meaningful, rules, reviewer correction, and disposition.
- Link inspection outcomes to product/serial/lot/time/station when traceability requires it.
- Protect customer/proprietary product imagery and worker video as sensitive data where applicable.
- Keep audit artifacts sufficient to investigate field escapes, recalls, customer complaints, or model changes.

## Drift and Change Management

- Monitor product variant, supplier/material, lighting/camera, line speed, background, tooling, process, season/environment, and defect-distribution changes.
- Trigger re-evaluation after camera/lighting/line/model/runtime/product/process changes that can alter the input distribution.
- Track pass/reject rates, review rates, class distribution, confidence/calibration, false rejects, discovered escapes, and acquisition-quality metrics over time.
- Do not retrain automatically from every operator correction without label/quality review.
- Version datasets/models/configuration and support rollback to the last validated inspection release.

## Model Promotion and Rollback

- Validate candidate models offline, then shadow mode, then bounded production rollout where practical.
- Compare against the current production system on the same real samples and defined acceptance metrics.
- Require quality/operations owner approval before changing production disposition behavior.
- Keep immediate rollback capability after regression or incident.
- Avoid changing model, camera setup, preprocessing, and quality thresholds simultaneously unless the validation isolates effects.

## Prompt Injection and Generative Vision Agents

- Treat labels, packaging text, screens, documents, signs, operator displays, QR-linked/web content, and other visible text as untrusted input when a VLM/agent can call tools.
- Visual/text content must not override inspection policy or expand tool/action authority.
- Keep inspection action rules outside image-controlled prompts.
- Do not expose secrets/system instructions because a product/label contains adversarial text.
- Include visual prompt-injection cases when generative agents are used in quality workflows.

## Worker Privacy and Safety

- When cameras include workers, define purpose, access, retention, acceptable monitoring, and applicable labor/privacy policy.
- Do not repurpose worker footage for performance/disciplinary scoring without explicit approved governance.
- Separate product-quality evidence from employee monitoring where possible.
- For safety-related observations, preserve deterministic safety systems and qualified review appropriate to consequence.

## Evaluation Suite

- Build a versioned production evaluation set stratified by product/variant, line/camera, defect class/severity, good variation, acquisition quality, environment, supplier/material, and time.
- Include rare defects, hard negatives, unknown anomalies, borderline tolerances, dirty/blurred/occluded images, lighting variation, prompt-injected visible text where generative agents are used, and cases requiring review.
- Score class-level recall/precision, false reject, defect escape, localization/segmentation quality, calibration/review routing, acquisition failures, sensor-to-decision latency, throughput, action correctness, and cost.
- Evaluate on independent real production data even when synthetic training data is used.
- Re-run regression after dataset/model/runtime/camera/lighting/product/process/rule changes.

## Concurrency and Reliability

- Measure camera stream count, FPS/resolution, products per minute, burst/queue behavior, inference capacity, memory, frame drops, network/edge availability, model startup/update, and PLC/MES/QMS integration latency.
- Define fail-safe behavior for camera/model/accelerator/network failure.
- Monitor p50/p95/p99 latency and dropped/late inspections where deadlines matter.
- Keep production-safe operation possible during AI maintenance/outage according to process risk.

## Cost per Accepted Inspection

- Compare **total cost per accepted inspected unit/lot**: cameras/lighting, edge compute, model training/labeling, synthetic data, software/runtime, integration, maintenance, review labor, false rejects/rework/scrap, defect escapes/claims/recalls, and downtime.
- A model with higher nominal accuracy can be worse economically if it increases latency or false rejects materially.
- An edge model can be preferable to a cloud model when line availability/data transfer/latency dominate.
- Measure production yield/quality outcomes cautiously; vendor case-study ROI is not organization-specific evidence.

## Local/Private and Hybrid Route

- Edge/private inference is normally the preferred production route when line latency/availability or proprietary image data requires it; hosted training/management can still be used when approved.
- Define which images/metadata leave the plant/site for training, support, observability, or model management.
- Do not silently upload production imagery to external services.
- Hybrid workflows can train/augment centrally while deploying validated inference locally, provided artifact/provenance/security boundaries are controlled.
- Escalate shared model/runtime infrastructure to `internal-ai-platform/` when it becomes cross-factory/organization infrastructure.

## Escalation Triggers

- Move to this scenario when visual/sensor inspection directly affects production quality/disposition at organization scale.
- Move to `supply-chain-and-demand-planning/` when planning/inventory/supply decisions dominate.
- Move to `enterprise-workflow-automation/` when agents coordinate broad business workflows beyond inspection.
- Move to `high-security-environment/` when plant/network isolation or sovereign constraints dominate.
- Narrow/stop automated disposition when defect escape/false reject/action/reliability evidence cannot meet acceptance.

## Hardware-Specific Model Selection Continuation

- Link `../../../hardware/` when exact deployed industrial edge/server hardware materially constrains model/runtime fit.
- Use the applicable `../../../hardware/sub/embedded/`, `../../../hardware/sub/computers/`, or `../../../hardware/sub/servers/` route according to the fixed deployment target.
- Hardware purchasing remains outside this scenario.

## Canonical Links

- Link supply-chain/workflow/internal-platform/high-security concerns to their organization scenario owners.
- Link named industrial vision software/services and exact models to canonical catalog owners when materialized.
- Keep exact fixed-hardware fit in the hardware selection journey rather than duplicating it here.

## Evidence and Freshness

- Re-evaluated on **2026-08-24** using current first-party NVIDIA Metropolis/TAO/DeepStream visual-inspection and synthetic-defect workflows plus current Siemens Inspekto, Visual Inspection Cockpit/Industrial Edge, and Teamcenter Quality inspection-planning material.
- Current evidence establishes production visual-inspection routes using fine-tuned vision models, real-time edge inference, synthetic rare-defect data, anomaly detection, classical-vision fusion, and production/QMS integration. Vendor case-study performance remains external evidence, not organization-specific acceptance proof.
- Models, TAO/DeepStream/runtime versions, industrial-edge support, camera/tool integration, synthetic-data tools, product features, and quality workflows are mutable; recheck them before rendering current guidance.
- Real production datasets, exact line acquisition/deployment, approved quality rules, and measured false-reject/escape/action performance remain the acceptance authority.

## Validation

- Camera/sensor acquisition, classical logic, model inference, quality rules, and physical/business action are distinct pipeline stages.
- Overall accuracy is not used instead of class-level defect recall/false reject/escape evidence.
- Synthetic defect data is validated against independent real production data.
- Exact edge runtime/hardware/stream configuration and sustained line-speed performance determine fit.
- Unknown/uncertain/acquisition-failure cases can route to review rather than forced pass/reject.
- Production reject/hold/line actions have deterministic fail-safe and verification boundaries.
- Visible attacker-controlled text cannot expand generative-agent authority.
- Drift/change control covers camera/lighting/product/process/model/runtime changes.
- Hardware purchasing remains outside the scenario.
- Mutable current claims carry the 2026-08-24 evidence boundary.
