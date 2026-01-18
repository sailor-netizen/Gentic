---
description: Use this skill to check if a component or resource already exists before building it.
---
# find-asset

## Trigger
"Do we have a ...?", "Find a reusable...", "Check the library for..."

## Process
1.  **Search**: Look through `asset-library/` using `list_dir` or `find_by_name`.
2.  **Analyze**: Check `metadata.json` or file contents to see if it matches the user's need.
3.  **Report**:
    - **Found**: "Yes, I found `asset-library/components/Button.tsx`. Shall I copy it to your project?"
    - **Not Found**: "I didn't find an exact match in the library. I can build it from scratch."
