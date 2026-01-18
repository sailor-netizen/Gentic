# Cross-Platform Agent Guide

Your Agentic System is now **Universal**. You can use the intelligence defined in `.agent/` with almost any AI coding tool.

## 1. Cursor IDE
**Status**: ✅ Automatically Configured
**File**: `.cursorrules`
**Usage**: Just open a chat in Cursor. It will automatically read `.cursorrules` and know about your Agents, Memory, and Skills.

## 2. GitHub Copilot
**Status**: ✅ Automatically Configured
**File**: `.github/copilot-instructions.md`
**Usage**: Copilot Chat will now respect your defined personas (e.g., "Act as Lead Architect") and follow your project standards.

## 3. Raw Models (Gemini, ChatGPT, GLM-4, Claude.ai, Minimax)
**Status**: 📋 Manual Paste
**File**: `unified_system_prompt.md`
**Usage**: 
1. Open this file.
2. Copy the entire content.
3. Paste it as the **System Instruction** or the first message in the chat context.
4. The model will instantly "download" your entire agent team and memory.

## 4. Keeping it Sync'd
If you add new agents or update memory, simply run:
```bash
python generate_configs.py
```
This will re-compile the source of truth (`.agent/`) into the specific config files.
