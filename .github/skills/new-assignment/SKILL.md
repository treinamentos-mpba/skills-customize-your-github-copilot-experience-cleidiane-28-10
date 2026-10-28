---
name: new-assignment
description: "Create or add an educational programming assignment to this repository. Use when asked to create, design, or publish a new assignment, exercise, or programming task; includes README structure, optional starter code, and config.json registration."
---

# New Assignment

Use this workflow to add a complete, discoverable assignment to the educational portal.

## Procedure

1. Choose a short, descriptive kebab-case ID and check `config.json` to ensure it is not already in use.
2. Read [the assignment design guide](./references/assignment-guide.md), [the assignment template](../../../templates/assignment-template.md), and the applicable assignment instructions in `../../instructions/assignments.instructions.md`.
3. Create `assignments/<id>/README.md` using the template's section structure. Keep the student-facing language clear and encouraging. Include 2 to 4 tasks that progress from a quick first success to more challenging work, with one central learning focus. Use the exact section headings expected by the project, including `## 🎯 Objetivo` and `## 📝 Tarefas`; describe each task and list specific, measurable requirements.
4. Add `starter-code.py` only when boilerplate or a required function/class/API structure helps students focus on the learning goal. Leave clear implementation points, and ensure the starter code agrees with the README.
5. Register the assignment from the repository root with the existing script:

   ```bash
   node .github/skills/new-assignment/scripts/update-config.js <id> "<title>" "<description>"
   ```

   This script adds a due date one week from the current date. Check `config.json` first because the script does not prevent duplicate IDs.
6. If the assignment has a downloadable starter file or other attachment, create the file first, then register it with:

   ```bash
   node .github/skills/new-assignment/scripts/add-attachment.js <id> "Starter Code" starter-code.py python
   ```

   Use a descriptive display name and the appropriate file type for other attachments.
7. Verify that the assignment ID, folder path, README, and any attachment paths agree with `config.json`. Parse `config.json` and syntax-check starter code when applicable.

## Constraints

- Keep assignment files in `assignments/<id>/` and use `README.md` for the instructions.
- Do not add unrelated files or sections beyond the template unless requested.
- Do not implement the complete solution in starter code; leave the core learning work to the student.
- Do not duplicate an existing assignment ID or append a second copy of an existing entry in `config.json`.
