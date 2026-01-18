---
description: Use this skill to save a fix or solution to the permanent knowledge base (JSON).
---
# learn-lesson

## Trigger
"Remember this fix", "Save this solution", "Learn this"

## Context
The user has just solved a problem or you have successfully verified a fix.

## Process
1.  **Extract Info**: Identify the **Problem** (one sentence) and the **Fix** (command or code explanation).
2.  **Execute**: Run the knowledge manager script.
    ```bash
    python .agent/scripts/knowledge_manager.py learn "[Problem Description]" "[The Fix]"
    ```
3.  **Confirm**: Verify the output says "✅ Learned new solution".
