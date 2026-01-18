# 📚 Asset Library

This directory is the central store for reusable assets. **Agents must check here before building new components.**

## Structure
- **`/components`**: UI Components (React, Vue, etc.) - e.g., `Button.tsx`, `Modal.vue`.
- **`/features`**: Full functional modules - e.g., `Authentication`, `PaymentGateway`.
- **`/styles`**: CSS, Sass, or Theme definitions.
- **`/utils`**: Helper functions - e.g., `date-formatter.ts`, `math-utils.js`.
- **`/logos`**: Brand assets.
- **`/icons`**: SVG or font icons.

## Usage
- **To Publish**: Use the `publish-asset` skill.
- **To Use**: Use the `find-asset` skill to locate existing code.
