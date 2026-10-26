# -*- coding: utf-8 -*-
"""Tennessee Board of Regents (College System of Tennessee) win, Oct 2026.
Facts come from EnlitEDU's client slides: 11 TBR community colleges + 7 institutions in 6 other states.
TBR has 13 community colleges in total, so never write "all" or "the entire system"."""

# ---- switch between the two homepage options the client is choosing from
TBR_PROMO = {
    "section": True,      # Option B: highlight section on the homepage (right after the logo strip)
    "popup_auto": False,  # Option A: announcement popup opens by itself on the homepage (once per visitor / 30 days)
}                         # Preview the popup any time with index.html?tbr-popup

TBR = dict(name="Tennessee Board of Regents", system="College System of Tennessee", short="TBR",
           url="https://www.tbr.edu/", logo="tbr-college-system-of-tennessee.png")

NEWS_PATH = "news/tennessee-board-of-regents-selects-lioraai.html"
NEWS_DATE = "2026-10-26"   # change to the official announcement date if it differs

# name, city, logo file, official website (all checked Oct 2026)
TBR_COLLEGES = [
    ("Chattanooga State Community College", "Chattanooga", "chattanooga-state-community-college.png", "https://www.chattanoogastate.edu/"),
    ("Cleveland State Community College", "Cleveland", "cleveland-state-community-college.png", "https://www.clevelandstatecc.edu/"),
    ("Columbia State Community College", "Columbia", "columbia-state-community-college.png", "https://www.columbiastate.edu/"),
    ("Jackson State Community College", "Jackson", "jackson-state-community-college.png", "https://www.jscc.edu/"),
    ("Motlow State Community College", "Tullahoma", "motlow-state-community-college.png", "https://www.mscc.edu/"),
    ("Nashville State Community College", "Nashville", "nashville-state-community-college.png", "https://www.nscc.edu/"),
    ("Northeast State Community College", "Blountville", "northeast-state-community-college.png", "https://www.northeaststate.edu/"),
    ("Pellissippi State Community College", "Knoxville", "pellissippi-state-community-college.png", "https://www.pstcc.edu/"),
    ("Roane State Community College", "Harriman", "roane-state-community-college.png", "https://www.roanestate.edu/"),
    ("Southwest Tennessee Community College", "Memphis", "southwest-tennessee-community-college.png", "https://www.southwest.tn.edu/"),
    ("Volunteer State Community College", "Gallatin", "volunteer-state-community-college.png", "https://www.volstate.edu/"),
]

# institutions outside Tennessee (client slide "Trusted Across Higher Education": 6 states)
NATIONWIDE = [
    ("Alabama A&M University", "alabama-a-m-university.png", "HBCU, Alabama"),
    ("Miles College", "miles-college.png", "HBCU, Alabama"),
    ("WSU Tech", "wsu-tech.png", "Technical college, Kansas"),
    ("Villanova University", "villanova-university.png", "University, Pennsylvania"),
    ("Johnston Community College", "johnston-community-college.png", "Community college, North Carolina"),
    ("Vincennes University", "vincennes-university.png", "University, Indiana"),
    ("Minnesota State University, Mankato", "minnesota-state-university-mankato.png", "Research university, Minnesota"),
]
NATIONWIDE_STATES = "Alabama, Kansas, Pennsylvania, North Carolina, Indiana and Minnesota"
