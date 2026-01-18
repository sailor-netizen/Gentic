import os
import shutil
import sys
import datetime

# Configuration (User can edit this)
# Default to a folder in the User's Home directory
HIVE_MIND_PATH = os.path.join(os.path.expanduser("~"), "AntigravityHive")

AGENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # .agent/

def sync_to_hive():
    if not os.path.exists(HIVE_MIND_PATH):
        os.makedirs(HIVE_MIND_PATH)
        print(f"Created Hive Mind at: {HIVE_MIND_PATH}")
    
    # Simple Copy/Overwrite for now (One-way Sync capability)
    # in a real scenario, this would be a git push/pull
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_dir = os.path.join(HIVE_MIND_PATH, f"backup_{timestamp}")
    
    print(f"Backing up Brain to {backup_dir}...")
    shutil.copytree(AGENT_DIR, backup_dir)
    print("✅ Sync Complete. Your agents are backed up to the Hive Mind.")

if __name__ == "__main__":
    sync_to_hive()
