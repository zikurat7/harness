# Inbox

Drop vacancies here that the harness can't fetch by itself (LinkedIn, Indeed, anything else).

## How
Create a text or Markdown file for each vacancy. Any of these work:
- **A link only**: a file containing just the URL. `kb-sync` will try to read it; if the site blocks it, it will ask you to paste the text instead.
- **Pasted text**: the full listing copied from the site, plus the URL on the first line.
- **A screenshot or PDF**: saved in this folder.

Name files however you like, e.g. `linkedin-robotica-zwolle.md`.

## What happens next
Run `kb-sync`. It turns each inbox item into a vacancy file in `context/vacancies/` with the standard fields and today's date as `fetched`, then moves the original into `context/inbox/done/`.
