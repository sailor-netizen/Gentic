---
description: Use this skill to save a file or folder to the asset-library for future reuse.
---
# publish-asset

## Trigger
"Save this to the library", "Publish this component", "Make this reusable"

## Process
1.  **Identify Target**: Determine which file or folder the user wants to save (e.g., `src/components/MyButton.tsx`).
2.  **Determine Category**: Map it to one of: `components`, `features`, `styles`, `utils`, `icons`.
3.  **Copy**: Copy the target to `asset-library/[category]/[name]`.
4.  **Metadata**: Create a `metadata.json` in the destination folder (if it's a folder) or same dir (if file).
    ```json
    {
      "name": "MyButton",
      "dependencies": ["react", "styled-components"],
      "description": "A reusable primary button."
    }
    ```
5.  **Confirm**: Tell the user it is published.
