---
description: Trigger a multi-agent debate to critique and improve a plan before implementation.
---
# adversarial-design

## Trigger
"Run a design review", "Criticize this plan", "Simulate a debate", "Adversarial mode"

## Context
You are the moderator. You must orchestrate a debate between specialized personas.

## Process
1.  **Identify Subject**: What is being built? (e.g., "New Auth System").
2.  **Load Persona A (The Architect)**: Ask: "Propose a robust design."
3.  **Load Persona B (The Attacker)**: Ask: "Find 3 security flaws or edge cases in A's design."
4.  **Load Persona C (The Optimiser)**: Ask: "How can this be faster or cheaper?"
5.  **Synthesis**: Combine all 3 viewpoints into a final `design_spec.md`.

## Output
Present the "Debate Transcript" and the "Final Robust Plan".
