# MentalHealthBench

MentalHealthBench is OpenAI's open benchmark for AI responses in realistic mental-health conversations, developed with licensed mental-health experts. Its synthetic scenarios span everyday concerns, serious distress, and emergencies, with adult, teen, caregiver, and clinician personas.

## Evaluation scope

Expert-defined rubrics examine safety, context seeking, user agency, and appropriate actionable guidance. Experts review the criteria, while an automated grader evaluates a model's response to the final user message. These roles differ from evaluating a deployed product's entire conversation policy or safeguards.

## Using results

Record the dataset release, scenario/persona and country or language coverage, rubric dimensions and weights, grader revision, and evaluated model configuration. Task counts, methods, public artifacts, and scores can change. The chosen scenario mix does not establish the prevalence of those situations in real usage, and a teen persona is not a measurement of every product-specific teen safeguard.

This benchmark is separate from [HealthBench](../healthbench/), ChatGPT safeguards, crisis-response procedures, and generic safety tests. Scores do not validate clinical care or establish that an AI system can replace a mental-health professional.

## Provenance

- Produced by: [OpenAI](../../../producers/sub/o/sub/openai/)

The expert collaborators define the evaluation's behavioral expectations; their involvement is not a clinical endorsement of evaluated models.

## Official resources

- [MentalHealthBench release and expert rubric methodology](https://openai.com/index/introducing-mentalhealthbench/)
