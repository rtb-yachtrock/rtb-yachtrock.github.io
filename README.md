# Relova Thomas Yacht Rock Band Website

Source code and assets for the RTB Yacht Rock band website, hosted via GitHub Pages.

## File & Folder Structure

* **`index.html`** — The main landing page, featuring a dynamic "Next Up" show callout card.
* **`gigs.html`** — The dedicated live gigs page, featuring the headline upcoming show, a list of later shows, and an archive of past performances.
* **`gigs.json`** — **The source of truth for all live shows.** Add, update, or remove dates and venues here.
* **`build.py`** — Python script that reads `gigs.json`, sorts upcoming/past dates chronologically, and automatically updates `index.html` and `gigs.html`.
* **`.github/workflows/build-gigs.yml`** — GitHub Actions automation workflow that automatically runs `build.py` and commits updated HTML files whenever `gigs.json` is modified.
* **`bios/`** — Folder containing individual `.txt` files for band member biographies and background info.
* **`images/`** — Folder containing site graphics, promotional band photos, logos, and venue assets.
