---
name: checkpoint
description: Teach-back and review for finished work in Code Dojo. You explain your code, Claude reviews and logs what is shaky.
disable-model-invocation: true
---

# Code Dojo: checkpoint

Follow Review and Teach-back in `../learn/behavior.md`.

1. Read the code the learner just wrote (ask which files if unclear).
2. Teach-back: they explain what it does and why it is built that way. Do not
   explain it for them. A vague answer means a tiny follow-up exercise.
3. Review: ask "what would you change?", then at most three points
   (bug > design > style), checked against `.dojo/style.md`.
4. Append to `.dojo/progress.md`: done, highest rung used, shaky items. Name the
   one thing to bring back next session.
