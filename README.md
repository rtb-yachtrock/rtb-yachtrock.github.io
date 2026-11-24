# Relova Thomas Yacht Rock Band Website

Source code and assets for the Relova Thomas Yacht Rock Band (RTB) website, hosted via GitHub Pages.

https://rtb-yachtrock.github.io/

## File & Folder Structure

- **`index.html`** — The main landing page, featuring a dynamic "Next Up" show callout card.
- **`gigs.html`** — **Automatically generated.** Dedicated live gigs page, featuring the headline upcoming show, a list of later shows, and an archive of past performances. *(Do not edit directly; see Gigs Automation below.)*
- **`gigs.json`** — **The source of truth for all live shows.** Add, update, or remove dates and venues here.
- **`build.py`** — Python script that reads `gigs.json`, sorts upcoming/past dates chronologically, and automatically updates `index.html` and `gigs.html`.
- **`.github/workflows/build-gigs.yml`** — GitHub Actions automation workflow that automatically runs `build.py` and commits updated HTML files whenever `gigs.json` is modified.
- **`bio.html`** — Page containing band and member bios. Update via the `.txt` files in the `bios/` folder.
- **`bios/`** — Folder containing individual `.txt` files for band member biographies and background info.
- **`media.html`** — Page containing pix, video, and other media assets. Store all media in the `images/` folder.
- **`images/`** — Folder containing site graphics, promotional band photos, logos, and venue assets.

## Gigs Automation

`gigs.html` (and any related gig listings on the site) is **automatically generated** by the Python build script (`build.py`) using structured data from `gigs.json`. 

* **Do not edit `gigs.html` directly.** 
* To add, remove, or modify upcoming shows, update `gigs.json` and run the build script (or let the automated GitHub Action workflow handle it upon commit).

## Updating Gigs & Rebuilding Pages

`index.html` and `gigs.html` are generated from `gigs.json` using `build.py`.

### Adding or editing a gig
1. Edit `gigs.json` on GitHub (`main` branch) and commit the changes.
2. The **Build Gigs Website** workflow automatically runs `build.py` and commits updated `index.html` and `gigs.html` files.
3. GitHub Pages then publishes the updated site.

### Clearing past gigs manually (when `gigs.json` wasn't edited)
1. Open the **Actions** tab in the repository.
2. Select **Build Gigs Website** on the left.
3. Click **Run workflow** (select the `main` branch if prompted) and confirm **Run workflow**.
4. Wait for the run to finish with a green checkmark so `index.html` and `gigs.html` update.

## Note on Media
- **Pictures:** Keep compressed under 200 KB for fast mobile load times.
- **Videos:** Link or embed via YouTube rather than hosting large video files directly on the server.

## Mailing List & Form Setup
- **Provider:** Web3Forms (`https://api.web3forms.com/submit`)
- **Recipient Email:** `rtb.yachtrock@gmail.com`
- **Access Key:** `2e67b624-3fef-4465-a84c-011264d581db` (embedded in `contact.html` via `<input type="hidden" name="access_key" value="2e67b624-3fef-4465-a84c-011264d581db">`)
- **Subject Line:** `New Subscriber`
- **Spam Protection:** Includes hidden `botcheck` input field.
