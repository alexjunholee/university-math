#!/usr/bin/env python3
"""Split index.html into shared templates + chapter files."""

import re
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "index.html"
SHARED = ROOT / "shared"
CHAPTERS = ROOT / "chapters"

SHARED.mkdir(exist_ok=True)
CHAPTERS.mkdir(exist_ok=True)

# Clean previous output
for f in CHAPTERS.glob("*.html"):
    f.unlink()

lines = SRC.read_text(encoding="utf-8").splitlines(keepends=True)

# --- Find key boundaries ---
main_start = None
main_end = None
for i, line in enumerate(lines):
    if '<main id="main-content">' in line:
        main_start = i
    if '</main>' in line:
        main_end = i

assert main_start is not None and main_end is not None

# --- shared/head.html: everything up to and including <main> ---
(SHARED / "head.html").write_text("".join(lines[:main_start + 1]), encoding="utf-8")

# --- shared/footer.html: </main> through end ---
(SHARED / "footer.html").write_text("".join(lines[main_end:]), encoding="utf-8")

# --- Content lines ---
content = lines[main_start + 1 : main_end]

# Define chapter boundaries by scanning for:
#   1. <h2 id="...">  — standard chapter
#   2. <h2 class="part-title">  — part header (merge with next content)
#   3. <section id="..."> — chapters in Part VII-XI

# We'll build a list of (line_index, type, id_or_name) markers
markers = []
for i, line in enumerate(content):
    # Standard chapter h2
    m = re.search(r'<h2\s+id="([^"]+)"', line)
    if m:
        markers.append((i, "chapter", m.group(1)))
        continue
    # Part title h2
    m = re.search(r'<h2\s+class="part-title"', line)
    if m:
        markers.append((i, "part-title", line))
        continue
    # Section-based chapters (Part VII-XI)
    m = re.search(r'<section\s+id="([^"]+)"', line)
    if m:
        markers.append((i, "section", m.group(1)))
        continue

# Build chunks: each chunk is (name, start_line, end_line)
# First chunk: "about" section (before first marker)
chunks = []
if markers:
    if markers[0][0] > 0:
        chunks.append(("about", 0, markers[0][0]))

for idx, (line_idx, mtype, mid) in enumerate(markers):
    # End is next marker's start, or end of content
    end = markers[idx + 1][0] if idx + 1 < len(markers) else len(content)

    if mtype == "chapter":
        chunks.append((mid, line_idx, end))
    elif mtype == "part-title":
        # Part intros: merge into the next chunk by NOT creating a separate chunk.
        # The lines will be captured as part of the next chunk since we skip this.
        # But we need to extend the next chunk's start to include the part intro.
        # Strategy: just let the next marker's chunk start from this line_idx
        if idx + 1 < len(markers):
            # Modify next marker to start from this part-title's line
            # We'll handle this by storing part-title start and using it
            chunks.append(("__part_intro__", line_idx, end))
        else:
            chunks.append(("part-trailing", line_idx, end))
    elif mtype == "section":
        chunks.append((mid, line_idx, end))

# Now merge: __part_intro__ chunks get prepended to the NEXT chunk
merged = []
for i, (name, start, end) in enumerate(chunks):
    if name == "__part_intro__":
        # Find the next non-part-intro chunk and prepend
        if i + 1 < len(chunks):
            next_name, next_start, next_end = chunks[i + 1]
            chunks[i + 1] = (next_name, start, next_end)  # extend next chunk
        else:
            merged.append(("part-trailing", start, end))
    else:
        merged.append((name, start, end))

# Map names to numbered filenames
chapter_order = [
    "about",
    "sets-logic",
    "number-systems",
    "single-var-calc",
    "multivariable-calc",
    "ode",
    "pde",
    "linear-algebra",
    # 8-12 missing in content
    "group-theory",
    "ring-field-theory",
    "graduate-algebra",
    "homological-algebra",
    "elementary-number-theory",
    "algebraic-number-theory",
    "topology",
    "differential-geometry",
    "algebraic-geometry",
    "algebraic-topology",
    "probability",
    "statistics",
    "stochastic-processes",
    "convex-optimization",
    "linear-programming",
    "numerical-analysis",
    "computational-methods",
    "dynamical-systems",
    "discrete-math",
    "math-history",
]

name_to_num = {}
for i, name in enumerate(chapter_order):
    if name == "about":
        name_to_num[name] = "00"
    else:
        # Use the chapter number from the content if available, else sequential
        name_to_num[name] = str(i).zfill(2)

# Better: extract chapter number from content
ch_num_from_content = {
    "about": "00",
    "sets-logic": "01",
    "number-systems": "02",
    "single-var-calc": "03",
    "multivariable-calc": "04",
    "ode": "05",
    "pde": "06",
    "linear-algebra": "07",
    "real-analysis": "08",
    "complex-analysis": "09",
    "functional-analysis": "10",
    "measure-theory": "11",
    "fourier-analysis": "12",
    "group-theory": "13",
    "ring-field-theory": "14",
    "graduate-algebra": "15",
    "homological-algebra": "16",
    "elementary-number-theory": "17",
    "algebraic-number-theory": "18",
    "topology": "19",
    "differential-geometry": "20",
    "algebraic-geometry": "21",
    "algebraic-topology": "22",
    "probability": "23",
    "statistics": "24",
    "stochastic-processes": "25",
    "convex-optimization": "26",
    "linear-programming": "27",
    "numerical-analysis": "28",
    "computational-methods": "29",
    "dynamical-systems": "30",
    "discrete-math": "31",
    "math-history": "32",
}

# Write chapter files
manifest = []
for name, start, end in merged:
    num = ch_num_from_content.get(name, "XX")
    filename = f"{num}-{name}.html"
    chunk_lines = content[start:end]
    (CHAPTERS / filename).write_text("".join(chunk_lines), encoding="utf-8")
    manifest.append(filename)
    print(f"  {filename} ({len(chunk_lines)} lines)")

# Write manifest (build order)
(CHAPTERS / "manifest.txt").write_text("\n".join(manifest) + "\n", encoding="utf-8")

print(f"\nTotal: {len(manifest)} chapter files")
print(f"Shared: head.html, footer.html")
print(f"Manifest: chapters/manifest.txt")
