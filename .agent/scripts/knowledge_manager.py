import json
import os
import sys
import difflib

# Paths (Relative to this script in .agent/scripts/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # .agent/
KNOWLEDGE_DIR = os.path.join(BASE_DIR, "knowledge")
SOLUTIONS_FILE = os.path.join(KNOWLEDGE_DIR, "solutions.json")

def load_solutions():
    if not os.path.exists(SOLUTIONS_FILE):
        return []
    try:
        with open(SOLUTIONS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save_solutions(data):
    with open(SOLUTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def learn(problem, fix, tags=[]):
    data = load_solutions()
    entry = {
        "problem": problem,
        "fix": fix,
        "tags": tags
    }
    data.append(entry)
    save_solutions(data)
    print(f"✅ Learned new solution for: {problem}")

def recall(query):
    data = load_solutions()
    if not data:
        print("No knowledge base found.")
        return

    # Simple fuzzy search on problem text
    print(f"🔍 Searching knowledge for: '{query}'...")
    
    matches = []
    for entry in data:
        # Check basic containment
        if query.lower() in entry["problem"].lower():
            matches.append(entry)
            continue
        # Check similarity
        ratio = difflib.SequenceMatcher(None, query.lower(), entry["problem"].lower()).ratio()
        if ratio > 0.6:
            matches.append(entry)

    if matches:
        print(f"Found {len(matches)} matches:")
        for m in matches:
            print(f"\nProblem: {m['problem']}")
            print(f"Fix: {m['fix']}")
            print("-" * 20)
    else:
        print("No exact matches found in memory.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python knowledge_manager.py [learn|recall] [args...]")
        sys.exit(1)

    command = sys.argv[1]
    
    if command == "learn":
        if len(sys.argv) < 4:
            print("Usage: python knowledge_manager.py learn 'problem' 'fix'")
        else:
            learn(sys.argv[2], sys.argv[3])
            
    elif command == "recall":
        if len(sys.argv) < 3:
            print("Usage: python knowledge_manager.py recall 'query'")
        else:
            recall(sys.argv[2])
