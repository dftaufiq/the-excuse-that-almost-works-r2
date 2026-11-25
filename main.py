"""Write the excuse line to /output/entry.txt for make.fun's
"The Excuse That Almost Works" bounty (round 2 resubmit).

The R1 line (boiler burst) finished #910 of 1987, below the interim cut
of 500, so its score is frozen and it is dead. This R2 line is a
DIFFERENT angle, chosen by a full pairwise round-robin of 22 candidates
against the judge's brief (see variants-r2.md in the build folder):
undefeated 21-0, beats the runner-up by margin 2 and the R1 line by
margin 3. Structure is 2-beat + reveal in the final clause: beat one,
the fire brigade tapes off the street at 5am for a gas leak two doors
down; beat two, the reveal that the sender is standing on the pavement
in their pyjamas. No GTA mention, no illness, no dead grandmother, no
flat tyre, no water/plumber. Deterministic: the same bytes on every run.
"""

import os

LINE = "Fire brigade taped off our street at 5am, gas leak two doors down, I'm on the pavement in my pyjamas."

# The sealed gate (RULES.txt): /output/entry.txt must be UTF-8 text of
# 1-140 characters, not only whitespace, one line; the brief caps the line
# at 20 words. Refuse to write anything that breaks either limit.
# Tie-break note: on an exact Judge win-rate tie the smaller text wins,
# so the line is kept at 101 bytes — short is an asset, and "a long
# excuse sounds rehearsed" per the judge brief.
MAX_CHARS = 140
MAX_WORDS = 20
WORDS = LINE.split()
if not 1 <= len(LINE) <= MAX_CHARS or not LINE.strip() or "\n" in LINE:
    raise SystemExit("entry line violates the 1-140 char single-line gate")
if len(WORDS) > MAX_WORDS:
    raise SystemExit("entry line is over the 20-word cap")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
