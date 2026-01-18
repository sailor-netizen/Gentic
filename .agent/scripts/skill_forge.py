import os
import subprocess
import re
from collections import Counter

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # .agent/
SKILLS_DIR = os.path.join(BASE_DIR, "skills")

def get_git_log():
    try:
        # Get last 100 commits with stats
        result = subprocess.run(
            ["git", "log", "-n", "100", "--name-only", "--pretty=format:%s"],
            cwd=os.path.dirname(BASE_DIR), # Root
            capture_output=True,
            text=True
        )
        return result.stdout
    except Exception as e:
        print(f"Error reading git log: {e}")
        return ""

def analyze_patterns(log_text):
    # Very basic Heuristic: Count repeated commit messages or file touches
    lines = log_text.split('\n')
    commit_msgs = [line for line in lines if line and not line.startswith('/') and not '.' in line]
    
    msg_counts = Counter(commit_msgs)
    
    proposals = []
    for msg, count in msg_counts.items():
        if count >= 3:
            proposals.append(f"Frequent Task: '{msg}' (Performed {count} times)")
            
    return proposals

def forge_skill_proposal(proposal_name):
    print(f"\n🔥 SKILL FORGE: Detected Pattern [{proposal_name}]")
    print("Drafting new Skill Proposal...")
    
    filename = proposal_name.lower().replace(" ", "-") + ".md"
    content = f"""---
description: Auto-generated skill based on frequent usage of '{proposal_name}'
---
# {filename.replace(".md", "")}

## Trigger
"{proposal_name}", "Do the usual {proposal_name}"

## Process
(Agents: Please fill this in based on the git diff history for this task)
1. ...
2. ...
"""
    # In a real system, we would write this to a 'drafts' folder
    print(f"Proposed file: .agent/skills/_drafts/{filename}")
    print(content)

def main():
    print("⚒️  Igniting Skill Forge...")
    log = get_git_log()
    if not log:
        print("No git history found. Forge is cold.")
        return

    patterns = analyze_patterns(log)
    
    if not patterns:
        print("No strong patterns detected yet. Keep working!")
    else:
        for p in patterns:
            forge_skill_proposal(p)

if __name__ == "__main__":
    main()
