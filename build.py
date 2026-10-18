import json
from datetime import datetime

# Load the gigs data
with open("gigs.json", "r") as f:
    gigs = json.load(f)

# Get today's date for comparison
today = datetime.now().strftime("%Y-%m-%d")

# Separate and sort gigs
# Upcoming: closest date first (ascending order)
upcoming = sorted(
    [g for g in gigs if g["date"] >= today], key=lambda x: x["date"]
)
# Past: most recent past show first (descending order)
past = sorted([g for g in gigs if g["date"] < today], key=lambda x: x["date"], reverse=True)

print(f"Found {len(upcoming)} upcoming show(s) and {len(past)} past show(s).")

# 1. GENERATE HOMEPAGE ("Next Up" banner snippet)
if upcoming:
    next_gig = upcoming[0]
    # Format time display
    time_display = (
        f" @ {next_gig['time']}"
        if next_gig["time"] and next_gig["time"] != "TBD"
        else (f" @ {next_gig['time']}" if next_gig["time"] == "TBD" else "")
    )
    # You can output this HTML or have the script directly overwrite a placeholder in index.html
