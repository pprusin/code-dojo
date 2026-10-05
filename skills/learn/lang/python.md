# Python guide

Use after onboarding says Python. Pick the next task from the learner's gaps, not
from this list's order. Always tie a concept to the learner's own project.

## Progression (basics to intermediate)

1. Functions: arguments, return vs print, small pure functions.
2. Data: list, dict, set, tuple; iteration; comprehensions after loops are solid.
3. Control flow and errors: `try/except` specific exceptions, raising, never bare `except`.
4. Files and I/O: `pathlib`, `open` with `with`, `json`, `csv`.
5. Modules and layout: splitting files, imports, `__main__`, no circular imports.
6. Tests: `assert`, `pytest` basics, red-green with tests you write for the learner.
7. Classes and dataclasses: only when data and behavior clearly belong together.
8. Pipelines/CLI: `argparse`, logging, config, separating steps (extract / transform / load).

## Common beginner mistakes to watch for

- Mutable default argument (`def f(x=[])`).
- `print` instead of `return`; functions that do I/O and logic together.
- Bare `except:` or catching and ignoring.
- Modifying a list while looping over it.
- Global state instead of passing arguments.
- Copy-pasted blocks that want to be a function.
- Hard-coded paths and secrets.

## Coaching moves

- Ask "what type is this here?" before they hit a `TypeError`.
- Make them read the traceback aloud: bottom line first, then the file and line.
- Debugging ladder: reproduce, shrink, print/inspect, hypothesis, fix. Do not fix for them.
- Pipelines: have them draw the stages and the shape of data between stages first.
- Idioms (`enumerate`, `zip`, `with`, f-strings): show only after their working version.
- New syntax concept (`class`, `__init__`, `self`, decorators): before the learner writes their own version, first explain the basics of each new keyword (what `self` is and why it exists, when `__init__` runs), then show a short working example on an UNRELATED problem (e.g. `Dog` while the task is `Account`), with its output. The goal is to see the syntax, not to get the solution. Skip if the learner already knows the syntax.
