---
description: Use this skill to search the permanent knowledge base for past solutions.
---
# consult-memory

## Trigger
"How did we fix this before?", "Check memory", "Do you know about this error?"

## Process
1.  **Extract Query**: Identify the keywords or error message.
2.  **Execute**: Run the knowledge manager script.
    ```bash
    python .agent/scripts/knowledge_manager.py recall "[Query]"
    ```
3.  **Analyze**: Read the output.
    - If matches found: Present them to the user.
    - If no matches: Proceed with normal debugging/research.
