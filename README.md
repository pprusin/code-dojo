# Code Dojo

Learn to program on a real project. You write the code; Claude coaches.

- **Help ladder:** question, hint, plan, analogous example, skeleton, solution (last). One rung per request.
- **Think / teach-back checkpoints:** you state the approach first, explain it after.
- **Repo scan on first run:** reads an existing project, records your style, asks questions about improvements instead of rewriting.
- **Memory:** `.dojo/` notes your shaky spots and brings them back.
- **Light on tokens:** a 2-line reminder per prompt; guides are read once per session.

## Install

```
/plugin marketplace add pprusin/code-dojo
/plugin install code-dojo@code-dojo
```

Restart Claude Code in your project, then:

```
/code-dojo:learn we are building a data pipeline in Python
```

Other commands: `/code-dojo:stuck`, `/code-dojo:checkpoint`. Say "pause dojo" to switch it off.
Languages live in `skills/learn/lang/<language>.md` (Python first).

## Dev

`python3 -m unittest discover tests`
