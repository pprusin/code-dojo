import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "hooks"))
import dojo_hook  # noqa: E402


class HookTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name).resolve()
        (self.root / ".git").mkdir()
        dojo_hook.MARKER_DIR = self.root / "markers"
        dojo_hook.MARKER_DIR.mkdir()

    def tearDown(self):
        self.tmp.cleanup()

    def ev(self, name, source=None, sid="s1"):
        return {"hook_event_name": name, "cwd": str(self.root),
                "session_id": sid, "source": source}

    def text(self, payload):
        out = dojo_hook.build(payload)
        return out["hookSpecificOutput"]["additionalContext"] if out else None

    def test_startup_asks(self):
        self.assertIn("AskUserQuestion", self.text(self.ev("SessionStart", "startup")))

    def test_clear_asks(self):
        self.assertIn("AskUserQuestion", self.text(self.ev("SessionStart", "clear")))

    def test_ask_never_is_silent(self):
        (self.root / ".dojo").mkdir()
        (self.root / ".dojo" / "profile.md").write_text("Ask: never\n")
        self.assertIsNone(self.text(self.ev("SessionStart", "startup")))

    def test_no_marker_no_reminder_no_restore(self):
        self.assertIsNone(self.text(self.ev("UserPromptSubmit")))
        self.assertIsNone(self.text(self.ev("SessionStart", "resume")))

    def test_marker_enables_reminder_and_restore(self):
        (dojo_hook.MARKER_DIR / "s1").touch()
        self.assertIn("Code Dojo active", self.text(self.ev("UserPromptSubmit")))
        self.assertIn("behavior.md", self.text(self.ev("SessionStart", "compact")))

    def test_marker_is_per_session(self):
        (dojo_hook.MARKER_DIR / "s1").touch()
        self.assertIsNone(self.text(self.ev("UserPromptSubmit", sid="s2")))

    def test_bad_input(self):
        self.assertIsNone(dojo_hook.build("x"))
        self.assertIsNone(dojo_hook.build({"cwd": "rel", "session_id": "a"}))
        self.assertIsNone(dojo_hook.build(self.ev("UserPromptSubmit", sid="../x")))


if __name__ == "__main__":
    unittest.main()
