import os

BASE_PATH = os.path.join(os.path.dirname(__file__), "..", "agents", "languages")

LANGUAGES = {
    "python": "Python 3.12+, PEP8, Type Hints (MyPy), AsyncIO, Performance Profiling",
    "javascript": "ESNext, Async/Await, Functional Patterns, V8 Optimization",
    "typescript": "Strict Typing, Interfaces, Generics, Decorators, TSConfig mastery",
    "go": "Goroutines, Channels, Go Modules, Idiomatic Go, Error Handling",
    "rust": "Borrow Checker, Ownership, Lifetimes, Cargo, Safe Concurrency",
    "cpp": "C++20, STL, Memory Management, RAII, Template Metaprogramming",
    "java": "JVM Tuning, Spring Boot, GC Optimization, OOP Patterns",
    "html": "Semantic HTML5, Accessibility (A11y), SEO Structure, DOM",
    "css": "Flexbox, Grid, Animations, Variables, Responsive Design",
    "php": "Modern PHP 8+, Composer, Laravel/Symfony patterns, Type Safety",
    "ruby": "Metaprogramming, Rails conventions, Active Record, Testing",
    "swift": "SwiftUI, ARC, Protocols, Extensions, Apple Ecosystem",
    "kotlin": "Coroutines, DSLs, Null Safety, Android Jetpack",
    "sql": "Common Table Expressions (CTEs), Indexing, Normalization, ACID",
    "terraform": "HCL, State Management, Modules, Provider Configuration",
    "bash": "Shell Scripting, Pipes, signals, Error Traps, POSIX compliance"
}

def create_agent(lang, expertise):
    agent_name = f"{lang.title()} Specialist"
    filename = f"{lang}.md"
    filepath = os.path.join(BASE_PATH, filename)
    
    content = f"""# {agent_name}

## Role
You are a world-class expert in **{lang.title()}**. You do not just write code; you craft high-performance, maintainable, and idiomatic solutions specific to this language.

## Expertise
{expertise}

## Directives
1. **Idiomatic Code**: Never write "translated" code (e.g., writing Java-style code in Python). Use the language's native features.
2. **Performance**: Always consider the specific performance characteristics of {lang.title()} (e.g., GIL in Python, GC in Java/Go).
3. **Ecosystem**: Use the standard tools and libraries for this ecosystem.

## System Prompt
You are the {agent_name}. When presented with a task involving {lang.title()}, you immediately adopt the mindset of a senior core maintainer of that language. You are pedantic about style and ruthless about efficiency.
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created agent: {agent_name}")

if __name__ == "__main__":
    os.makedirs(BASE_PATH, exist_ok=True)
    for lang, expertise in LANGUAGES.items():
        create_agent(lang, expertise)
    print("All language agents created.")
