"""Check every vacancy file follows the format defined in CLAUDE.md."""
import re
import unittest
from datetime import date

from helpers import ROOT, build_site

REQUIRED = [
    "title", "company", "location", "distance_km_from_zwolle", "level", "language",
    "english_option", "contact", "apply_url", "source_url", "fetched", "status",
]
VACANCY_FILES = sorted((ROOT / "context" / "vacancies").glob("*.md"))


class VacancyFormatTests(unittest.TestCase):
    def test_there_are_vacancy_files(self):
        self.assertTrue(VACANCY_FILES)

    def test_each_vacancy(self):
        for path in VACANCY_FILES:
            with self.subTest(file=path.name):
                meta, body = build_site.parse_note(path.read_text(encoding="utf-8"))
                for key in REQUIRED:
                    self.assertTrue(meta.get(key), f"missing or empty '{key}'")
                self.assertIn(meta["language"], {"nl", "en", "both"})
                self.assertIn(meta["english_option"], {"yes", "no", "unknown"})
                self.assertIn(meta["status"], {"open", "closed"})
                self.assertRegex(meta["fetched"], r"^\d{4}-\d{2}-\d{2}$")
                fetched = date.fromisoformat(meta["fetched"])
                self.assertLessEqual(fetched, date.today(), "fetched date is in the future")
                for key in ("apply_url", "source_url"):
                    self.assertRegex(meta[key], r"^https?://\S+$", key)
                self.assertTrue(body, "listing text is empty")

    def test_filename_is_lowercase_slug(self):
        for path in VACANCY_FILES:
            with self.subTest(file=path.name):
                self.assertRegex(path.name, r"^[a-z0-9]+(-[a-z0-9]+)+\.md$")


if __name__ == "__main__":
    unittest.main()
