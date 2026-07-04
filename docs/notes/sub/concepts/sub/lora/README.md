# LoRA

LoRA means Low-Rank Adaptation.

## Purpose

Use this page to document LoRA as a practical AI concept for model adaptation and fine-tuning workflows.

## What it is

LoRA is a parameter-efficient adaptation technique. It adapts a model by training a smaller set of additional parameters instead of updating all original model weights.

## When it is used

- Adapting a model to a task or style.
- Fine-tuning with lower compute or storage requirements than full fine-tuning.
- Creating reusable adapters for model variants.

## Advantages

- Lower training cost than full fine-tuning.
- Smaller adapter artifacts.
- Easier experimentation with multiple task-specific variants.

## Disadvantages

- Compatibility depends on the base model and runtime.
- Quality depends on training data and configuration.
- Adapters can be misused or mismatched with unsupported models.

## Compatibility

Compatibility must be verified for each base model, format, runtime, and workflow.

## Common use cases

- Style adaptation.
- Domain adaptation.
- Task-specific tuning.
- Personal or project-specific adapters.
