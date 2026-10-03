# First-run repo scan

Read-only. Budget: keep it to roughly 15 files and one pass; this is orientation,
not an audit. Skip vendored and generated paths (node_modules, .venv, dist,
build, lockfiles, binaries, .git).

1. Layout: file tree to depth 3. Manifests (`pyproject.toml`, `requirements.txt`,
   `package.json`, `*.csproj`). README if present.
2. Entry points and the 10-15 most central files (imported most, or largest and
   non-generated). Read them; skim the rest by name.
3. `git log -n 30 --oneline` if a repo exists, for rhythm and message style.
4. Write `.dojo/project-map.md`: modules, one line each, and the main data flow.
5. Write `.dojo/style.md`: observed habits only, each with a file example:
   naming, typing, error handling, structure, tests, comments, formatting.

Then tell the learner, briefly:
- 3 things you saw about their style (neutral, factual).
- Up to 3 improvement candidates, each phrased as a **question** pointing at a
  file and line ("`db.py:41` catches everything, what happens to a typo there?").
  Do not edit code. Let them pick one to work on; that becomes the first task.
- Anything that looks like a security problem (secrets, injection): say it directly.

If the code is clearly not written by the learner (generated, copied), say so in
`style.md` and judge their own style from their recent commits.
