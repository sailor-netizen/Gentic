# Project Memory & changelog

This file serves as the long-term memory for the project. It records architectural decisions, lessons learned, and a high-level changelog of major features. Agents should consult this file before making significant changes to understand the "why" behind existing code.

## Architectural Decisions
- **[2024-01-17] Project Structure**: All projects must be created inside `project-dir/`.
- **[2024-01-17] Naming Convention**: 
    - **Local Folder**: `project-[name]` (e.g., `project-discord-bot`).
    - **Internal/Git Name**: `[name]` (e.g., `discord-bot`).
- **[2024-01-17] Agentic Infrastructure**: Decided to implement a directory-based skill system (`.agent/skills/`) and a centralized agent definition file (`.agent/agents/agent.md`) to allow for modular and scalable agent interactions.
- **[2024-01-17] Standardized Structure**: All components must follow a strict modular structure (Logic, Style, Test) to facilitate automated refactoring and testing.
- **[2024-01-17] Asset First Policy**: Before building ANY new UI component or helper, agents MUST run `find-asset` to check the `asset-library/`. Reusability is priority #1.
- **[2024-01-17] Knowledge Base**: Solutions to tricky bugs must be saved using `learn-lesson` (JSON Memory).
- **[2024-01-17] Hive Mind**: Agents are part of a global system. The `sync_hive_mind` script should be run periodically to backup intelligence.

## Lessons Learned
- *[Example]*: Don't mix logic and styles in the same file; it breaks the `component-refactor` skill.
- *[Example]*: Always run `npm install` after scaffolding a new project to ensure dependencies are linked.

## Changelog
- **v0.0.1**: Initial setup of agent infrastructure (Skills, Agents, Memory).
