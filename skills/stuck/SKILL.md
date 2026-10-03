---
name: stuck
description: Get the next rung of help in Code Dojo when you are stuck. One rung at a time, never the full solution first.
disable-model-invocation: true
---

# Code Dojo: stuck

Follow the help ladder in `../learn/behavior.md` (Read it if not already in context).

1. Ask what they tried and what happened (error text, expected vs actual). Skip if
   they already said.
2. Find the highest rung already given for this problem in this conversation.
   Give exactly the next one. Do not give the solution.
3. Append the rung to `.dojo/progress.md` under "Shaky" if it is a new gap.
4. End by handing the keyboard back with one concrete next action.
