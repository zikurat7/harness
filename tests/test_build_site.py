import json
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest import mock

from helpers import ROOT, build_site

PREFIX = "window.HARNESS_DATA = "


def load_data_js(path):
    """Parse a generated data.js back into a dict."""
    text = Path(path).read_text(encoding="utf-8")
    body = text.split(PREFIX, 1)[1].rstrip()
    assert body.endswith(";")
    return json.loads(body[:-1])


def build_into(out_path):
    """Run build_site.main() writing to out_path instead of site/data.js."""
    with mock.patch.object(build_site, "OUT", Path(out_path)), redirect_stdout(StringIO()):
        return build_site.main()


class ParseNoteTests(unittest.TestCase):
    def test_splits_front_matter_and_body(self):
        meta, body = build_site.parse_note("---\ntitle: A\ncompany: B\n---\n\nHello\n")
        self.assertEqual(meta, {"title": "A", "company": "B"})
        self.assertEqual(body, "Hello")

    def test_value_may_contain_colons(self):
        meta, _ = build_site.parse_note("---\nsource_url: https://example.com/x\n---\nbody")
        self.assertEqual(meta["source_url"], "https://example.com/x")

    def test_no_front_matter_returns_whole_text(self):
        meta, body = build_site.parse_note("just text\n")
        self.assertEqual(meta, {})
        self.assertEqual(body, "just text")

    def test_unclosed_front_matter_returns_whole_text(self):
        meta, body = build_site.parse_note("---\ntitle: A\n")
        self.assertEqual(meta, {})
        self.assertIn("title: A", body)


class BuildTests(unittest.TestCase):
    def test_build_writes_valid_data_js(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "data.js"
            self.assertIsNone(build_into(out))
            data = load_data_js(out)
        self.assertEqual(set(data), {"built", "vacancies", "prep", "syncLog"})
        self.assertEqual(len(data["vacancies"]), len(list((ROOT / "context/vacancies").glob("*.md"))))

    def test_build_does_not_touch_real_data_js(self):
        real = ROOT / "site" / "data.js"
        before = real.read_bytes()
        with tempfile.TemporaryDirectory() as tmp:
            build_into(Path(tmp) / "data.js")
        self.assertEqual(real.read_bytes(), before)

    def test_committed_data_js_is_up_to_date(self):
        """site/data.js must match context/. Fix: python3 scripts/build_site.py"""
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "data.js"
            build_into(out)
            fresh = load_data_js(out)
        committed = load_data_js(ROOT / "site" / "data.js")
        fresh.pop("built")
        committed.pop("built")
        self.assertEqual(committed, fresh, "site/data.js is stale: run python3 scripts/build_site.py")


if __name__ == "__main__":
    unittest.main()
