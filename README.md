# Relova Thomas Yacht Rock Band Website

Source code and assets for the Relova Thomas Yacht Rock Band (RTB) website, hosted via GitHub Pages.

https://rtb-yachtrock.github.io/

## File & Folder Structure

* **`index.html`** — The main landing page, featuring a dynamic "Next Up" show callout card.
* **`gigs.html`** — The dedicated live gigs page, featuring the headline upcoming show, a list of later shows, and an archive of past performances.
* **`gigs.json`** — **The source of truth for all live shows.** Add, update, or remove dates and venues here.
* **`build.py`** — Python script that reads `gigs.json`, sorts upcoming/past dates chronologically, and automatically updates `index.html` and `gigs.html`.
* **`.github/workflows/build-gigs.yml`** — GitHub Actions automation workflow that automatically runs `build.py` and commits updated HTML files whenever `gigs.json` is modified.
* **`bio.html`** — Page containing band and member bios. Update via the `.txt` files in the `bios/` folder.
* **`bios/`** — Folder containing individual `.txt` files for band member biographies and background info.
* **`media.html`** — Page containing pix, video, and other media assets. Store all media in the `images/` folder.
* **`images/`** — Folder containing site graphics, promotional band photos, logos, and venue assets.
