import os
import json

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KNOWLEDGE_DIR = os.path.join(BASE_DIR, "knowledge")
SOLUTIONS_FILE = os.path.join(KNOWLEDGE_DIR, "solutions.json")

def init_knowledge():
    if not os.path.exists(KNOWLEDGE_DIR):
        os.makedirs(KNOWLEDGE_DIR)
        print(f"Created {KNOWLEDGE_DIR}")

    if not os.path.exists(SOLUTIONS_FILE):
        initial_data = [
            {
                "problem": "Example: Build fails with missing dependency",
                "fix": "Run npm install to ensure all packages are linked.",
                "tags": ["build", "npm"]
            }
        ]
        with open(SOLUTIONS_FILE, "w", encoding="utf-8") as f:
            json.dump(initial_data, f, indent=2)
        print(f"Initialized {SOLUTIONS_FILE}")
    else:
        print(f"{SOLUTIONS_FILE} already exists.")

if __name__ == "__main__":
    init_knowledge()
