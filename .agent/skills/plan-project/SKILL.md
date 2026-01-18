---
description: Use this skill to plan a new complex project from a high-level description.
---
# plan-project

## Trigger
"Plan a new project", "Break down this idea", "Create a project plan"

## Process
This skill orchestrates multiple agents to transform a vaguely defined idea into a ready-to-execute plan, optimizing for minimal token usage during execution.

### Step 1: Initialize Planning Phase
**Action**: 
1. Call `task_boundary` with `Mode: PLANNING`.
2. Create/Clear `implementation_plan.md`.

### Step 2: Requirements & Design (Product Owner + Architect)
**Agents**: `Product Owner`, `Lead Architect`
**Action**:
1. **Product Owner**: Draft the "Goal Description" and "User Requirements" in `implementation_plan.md`. Focus on clarity to avoid back-and-forth.
2. **Lead Architect**: Fill the "Proposed Changes" section. Define the file structure, contracts, and data models upfront.
   - *Goal*: Solve the "How" now so the "Doing" is just typing.

### Step 3: Task Breakdown (Scrum Master)
**Agent**: `Scrum Master`
**Action**:
1. Update `task.md` with a granular checklist based on the Architecture.
2. Ensure tasks are atomic (e.g., "Implement User Schema" vs "Build Backend").

### Step 4: User Review (Token Saver)
**Action**:
1. Call `notify_user` to request review of `implementation_plan.md`.
2. **STOP**. Do not proceed to coding until the plan is frozen. This prevents wasted tokens on refactoring due to misunderstood requirements.

## Usage Example
> User: "Plan a Tinder for Cats."
> Agent: Enters PLANNING mode -> Writes `implementation_plan.md` (PO & Architect) -> Updates `task.md` (Scrum Master) -> Asks for approval.

