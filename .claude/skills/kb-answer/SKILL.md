---
name: kb-answer
description: Answer questions about junior SWE vacancies in and around Zwolle, how to contact the employer, and how to prepare for the interview, using only the saved knowledge in context/. Use for any question about current vacancies, companies, contacts, requirements, English options, or interview preparation.
---

# kb-answer

Answer the user's question from `context/` only. The rules in `CLAUDE.md` apply: cite, flag stale data, never invent contacts, say "I don't know" when the files don't cover it.

## Steps
1. **Find the evidence.**
   - Vacancies: Glob `context/vacancies/*.md`, then Grep the headers (company, location, level, language, english_option, status) to select candidates. Read only the matching files.
   - Run history: read the latest sections of `context/sync-log.md` to know when each source was last checked and what it showed.
   - Interview questions: read `context/interview-prep/` plus the requirements in the relevant vacancy file.
   - If `context/vacancies/` is empty and `sync-log.md` is missing, say the harness hasn't been synced yet and suggest `kb-sync`.
2. **Check freshness.** Compare each `fetched` date with today's date. Older than 7 days: add "may be closed, check the link". Treat `status: closed` listings as not available (mention them only if asked).
3. **Answer.** Match the question:
   - *"What vacancies are available?"*: list open listings as title, company, town, level, language/English option, fetched date. Then add the sync-log facts about companies with no junior roles, e.g. "Fellowmind: no junior roles when last checked (2026-11-12)". If nothing is open, say so plainly.
   - *"How do I contact them?"*: give the contact and apply URL exactly as saved. If none is saved: "no contact found", and give the `apply_url` or `source_url` if there is one.
   - *"What should I prepare?"*: combine the listing's stated requirements with `interview-prep/` notes. Keep it to what those files support.
4. **Cite** every fact as `(context/vacancies/<file>.md, fetched YYYY-MM-DD)` or `(context/interview-prep/<file>.md)`.
5. **Don't know.** If the files don't answer it, reply "I don't know" and say what would fix it: run `kb-sync`, drop the listing in `context/inbox/`, or add notes to `interview-prep/`. Don't guess, and don't fill gaps from general knowledge.

## Style
English, short, plain. Keep Dutch titles and quotes in Dutch with a brief English gloss. Lead with the answer, then the citations.
