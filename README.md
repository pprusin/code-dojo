# Code Dojo

**Learn to program by building a real project, with Claude as your coach instead of your ghostwriter.**

AI can write a whole project while you still can't explain how it works. Code Dojo flips the roles: **you write the code**, Claude asks questions, gives graded hints, writes the tests, and reviews what you wrote.

It works on your own projects, in your own repos, in whatever you already build. No separate course, no toy exercises.

---

## How it works

### 1. It asks at the start of every session

Open Claude Code inside a git repo and Claude asks once how to run the session:

| Choice | What happens |
|---|---|
| **Dojo** | Learning mode on for this session only. |
| **Normal** | Code Dojo stays out of the way. Claude behaves as usual. |
| **Normal, and stop asking here** | Same as Normal, and this project is never asked again. |

The choice is per session, so the same repo can be a learning project on Monday and a "just get it done" project on Tuesday. Outside git repos nothing is asked.

### 2. The first time, it gets to know you and your code

In Dojo mode, the first run asks at most three short questions: your level (zero, basics, intermediate), the language, and what you want to build.

If the folder already contains code, Code Dojo does a quick **read-only scan** (about 15 files, no edits):

- `project-map.md`: what each module does and how data flows.
- `style.md`: how *you* write: naming, error handling, structure, tests.
- Then it tells you three things it noticed and up to three **questions** about possible improvements, such as "`db.py:41` catches every exception; what happens to a typo there?" You pick one, and that becomes your first task.

### 3. Then you build, and Claude holds back

You write; Claude coaches. The rules are:

- **Think first.** Before code, you state your approach in a few sentences, or write a plan as comments in an empty file. Claude reacts with at most two questions.
- **The help ladder.** Stuck? Claude gives one rung at a time, never the full answer first:

  1. A question ("what goes in, what comes out?")
  2. A concept hint ("you need to loop over the words")
  3. A plan sketch (pseudocode or comment steps)
  4. An analogous example on a *different* problem
  5. A skeleton with `# TODO` lines for you to fill
  6. The full solution, only after you tried at rung 5, and then you explain it back line by line

  "Just write it" is not refused coldly; it simply moves you one rung up.
- **Claude may write:** tests for behavior you described, skeletons, unrelated examples, reviews.
- **Claude won't write:** your solution to your current task.
- **Teach-back.** When your code works, you explain what it does and why. A vague answer means one more small exercise, not moving on.
- **Review.** First "what would you change?", then at most three points ordered bug, design, style, checked against your own `style.md`.

### 4. It remembers

Notes live in `.dojo/` inside your project: your level, project map, style, and a progress log that records the highest ladder rung you needed and what was shaky. Shaky topics come back in later sessions. Add `.dojo/` to your `.gitignore` if you don't want it committed.

---

## Install

In Claude Code:

```
/plugin marketplace add pprusin/code-dojo
/plugin install code-dojo@code-dojo
```

Or from a terminal:

```
claude plugin marketplace add pprusin/code-dojo
claude plugin install code-dojo@code-dojo
```

Restart Claude Code. Requires Python 3 (for the hook script).

## Commands

| Command | What it does |
|---|---|
| `/code-dojo:learn <what you're building>` | Starts or resumes Dojo for this session. First run: onboarding plus repo scan. Pass `rescan` to refresh `style.md` and `project-map.md`. |
| `/code-dojo:stuck` | Asks what you tried, then gives exactly **one** rung higher on the help ladder. Logs the gap. |
| `/code-dojo:checkpoint` | Teach-back and review of what you just wrote. Logs what is shaky and what to revisit next time. |

Say **"pause dojo"** at any time to switch it off for the rest of the session.

## Skills in detail

### `learn`

The entry point and the home of the coaching rules.

- `SKILL.md`: turns Dojo on for the session, finds `.dojo/`, resumes or runs onboarding.
- `behavior.md`: the rulebook: who writes what, the help ladder, Think and Teach-back checkpoints, how to handle blank pages, "reads fine but can't write", and architecture, plus review style.
- `scan.md`: the first-run repo scan procedure.
- `state-templates.md`: formats of the `.dojo/` files.
- `lang/python.md`: Python curriculum (functions through pipelines), common beginner mistakes, and coaching moves.

### `stuck`

Use it when you are blocked. It finds the highest rung already given for the current problem and gives only the next one, then hands the keyboard back with one concrete action.

### `checkpoint`

Use it when something works. You explain, Claude reviews, and the result goes into `progress.md` so the next session starts from your real weak spots.

## Hooks

One small Python script (`hooks/dojo_hook.py`) keeps the whole thing cheap:

| Event | Behavior |
|---|---|
| Session start or clear (in a git repo) | Tells Claude to ask Dojo, Normal, or stop asking. About 150 tokens, once. |
| Resume, compact, fork | If Dojo was on for the session, tells Claude to re-read the rules. |
| Every prompt | If Dojo is on, injects a two-line reminder (about 50 tokens) to stop the rules from fading in long sessions. |

Dojo state per session is a marker file in `~/.claude/code-dojo/sessions/`. In Normal mode the hook adds nothing.

## Honest limitations

- The rules are instructions to Claude, not a lock. A very insistent prompt can still make it slip. The per-prompt reminder and the ladder design reduce this, but don't eliminate it.
- Only Python has a language guide so far. Other languages work with the generic rules; add `skills/learn/lang/<language>.md` for more.

## Layout

```
.claude-plugin/    plugin.json, marketplace.json
hooks/             hooks.json, dojo_hook.py
skills/learn/      SKILL.md, behavior.md, scan.md, state-templates.md, lang/
skills/stuck/      SKILL.md
skills/checkpoint/ SKILL.md
tests/             test_hook.py
```

## Development

```
python3 -m unittest discover tests
claude plugin validate .
```

## License

MIT
