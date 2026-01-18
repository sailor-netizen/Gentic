# Model Context Protocol (MCP) Integration

Antigravity natively supports the Model Context Protocol (MCP). This allows you to connect external data sources (Databases, APIs, Local Files) and tools directly to the agent.

## 1. How to Connect an MCP Server

Connection happens at the **Client/IDE Level**, not inside this `.agent` folder. You need to configure your AI Client (e.g., VS Code Extension, Desktop App) to point to the MCP server.

**Typical Configuration (`claude_desktop_config.json` or Extension Settings):**
```json
{
  "mcpServers": {
    "postgres": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "mcp/postgres", "postgresql://user:pass@localhost/db"]
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/files"]
    }
  }
}
```

## 2. How the Agent Uses It

Once you connect a server in your settings, **I automatically see the tools**.
- If you add the `postgres` server, I gain tools like `query_database`.
- If you add the `github` server, I gain tools like `create_issue`.

## 3. Best Practice: "Wrapping" MCP in a Skill

To ensure specialized agents use these tools correctly, you should create a **Skill**.

### Example: `.agent/skills/mcp-postgres/SKILL.md`
```markdown
---
description: Use this skill when the user asks to query the live database.
---
# mcp-postgres

## Trigger
"Check the database", "Run a query", "Debug DB data"

## Context
We have an MCP server connected to the `users` database.

## Process
1. **Schema Check**: First, use `get_table_schema` (MCP Tool) to understand the structure.
2. **Safety**: NEVER run `DROP` or `DELETE` without explicit user confirmation.
3. **Query**: Use `query_database` (MCP Tool) to fetch data.
```

## 4. Current Status
To check what valid MCP tools are currently available to the agent, simply ask: *"What MCP tools can you see right now?"*
