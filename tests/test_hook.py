import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "hooks"))
import dojo_hook  # noqa: E402


def ev(cwd, name):
    return {"hook_event_name": name, "cwd": str(cwd)}


class HookTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name).resolve()
        (self.root / ".git").mkdir()

    def tearDown(self):
        self.tmp.cleanup()

    def profile(self, text):
        (self.root / ".dojo").mkdir()
        (self.root / ".dojo" / "profile.md").write_text(text)

    def test_silent_without_state(self):
        self.assertIsNone(dojo_hook.build(ev(self.root, "UserPromptSubmit")))

    def test_reminder_when_active(self):
        self.profile("Mode: active\nLevel: basics\n")
        out = dojo_hook.build(ev(self.root, "UserPromptSubmit"))
        self.assertIn("Code Dojo active", out["hookSpecificOutput"]["additionalContext"])

    def test_session_start_points_to_behavior(self):
        self.profile("Mode: active\n")
        sub = self.root / "src"
        sub.mkdir()
        out = dojo_hook.build(ev(sub, "SessionStart"))
        self.assertIn("behavior.md", out["hookSpecificOutput"]["additionalContext"])

    def test_paused_is_silent(self):
        self.profile("Mode: paused\nLevel: basics\n")
        self.assertIsNone(dojo_hook.build(ev(self.root, "UserPromptSubmit")))

    def test_bad_input(self):
        self.assertIsNone(dojo_hook.build("x"))
        self.assertIsNone(dojo_hook.build({"cwd": "relative"}))


if __name__ == "__main__":
    unittest.main()
