import os

BASE_PATH = os.path.join(os.path.dirname(__file__), "..", "skills")

def create_skill(name, description, instructions):
    skill_dir = os.path.join(BASE_PATH, name)
    os.makedirs(skill_dir, exist_ok=True)
    
    content = f"""---
description: {description}
---
# {name}

{instructions}
"""
    with open(os.path.join(skill_dir, "SKILL.md"), "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Created skill: {name}")

# --- Language Skills Generator ---
LANGUAGES = [
    "javascript", "typescript", "python", "html", "css", "php", "ruby", "perl", "lua",
    "go", "rust", "cpp", "c", "java", "csharp",
    "swift", "kotlin", "dart", "flutter",
    "r", "julia", "haskell", "scala", "elixir",
    "sql", "terraform", "bash", "powershell"
]

for lang in LANGUAGES:
    name = f"skill-{lang}"
    desc = f"Use this skill when writing, debugging, or reviewing {lang.replace('cpp', 'C++').replace('csharp', 'C#').title()} code."
    instr = f"""
## Role
You are an expert {lang.title()} developer.

## Standards
- Follow idiomatic patterns for {lang}.
- Ensure code is efficient, secure, and readable.
- Use best practices for error handling and memory management.
"""
    create_skill(name, desc, instr)

# --- Functional Skills ---
FUNCTIONAL_SKILLS = {
    "scaffold-project": {
        "desc": "Use this to initialize a new project structure.",
        "instr": "## Steps\n1. Create standard folders: `src`, `tests`, `docs`.\n2. Initialize git.\n3. Create `.gitignore`.\n4. specific to the tech stack, run init commands (e.g., `npm init`, `go mod init`)."
    },
    "create-component": {
        "desc": "Use this to create a new modular UI component.",
        "instr": "## Steps\n1. Create folder `src/components/[ComponentName]`.\n2. Create `[ComponentName].tsx` (Logic).\n3. Create `[ComponentName].module.css` (Style).\n4. Create `[ComponentName].test.tsx` (Test).\n5. Ensure no logic leaks into styles."
    },
    "create-api-endpoint": {
        "desc": "Use this to generate a backend API route.",
        "instr": "## Steps\n1. Define the route handler.\n2. Implement input validation (Zod/Joi).\n3. Call service layer (do not put business logic in controller).\n4. Return standard error/success response."
    },
    "dockerize-app": {
        "desc": "Use this to add Docker support.",
        "instr": "## Steps\n1. Create `Dockerfile` optimized for multi-stage builds.\n2. Create `.dockerignore`.\n3. Create `docker-compose.yml` for local dev.\n4. Minimize image size (use alpine/distroless)."
    },
    "setup-ci-pipeline": {
        "desc": "Use this to configure CI/CD.",
        "instr": "## Steps\n1. content depends on provider (GitHub Actions/GitLab).\n2. Define stages: Build, Lint, Test, Deploy.\n3. Cache dependencies to speed up runs."
    },
    "run-tests": {
        "desc": "Use this to execute the test suite.",
        "instr": "## Steps\n1. Identify test runner (Jest/Pytest/Go Test).\n2. Run tests with coverage flag.\n3. Report failures with context."
    },
    "generate-docs": {
        "desc": "Use this to generate project documentation.",
        "instr": "## Steps\n1. Parse code comments/docstrings.\n2. Update `README.md`.\n3. Generate API references if applicable.\n4. Ensure examples are runnable."
    },
    "perform-code-review": {
        "desc": "Use this to review code against standards.",
        "instr": "## Checklist\n- [ ] Naming conventions followed?\n- [ ] No hardcoded secrets?\n- [ ] Tests added/passed?\n- [ ] Error handling robust?\n- [ ] Performance pitfalls avoided?"
    },
    "optimize-assets": {
        "desc": "Use this to compress images and fonts.",
        "instr": "## Steps\n1. Convert images to WebP/AVIF.\n2. Subset fonts.\n3. Minify SVG files."
    },
    "audit-security": {
        "desc": "Use this to scan for vulnerabilities.",
        "instr": "## Steps\n1. Run `npm audit` or equivalent.\n2. Check for SAST (Static Analysis Security Testing).\n3. Review deep dependencies."
    },
    "manage-deps": {
        "desc": "Use this to update and prune dependencies.",
        "instr": "## Steps\n1. Check for unused packages.\n2. Update minor versions safely.\n3. Lockfile sync."
    },
    "migrate-db": {
        "desc": "Use this to handle database schema changes.",
        "instr": "## Steps\n1. Create migration file with timestamp.\n2. Write Up/Down scripts.\n3. Verify data integrity before applying."
    },
    "deploy-staging": {
        "desc": "Use this to deploy to a staging environment.",
        "instr": "## Steps\n1. Build for production.\n2. Push to staging registry/server.\n3. Run smoke tests."
    },
    "analyze-bundle": {
        "desc": "Use this to analyze build size.",
        "instr": "## Steps\n1. Run build with stats enabled.\n2. Check for large dependencies.\n3. Identify tree-shaking failures."
    },
    "format-code": {
        "desc": "Use this to enforce code formatting.",
        "instr": "## Steps\n1. Run formatter (Prettier/Black).\n2. Fix linting errors (ESLint/Pylint)."
    },
    "gen-seed-data": {
        "desc": "Use this to generate mock data for testing.",
        "instr": "## Steps\n1. Identify data models.\n2. Use faker library to create realistic data.\n3. Populate local DB."
    },
    "check-links": {
        "desc": "Use this to find broken links in project.",
        "instr": "## Steps\n1. Crawl local files/docs.\n2. Verify internal and external links.\n3. Report 404s."
    },
    "parse-logs": {
        "desc": "Use this to analyze error logs.",
        "instr": "## Steps\n1. Read log file.\n2. Group errors by stack trace.\n3. Identify most frequent issues."
    },
    "update-changelog": {
        "desc": "Use this to update the version history.",
        "instr": "## Steps\n1. Read git commit history.\n2. Group commits by type (feat, fix, chore).\n3. Prepend to `CHANGELOG.md`."
    },
    "extract-function": {
        "desc": "Use this refactoring tool to extract code.",
        "instr": "## Steps\n1. Identify block of code to extract.\n2. Create new function with parameters.\n3. Replace block with function call.\n4. Verify tests pass."
    }
}

for key, data in FUNCTIONAL_SKILLS.items():
    create_skill(key, data["desc"], data["instr"])

print("All skills generated successfully.")
