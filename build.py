from datetime import datetime
import json
import re

# 1. Load gigs data
with open("gigs.json", "r", encoding="utf-8") as f:
  gigs = json.load(f)

# Get today's date (October 18, 2026) for comparison
today = datetime.now().strftime("%Y-%m-%d")

# 2. Sort and filter
# Upcoming: closest date first (ascending)
upcoming = sorted(
    [g for g in gigs if g["date"] >= today], key=lambda x: x["date"]
)
# Past: most recent first (descending)
past = sorted(
    [g for g in gigs if g["date"] < today], key=lambda x: x["date"], reverse=True
)

print(f"Found {len(upcoming)} upcoming show(s) and {len(past)} past show(s).")


# Helper formatting function for times
def format_time(time_str):
  if not time_str:
    return ""
  if time_str.upper() == "TBD":
    return " @ TBD"
  return f" @ {time_str}"


# --- 3. BUILD INDEX.HTML SNIPPET ---
index_next_up_html = ""
if upcoming:
  next_gig = upcoming[0]
  time_disp = format_time(next_gig["time"])
  details_p = (
      f'<p style="font-style: italic; margin: 0 0 15px 0; color: rgba(255, 255, 255, 0.9);">'
      f"{next_gig['details']}</p>"
      if next_gig["details"]
      else ""
  )
  venue_display = (
      f'<a href="{next_gig["venueUrl"]}" target="_blank" style="color: #ffffff; text-decoration: underline; font-weight: bold;">'
      f'{next_gig["venue"]}</a>'
      if next_gig["venueUrl"]
      else f'<strong style="color: #ffffff;">{next_gig["venue"]}</strong>'
  )

  index_next_up_html = f"""<!-- NEXT_UP_START -->
        <div style="background-color: rgba(255, 255, 255, 0.1); padding: 25px; border-radius: 12px; margin-bottom: 30px; border: 1px solid rgba(255, 255, 255, 0.3); text-align: left;">
            <div style="color: #fef08a; font-weight: bold; font-size: 13px; text-transform: uppercase; margin-bottom: 8px; letter-spacing: 0.5px;">Next Up</div>
            <div style="font-size: 18px; color: #fef08a; font-weight: bold; margin-bottom: 6px;">{next_gig['venue']}</div>
            <div style="font-size: 15px; color: rgba(255, 255, 255, 0.9); margin-bottom: 15px;">{next_gig['displayDate']}{time_disp}</div>
            <a href="gigs.html" style="background-color: #ffffff; color: #0284c7; padding: 8px 18px; text-decoration: none; font-size: 14px; font-weight: bold; border-radius: 20px; display: inline-block;">
                View All Gigs & Details →
            </a>
        </div>
        <!-- NEXT_UP_END -->"""

with open("index.html", "r", encoding="utf-8") as f:
  index_content = f.read()

index_content = re.sub(
    r"<!-- NEXT_UP_START -->.*?<!-- NEXT_UP_END -->",
    index_next_up_html,
    index_content,
    flags=re.DOTALL,
)

with open("index.html", "w", encoding="utf-8") as f:
  f.write(index_content)


# --- 4. BUILD GIGS.HTML SNIPPET ---
gigs_section_html = "<!-- GIGS_CONTENT_START -->\n"

# Render all upcoming shows
for gig in upcoming:
  time_disp = format_time(gig["time"])
  venue_display = (
      f'<a href="{gig["venueUrl"]}" target="_blank" style="color: #ffffff; text-decoration: underline; font-weight: bold;">'
      f"{gig['venue']}</a>"
      if gig["venueUrl"]
      else f'<strong style="color: #ffffff;">{gig["venue"]}</strong>'
  )
  details_p = (
      f'<p style="font-style: italic; margin: 0 0 15px 0; color: rgba(255, 255, 255, 0.9);">'
      f"{gig['details']}</p>"
      if gig["details"]
      else ""
  )

  gigs_section_html += f"""        <!-- Upcoming Show Card -->
        <div style="background-color: rgba(255, 255, 255, 0.1); padding: 25px; border-radius: 12px; margin-bottom: 30px; border: 1px solid rgba(255, 255, 255, 0.3);">
            <div style="color: #fef08a; font-weight: bold; text-transform: uppercase; font-size: 14px; margin-bottom: 8px;">Next Up</div>
            <div style="font-size: 18px; font-weight: bold; margin-bottom: 8px;">{gig['displayDate']}{time_disp}</div>
            <div style="font-size: 18px; margin-bottom: 12px;">
                {venue_display} — {gig['location']}
            </div>
            {details_p}
            <a href="https://maps.google.com/?q={gig['mapQuery']}" target="_blank" style="background-color: #ffffff; color: #0284c7; padding: 8px 16px; text-decoration: none; font-size: 14px; font-weight: bold; border-radius: 20px; display: inline-block;">
                📍 Map & Directions
            </a>
        </div>\n"""

# Render past shows list
gigs_section_html += """        <!-- Past Gigs List -->
        <h3 style="text-align: center; margin-top: 40px; margin-bottom: 20px; font-size: 18px; color: #fef08a; font-weight: bold; ">Past Shows</h3>
        <ul style="list-style: none; padding: 0; line-height: 2.0; color: rgba(255, 255, 255, 0.8); text-align: center;">\n"""

for gig in past:
  gigs_section_html += (
      f"            <li>{gig['displayDate']} — {gig['venue']}, "
      f"{gig['location']}</li>\n"
  )

gigs_section_html += """        </ul>
        <!-- GIGS_CONTENT_END -->"""

with open("gigs.html", "r", encoding="utf-8") as f:
  gigs_content = f.read()

gigs_content = re.sub(
    r"<!-- GIGS_CONTENT_START -->.*?<!-- GIGS_CONTENT_END -->",
    gigs_section_html,
    gigs_content,
    flags=re.DOTALL,
)

with open("gigs.html", "w", encoding="utf-8") as f:
  f.write(gigs_content)

print("Build complete successfully!")
