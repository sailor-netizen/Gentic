---
description: Use this to initialize a new project structure.
---
# scaffold-project

## Trigger
"Create a new project", "Start a new app", "Scaffold [name]"

## Process
This skill enforces the standardized project structure.

### Step 1: Directory Setup
**Action**:
1.  **Canonical Name**: Extract the base name (e.g., `my-app`).
2.  **Folder Name**: Append prefix `project-[name]` (e.g., `project-my-app`).
3.  **Location**: Create at `root/project-dir/project-[name]`.

### Step 2: Initialization
**Action**:
1.  Navigate to `root/project-dir/project-[name]`.
2.  **Git/Config**: Initialize with the **Canonical Name** (NO prefix).
    - `package.json` -> `"name": "my-app"`
    - `git init` -> Remote origin should be `.../my-app.git`
3.  Create standard subfolders: `src`, `tests`, `docs`.