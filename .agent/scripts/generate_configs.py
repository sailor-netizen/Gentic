import os

# Paths
SCRIPT_DIR = os.path.dirname(__file__)
AGENT_DIR = os.path.join(SCRIPT_DIR, "..")
AGENTS_FILE = os.path.join(AGENT_DIR, "agents", "agent.md")
MEMORY_FILE = os.path.join(AGENT_DIR, "memory", "project_memory.md")
SKILLS_DIR = os.path.join(AGENT_DIR, "skills")
OUTPUT_DIR = os.path.join(AGENT_DIR, "..", "..") # Back to root

def read_file(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def generate_cursorrules(core_agents, memory):
    """Generates .cursorrules for Cursor IDE."""
    content = f"""# Cursor Rules (Auto-Generated)

You are an intelligent agent powered by the Antigravity system.
Always check the following context before answering:

## 1. Project Memory
{memory}

## 2. Core Agents
{core_agents}

## 3. Skill Access
You have access to skills in `.agent/skills/`. When asked to perform a task, check if a skill exists for it.
"""
    with open(os.path.join(OUTPUT_DIR, ".cursorrules"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Generated .cursorrules")

def generate_copilot_instructions(core_agents, memory):
    """Generates .github/copilot-instructions.md for GitHub Copilot."""
    github_dir = os.path.join(OUTPUT_DIR, ".github")
    os.makedirs(github_dir, exist_ok=True)
    
    content = f"""# Copilot Instructions

## Context
Use this context to guide your code generation.

### Project Memory & Standards
{memory}

### Specialized Personas
You can adopt these personas if the user requests:
{core_agents}
"""
    with open(os.path.join(github_dir, "copilot-instructions.md"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Generated .github/copilot-instructions.md")

def generate_model_specific_prompts(core_agents, memory):
    """Generates tailored prompts for specific LLMs."""
    prompts_dir = os.path.join(AGENT_DIR, "prompts")
    os.makedirs(prompts_dir, exist_ok=True)

    # 1. Claude (Anthropic) - XML Optimized
    claude_content = f"""<system_instructions>
You are an advanced agent powered by the Antigravity system.
<project_memory>
{memory}
</project_memory>

<agent_definitions>
{core_agents}
</agent_definitions>

<instruction>
Adopt the appropriate persona from the agent definitions based on the user's request.
Follow the standards in project memory.
</instruction>
</system_instructions>
"""
    with open(os.path.join(prompts_dir, "claude.md"), "w", encoding="utf-8") as f:
        f.write(claude_content)

    # 2. Gemini (Google) - Markdown/Structure Optimized
    gemini_content = f"""# SYSTEM INSTRUCTIONS
**Context**: You represent the 'Antigravity' agentic workforce.

## 1. MEMORY & CONTEXT
{memory}

## 2. TEAM ROSTER (AGENTS)
{core_agents}

## 3. DIRECTIVE
Act as the most relevant agent for the task. Use the specific "Prompt" defined in the Roster.
"""
    with open(os.path.join(prompts_dir, "gemini.md"), "w", encoding="utf-8") as f:
        f.write(gemini_content)

    # 3. Codex/OpenAI - Standard System Message
    codex_content = f"""# SYSTEM ROLE
You are an expert developer with access to a specialized team of sub-agents.

## PERSISTENT CONTEXT
{memory}

## AVAILABLE PERSONAS
{core_agents}

## INSTRUCTION
Identify the user's need, switch to the correct persona, and execute the task using the project standards.
"""
    with open(os.path.join(prompts_dir, "codex.md"), "w", encoding="utf-8") as f:
        f.write(codex_content)

    # 4. Minimax / GLM - Narrative/Instructional
    minimax_content = f"""User Request: Act as an expert system.
System Configuration:
[Memory]
{memory}
[Agents]
{core_agents}
[Instruction]
Utilize the knowledge above to solve the user's problem. Strict adherence to architecture is required.
"""
    # Write for both
    with open(os.path.join(prompts_dir, "minimax.md"), "w", encoding="utf-8") as f:
        f.write(minimax_content)
    with open(os.path.join(prompts_dir, "glm.md"), "w", encoding="utf-8") as f:
        f.write(minimax_content)

    print(f"Generated model-specific prompts in {prompts_dir}")

def main():
    print("Reading agent data...")
    core_agents = read_file(AGENTS_FILE)
    memory = read_file(MEMORY_FILE)
    
    generate_cursorrules(core_agents, memory)
    generate_copilot_instructions(core_agents, memory)
    generate_model_specific_prompts(core_agents, memory)
    
    print("Universal configuration generation complete.")

if __name__ == "__main__":
    main()
