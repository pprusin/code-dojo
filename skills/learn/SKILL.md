---
name: learn
description: Start or resume Code Dojo. Learn to code on a real project; Claude coaches, you write the code. Usage - /code-dojo:learn <what you want to build, or "rescan">
disable-model-invocation: true
---

# Code Dojo: learn

Read [behavior.md](behavior.md) and [guide.md](guide.md) now and follow them for
the rest of the session, not just this command. Use Read, not `cat`.

## Turn Dojo on for this session

First, run: `mkdir -p ~/.claude/code-dojo/sessions && touch ~/.claude/code-dojo/sessions/${CLAUDE_SESSION_ID}`
This marker enables the per-prompt reminder. "Pause dojo" deletes it.

## Locate state

From the current directory go upward looking for `.dojo/`, stop at the nearest
`.git` (file or dir). Use the nearest one. If none, create `.dojo/` at the git
root (or cwd without git). Never use state from another repo; never follow symlinks.
A missing `.dojo/` is normal first run, not an error.

## Resume

If `.dojo/profile.md` has a `Level:` line: Read it (note `Known`, `Unknown`,
`Help`, `Boilerplate`), `style.md`, `project-map.md`, and the end of
`progress.md`. Do not repeat onboarding or re-ask anything already saved. Then
continue with the user's request, or ask what they want to build next.

## First run

1. Onboarding: ask only what the user's message and the repo do not answer:
   what they want to build, and their rough level (zero / basics / intermediate).
   Then Frame and Calibrate from guide.md (decisions, `Known`/`Unknown`, `Help`).
   Write [state-templates.md](state-templates.md) files. If the project uses a
   language with a guide in `lang/<language>.md`, load it. If none exists, coach
   with the generic rules.
2. If the directory already contains code, follow [scan.md](scan.md). If it is
   empty, skip the scan.
3. Start the work: decisions via guide.md, core code through the Think checkpoint
   in behavior.md. Do not propose a design for the user's project.

`rescan` as the argument re-runs scan.md and updates `style.md` / `project-map.md`.
Suggest adding `.dojo/` to `.gitignore` once; do not edit it unasked.
