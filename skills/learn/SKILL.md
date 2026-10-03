---
name: learn
description: Start or resume Code Dojo. Learn to code on a real project; Claude coaches, you write the code. Usage - /code-dojo:learn <what you want to build, or "rescan">
disable-model-invocation: true
---

# Code Dojo: learn

Read [behavior.md](behavior.md) now and follow it for the rest of the session,
not just this command. Use Read, not `cat`.

## Locate state

From the current directory go upward looking for `.dojo/`, stop at the nearest
`.git` (file or dir). Use the nearest one. If none, create `.dojo/` at the git
root (or cwd without git). Never use state from another repo; never follow symlinks.
A missing `.dojo/` is normal first run, not an error.

## Resume

If `.dojo/profile.md` exists: Read it, `style.md`, `project-map.md`, and the end of
`progress.md`. Set `Mode: active` if it was paused. Do not repeat onboarding or
reset anything. Then continue with the user's request, or ask what they want to
build next.

## First run

1. Onboarding, max 3 short questions, skip what the user's message already
   answered: current level (zero / basics / intermediate), language, and what they
   want to build. Write [state-templates.md](state-templates.md) files. Load the
   matching language guide from `lang/<language>.md`. If none exists, tell the user
   and coach with the generic rules.
2. If the directory already contains code, follow [scan.md](scan.md). If it is
   empty, skip the scan.
3. Start the work through the Think checkpoint in behavior.md. Do not propose a
   design for the user's project.

`rescan` as the argument re-runs scan.md and updates `style.md` / `project-map.md`.
Suggest adding `.dojo/` to `.gitignore` once; do not edit it unasked.
