#!/usr/bin/env python3
"""Add YouTube video resource blocks to chapter files.

Sources ONLY from: Developer-Y/math-science-video-lectures README
and the About section's listed sources (MIT OCW, Stanford SEE, NPTEL, etc.)
No externally searched content.
"""

from pathlib import Path

CHAPTERS = Path(__file__).parent / "chapters"

# ===================================================================
# All entries below are from Developer-Y/math-science-video-lectures
# and the document's own About section source list.
# ===================================================================

VIDEOS = {
    "01-sets-logic.html": [
        ("Mathematical Logic — NPTEL IIT Madras", "http://nptel.ac.in/courses/111106052/"),
        ("Foundations of Pure Mathematics — U. of Nottingham", "https://www.youtube.com/playlist?list=PLpRE0Zu_k-BzsKBqQ-HEqD6WVLIHSNuXa"),
        ("Sets, Counting, and Probability — Harvard", "https://www.youtube.com/playlist?list=PLelIK3uylPMFx0ChiZsKts8cs46wu9CJb"),
    ],
    "02-number-systems.html": [
        ("Math Foundations A (1-79) — N.J. Wildberger (UNSW)", "https://www.youtube.com/playlist?list=PL5A714C94D40392AB"),
        ("Math Foundations B (80-149) — N.J. Wildberger (UNSW)", "https://www.youtube.com/playlist?list=PLIljB45xT85DpiADQOPth56AVC48SrPLc"),
    ],
    "03-single-var-calc.html": [
        ("18.01 Single Variable Calculus — MIT OCW", "https://ocw.mit.edu/courses/mathematics/18-01-single-variable-calculus-fall-2006/"),
        ("Calculus Revisited: Single Variable Calculus — MIT OCW", "https://ocw.mit.edu/resources/res-18-006-calculus-revisited-single-variable-calculus-fall-2010/"),
        ("Highlights of Calculus — Gilbert Strang, MIT OCW", "https://www.youtube.com/playlist?list=PLBE9407EA64E2C318"),
        ("Mathematics 16A Analytic Geometry and Calculus — UC Berkeley", "https://www.youtube.com/view_play_list?p=B7EDD5D491072A6E"),
        ("Mathematics 1A Calculus — UC Berkeley (Paulin, Fall 2019)", "https://math.berkeley.edu/~apaulin/1A_001%20(Fall%202019).html"),
        ("MAT 137 Calculus with Proofs — U. of Toronto", "https://www.math.utoronto.ca/alfonso/137/137.html?videos"),
        ("Calculus III: Multivariable Calculus — Princeton", "https://www.youtube.com/playlist?list=PLGqzsq0erqU7h6_bpE-CgJp4iX5aRju28"),
        ("Calculus — U. of Houston", "https://online.math.uh.edu/HoustonACT/videocalculus/"),
        ("MA 141 Calculus I — NCSU", "https://www.math.ncsu.edu/calculus/web/MA141lectures.html"),
        ("MA 241 Calculus II — NCSU", "https://www.math.ncsu.edu/calculus/web/MA241lectures.html"),
    ],
    "04-multivariable-calc.html": [
        ("18.02 Multivariable Calculus — MIT OCW", "https://ocw.mit.edu/courses/mathematics/18-02-multivariable-calculus-fall-2007/"),
        ("Calculus Revisited: Multivariable Calculus — MIT OCW", "https://ocw.mit.edu/resources/res-18-007-calculus-revisited-multivariable-calculus-fall-2011/"),
        ("Mathematics 53 Multivariable Calculus — UC Berkeley", "https://math.berkeley.edu/~pkoroteev/math53.html"),
        ("Math 241 Calculus III — U. of Maryland", "https://www.youtube.com/playlist?list=PL7RK4EsMAcJKgJXRKXKObYFH_JdWTubU-"),
        ("MA 242 Calculus III — NCSU", "https://courses.ncsu.edu/ma242/common/media/OutlineOfLectures.html"),
        ("Vector Calculus — UNSW (Chris Tisdell)", "https://www.youtube.com/course?list=EC283CA2107AD503A3"),
        ("Vector Calculus and PDE (Math 3140) — U. of Utah", "https://www.youtube.com/playlist?list=PLkfmuPOLLnthHE9ICNdGgdgIi16-M80ZS"),
    ],
    "05-ode.html": [
        ("18.03 Differential Equations — MIT OCW", "https://ocw.mit.edu/courses/mathematics/18-03-differential-equations-spring-2010/"),
        ("Calculus Revisited: Complex Variables, Diff Eq, and Linear Algebra — MIT OCW", "https://ocw.mit.edu/resources/res-18-008-calculus-revisited-complex-variables-differential-equations-and-linear-algebra-fall-2011/"),
        ("Math 246 Differential Equations for Engineers — U. of Maryland", "https://www.youtube.com/playlist?list=PL7RK4EsMAcJKgJXRKXKObYFH_JdWTubU-"),
        ("MA 341 Applied Differential Equations I — NCSU", "https://www.math.ncsu.edu/mmc/ma341lectures.php"),
        ("Differential Equations and Linear Algebra (Math 2250) — U. of Utah", "https://www.youtube.com/playlist?list=PLkfmuPOLLntiLBCHDCHWFtLaz-P94Iwe3"),
        ("12-267 Advanced ODE — U. of Toronto", "http://drorbn.net/index.php?title=12-267"),
        ("ODE and Applications — NPTEL IISC Bangalore", "http://nptel.ac.in/courses/111108081/"),
    ],
    "06-pde.html": [
        ("PDE for Engineers: Separation of Variables — NPTEL IIT Kharagpur", "http://nptel.ac.in/courses/111105093/"),
        ("Partial Differential Equations (Math 3150) — U. of Utah", "https://www.youtube.com/playlist?list=PLkfmuPOLLntjZFL7lH75U4jQeUJznduqL"),
        ("Numerical Methods of ODE and PDE — NPTEL IIT Kharagpur", "http://nptel.ac.in/courses/111105038/"),
    ],
    "07-linear-algebra.html": [
        ("18.06SC Linear Algebra — MIT OCW (Gilbert Strang)", "https://ocw.mit.edu/courses/mathematics/18-06sc-linear-algebra-fall-2011/"),
        ("Linear Algebra — Princeton", "https://www.youtube.com/playlist?list=PLGqzsq0erqU7w7ZrTZ-pWWk4-AOkiGEGp"),
        ("A First Course in Linear Algebra — N.J. Wildberger (UNSW)", "https://www.youtube.com/course?list=EC44B6B54CBF6A72DF"),
        ("MATH 461 Linear Algebra for Scientists and Engineers — U. of Maryland", "https://www.youtube.com/playlist?list=PL7RK4EsMAcJJ5XWkPJi-CyY_ABx_gIKR9"),
        ("MATH 401 Applications of Linear Algebra — U. of Maryland", "https://www.youtube.com/playlist?list=PL7RK4EsMAcJLL-sTuDoIetoxYnyqCDWmG"),
        ("Linear Algebra In-Depth Introduction (Parts 1-3)", "https://www.youtube.com/playlist?list=PLlXfTHzgMRUKXD88IdzS14F4NxAZudSmv"),
        ("Math 312 Linear Algebra — UPenn", "https://www.youtube.com/playlist?list=PLS3WLIIQXmMJ2bO_YS1r0UFW2XRRGqUUL"),
        ("Advanced Matrix Theory and Linear Algebra — NPTEL IISC Bangalore", "http://nptel.ac.in/courses/111108066/"),
        ("Linear Algebra — NPTEL IIT Madras", "http://nptel.ac.in/courses/111106051/"),
        ("EE263 Intro to Linear Dynamical Systems — Stanford", "https://see.stanford.edu/Course/EE263"),
    ],
    "08-real-analysis.html": [
        ("18.100A Real Analysis — MIT", "https://www.youtube.com/playlist?list=PLUl4u3cNGP61O7HkcF7UImpM0cR_L2gSw"),
        ("18.100B Real Analysis — MIT", "https://www.youtube.com/playlist?list=PLUl4u3cNGP62Ie7F_tTAhhXoX5_Cl8meG"),
        ("Real Analysis — Harvey Mudd College", "https://www.youtube.com/playlist?list=PL04BA7A9EB907EDAF"),
        ("Introduction to Real Analysis — METU Math349 (Ozan)", "https://www.youtube.com/playlist?list=PLBMmiR8tC9Um6w4pWfUq-hjgdQ24yzv0X"),
        ("A Basic Course in Real Analysis — NPTEL IIT Kharagpur", "http://nptel.ac.in/courses/111105069/"),
        ("Real Analysis — NPTEL IIT Madras", "http://nptel.ac.in/courses/111106053/"),
        ("Mathematical Analysis — U. of Nottingham", "https://www.youtube.com/playlist?list=PL58984C080F2B0575"),
        ("UC Berkeley Math 104 Real Analysis (Fall 2021)", "https://www.youtube.com/@RealAnalysisSummer-MaxWimberle/playlists"),
    ],
    "09-complex-analysis.html": [
        ("MATH 463 Complex Variables — U. of Maryland", "https://www.youtube.com/playlist?list=PL7RK4EsMAcJI8S01bmUC1ef53KbTA0FSf"),
        ("Applied Complex Variables (Math 3160) — U. of Utah", "https://www.youtube.com/playlist?list=PLkfmuPOLLntiM_HjG-FSUTyINMfgVszca"),
        ("Advanced Complex Analysis Part 1 — NPTEL IIT Madras", "http://nptel.ac.in/courses/111106084/"),
        ("Advanced Complex Analysis Part 2 — NPTEL IIT Madras", "http://nptel.ac.in/courses/111106094/"),
        ("Complex 1-Tori and Elliptic Curves — NPTEL IIT Madras", "http://nptel.ac.in/courses/111106044/"),
    ],
    "10-functional-analysis.html": [
        ("18.102 Introduction to Functional Analysis — MIT", "https://www.youtube.com/playlist?list=PLUl4u3cNGP63micsJp_--fRAjZXPrQzW_"),
        ("Functional Analysis — NPTEL IIT Kharagpur", "http://nptel.ac.in/courses/111105037/"),
        ("Functional Analysis — U. of Nottingham", "https://www.youtube.com/playlist?list=PL554B877A872B4F94"),
    ],
    "11-measure-theory.html": [
        ("Measure and Integration — NPTEL IIT Bombay", "http://nptel.ac.in/courses/111101005/"),
    ],
    "12-fourier-analysis.html": [
        ("EE261 The Fourier Transform and its Applications — Stanford", "https://see.stanford.edu/Course/EE261"),
        ("Math 139 Fourier Analysis — Winston Ou", "https://www.youtube.com/playlist?list=PLun8-Z_lTkC5KUsw0dO2SBkdwdEVKqcP5"),
        ("18.103 Fourier Analysis: Theory and Applications — MIT", "https://www.youtube.com/playlist?list=PLIygTcviGPKBMyjct4h5QLNBWxIeglSMA"),
    ],
    "13-group-theory.html": [
        ("Abstract Algebra — Harvard", "https://www.youtube.com/playlist?list=PLelIK3uylPMGzHBuR3hLMHrYfMqWWsmx5"),
        ("Group Theory — LadislauFernandes", "https://www.youtube.com/playlist?list=PLWbnIo7XnOkw7zZu6u3si3at21r534qIM"),
        ("Group Theory — Ben Garside", "https://www.youtube.com/playlist?list=PLAvgI3H-gclb_Xy7eTIXkkKt3KlV6gk9_"),
        ("Math 371 Algebra II (2014) — UPenn", "https://www.youtube.com/playlist?list=PLS3WLIIQXmMIM2UqSvLGnE-sbUPkDF4Bu"),
    ],
    "14-ring-field-theory.html": [
        ("Abstract Algebra — Harvard", "https://www.youtube.com/playlist?list=PLelIK3uylPMGzHBuR3hLMHrYfMqWWsmx5"),
        ("Math 371 Algebra II (2011) — UPenn", "https://www.youtube.com/playlist?list=PLS3WLIIQXmML4mJgnP9q6EaL8sBTg7I3p"),
        ("Math 371 Algebra II (2014) — UPenn", "https://www.youtube.com/playlist?list=PLS3WLIIQXmMIM2UqSvLGnE-sbUPkDF4Bu"),
    ],
    "15-graduate-algebra.html": [
        ("Math 602 Graduate Algebra 1 (2011) — UPenn", "https://www.youtube.com/playlist?list=PLS3WLIIQXmMIbqujCLRMYL4Dqe46c_dss"),
        ("Math 602 Graduate Algebra 1 (2013) — UPenn", "https://www.youtube.com/playlist?list=PLS3WLIIQXmMITfZqYjSS5AJHIZM2lequR"),
        ("Math 603 Graduate Algebra 2 (2014) — UPenn", "https://www.youtube.com/playlist?list=PLS3WLIIQXmMKzNNgSSJqyJocKY7vIcD8o"),
        ("Lie Groups — Harvard", "https://www.youtube.com/playlist?list=PLelIK3uylPMG3iyQ_SJYqeyjmeNC2QC3L"),
    ],
    "16-homological-algebra.html": [
        ("Math 340 Homological Algebra — UPenn", "https://www.youtube.com/playlist?list=PLS3WLIIQXmMLvfY5NOfWRs55x_H4lRTpj"),
    ],
    "17-elementary-number-theory.html": [
        ("MATH 406 Number Theory — U. of Maryland", "https://www.youtube.com/playlist?list=PL7RK4EsMAcJLz8MjNqDUE5n6kOlxRRkb"),
        ("Math 350 Number Theory — UPenn (Chinburg)", "https://www.youtube.com/playlist?list=PLS3WLIIQXmMJ5Dd-vu_ST6ll3PH7Co2S8"),
        ("Number Theory of 2015 — James Cook, Liberty U.", "https://www.youtube.com/playlist?list=PLBY4G2o7DhF3dBX7vxpS6b119SyM3S7WJ"),
    ],
    "18-algebraic-number-theory.html": [
        ("Math 702 Algebraic Number Theory I — UPenn (Chinburg)", "https://www.youtube.com/playlist?list=PLS3WLIIQXmMJU2wh0WDLsyMh_evP8m7os"),
        ("Math 703 Algebraic Number Theory II — UPenn (Chinburg)", "https://www.youtube.com/playlist?list=PLS3WLIIQXmMLEvNfav1QVRhIKJcBslI7F"),
        ("Math 720 Advanced Number Theory — UPenn (Chinburg)", "https://www.math.upenn.edu/~ted/720F18/hw-720SchedTab.html"),
    ],
    "19-topology.html": [
        ("Topology & Geometry — Tadashi Tokieda", "https://www.youtube.com/playlist?list=PLTBqohhFNBE_09L0i-lf3fYXF5woAbrzJ"),
        ("Topology — ThoughtSpaceZero", "https://www.youtube.com/playlist?list=PLF94A6F65866F3F31"),
    ],
    "20-differential-geometry.html": [
        ("Geometry — METU Math373 (CEM TEZER)", "https://www.youtube.com/playlist?list=PLuiPz6iU5SQ828B8vmWXrjMDGXHGH3ci6"),
        ("Tensor Calculus and the Calculus of Moving Surfaces", "https://www.youtube.com/playlist?list=PLlXfTHzgMRULkodlIEqfgTS-H1AY_bNtq"),
        ("Curves and Surfaces — NPTEL IIT Kanpur", "http://nptel.ac.in/courses/111104095/"),
        ("MATH 430 Euclidean and Non-Euclidean Geometry — U. of Maryland", "https://www.youtube.com/playlist?list=PL7RK4EsMAcJJ5XWkPJi-CyY_ABx_gIKR9"),
    ],
    "21-algebraic-geometry.html": [
        ("Basic Algebraic Geometry: Varieties, Morphisms — NPTEL IIT Madras", "http://nptel.ac.in/courses/111106097/"),
        ("Lectures on Basic Algebraic Geometry — Miles Reid (WCU)", "http://www.mathnet.or.kr/new_VOD/sub1.php?key_s_title=Lectures+on+Basic+Algebraic+Geometry+by+Miles+Reid+%28WCU+project%29"),
        ("Lectures on Algebraic Surfaces — Miles Reid (WCU)", "http://vod.mathnet.or.kr/sub1.php?key_s_title=Lectures+on+Algebraic+Surfaces+by+Miles+Reid+%28WCU+project%29"),
        ("Arithmetic Geometry — Clay Mathematics Institute 2006", "http://www.uni-math.gwdg.de/aufzeichnungen/SummerSchool/"),
    ],
    "22-algebraic-topology.html": [
        ("Algebraic Topology — METU Math537 (Ozan, Fall 2020)", "https://www.youtube.com/playlist?list=PLBMmiR8tC9UnLcRhGimiNs1CVvS6tm52s"),
        ("Algebraic Topology: a beginner's course — N.J. Wildberger (UNSW)", "https://www.youtube.com/playlist?list=PL6763F57A61FE6FE8"),
        ("Algebraic Knot Theory — U. of Toronto", "http://drorbn.net/index.php?title=AKT-09"),
    ],
    "23-probability.html": [
        ("6.041SC Probabilistic Systems Analysis — MIT OCW", "https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"),
        ("Statistics 110: Probability — Harvard", "https://www.youtube.com/course?list=EC2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo"),
        ("EE230 Probability and Random Variables — METU", "https://www.youtube.com/playlist?list=PLuiPz6iU5SQ8ra5kjxx770vk_famaeuvz"),
        ("Probability and Stochastics for Finance — NPTEL IIT Kanpur", "http://nptel.ac.in/courses/111104089/"),
        ("Probability Theory and Applications — NPTEL IIT Kanpur", "http://nptel.ac.in/courses/111104079/"),
    ],
    "24-statistics.html": [
        ("Probability and Statistics — NPTEL IIT Kharagpur", "http://nptel.ac.in/courses/111105041/"),
        ("Applied Multivariate Statistical Modeling — NPTEL IIT Kharagpur", "http://nptel.ac.in/courses/111105091/"),
        ("Applied Multivariate Analysis — NPTEL IIT Kanpur", "http://nptel.ac.in/courses/111104024/"),
        ("Statistical Inference — NPTEL IIT Kharagpur", "http://nptel.ac.in/courses/111105043/"),
        ("Prob & Statistics with Prof Spiegelhalter", "https://www.youtube.com/playlist?list=PLTBqohhFNBE9jRhvdtnuxj9FiOtDOnqoy"),
        ("DTU: Introduction to Statistics", "https://www.youtube.com/playlist?list=PLaLOVNqqD-2FE31HVMLOEapRdKhXAK9gI"),
    ],
    "25-stochastic-processes.html": [
        ("6.262 Discrete Stochastic Processes — MIT OCW", "https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-262-discrete-stochastic-processes-spring-2011/"),
        ("Stochastic Processes 1 — NPTEL IIT Bombay", "http://nptel.ac.in/courses/111102096/"),
        ("Stochastic Processes — NPTEL IIT Bombay", "http://nptel.ac.in/courses/111102014/"),
    ],
    "26-convex-optimization.html": [
        ("EE364A Convex Optimization I — Stanford (Boyd)", "https://see.stanford.edu/Course/EE364A"),
        ("EE364B Convex Optimization II — Stanford (Boyd)", "https://see.stanford.edu/Course/EE364B"),
        ("Convex Optimization — NPTEL IIT Kanpur", "http://nptel.ac.in/courses/111104068/"),
        ("Foundations of Optimization — NPTEL IIT Kanpur", "http://nptel.ac.in/courses/111104071/"),
    ],
    "27-linear-programming.html": [
        ("Linear Programming and Extensions — NPTEL IIT Kanpur", "http://nptel.ac.in/courses/111104027/"),
        ("Optimization — NPTEL IIT Kharagpur", "http://nptel.ac.in/courses/111105039/"),
    ],
    "28-numerical-analysis.html": [
        ("18.085 Computational Science and Engineering I — MIT OCW", "https://ocw.mit.edu/courses/mathematics/18-085-computational-science-and-engineering-i-fall-2008/"),
        ("18.086 Mathematical Methods for Engineers II — MIT OCW", "https://ocw.mit.edu/courses/mathematics/18-086-mathematical-methods-for-engineers-ii-spring-2006/"),
        ("Mathematics 128A Numerical Analysis — UC Berkeley (Persson)", "http://persson.berkeley.edu/mathW128A/lecture_videos.html"),
        ("Elementary Numerical Analysis — NPTEL IIT Bombay", "http://nptel.ac.in/courses/111101003/"),
        ("Holistic Numerical Methods", "http://nm.mathforcollege.com/videos/"),
    ],
    "29-computational-methods.html": [
        ("Advanced Scientific Computing: Numerical Methods — Harvard (Fall 2013)", "http://iacs-courses.seas.harvard.edu/courses/am205/fall13/"),
        ("Introduction to Numerical Analysis I — NCSU", "http://www4.ncsu.edu/~ctk/ma580.html"),
        ("Numerical Methods of ODE and PDE — NPTEL IIT Kharagpur", "http://nptel.ac.in/courses/111105038/"),
    ],
    "30-dynamical-systems.html": [
        ("Dynamical Systems and Ergodic Theory (Spring 2024) — ETH Zurich", "https://video.ethz.ch/lectures/d-math/2024/spring/401-2374-24L/4e2c6b6a-71c6-4ca7-a1c1-608227e65d65.html"),
        ("Dynamic Data Assimilation — NPTEL IIT Madras", "http://nptel.ac.in/courses/111106082/"),
    ],
    "31-discrete-math.html": [
        ("Discrete Mathematics — NPTEL IIT Roorkee", "http://nptel.ac.in/courses/111107058/"),
        ("Discrete Mathematics — NPTEL IIT Madras", "http://nptel.ac.in/courses/111106086/"),
        ("Math 151 Finite Mathematics — U. of Victoria (Noel, Fall 2023)", "https://www.youtube.com/playlist?list=PLtxJg53s2o0Mk87lsAQyx9ObyJN6O6jfH"),
    ],
    "32-math-history.html": [
        ("MATH 274 History of Mathematics — U. of Maryland", "https://www.youtube.com/playlist?list=PL7RK4EsMAcJLlIbuiN9e0ndoPY1IIsz03"),
        ("History of Mathematics — N.J. Wildberger (UNSW)", "https://www.youtube.com/course?list=EC34B589BE3014EAEB"),
    ],
}


def make_video_block(resources):
    """Generate HTML for a collapsible video resources block."""
    items = []
    for title, url in resources:
        items.append(f'<li><a href="{url}" target="_blank">{title}</a></li>')
    inner = "\n".join(items)
    return f"""
<details class="video-resources">
<summary>추천 영상 강의 (원본 소스 기반)</summary>
<ul>
{inner}
</ul>
</details>
"""


# First, strip any previously inserted video blocks from all chapter files
import re

for filepath in sorted(CHAPTERS.glob("*.html")):
    if filepath.name == "manifest.txt":
        continue
    content = filepath.read_text(encoding="utf-8")
    # Remove existing video-resources blocks (from previous runs)
    cleaned = re.sub(
        r'\n*<details class="video-resources">.*?</details>\n*',
        "\n",
        content,
        flags=re.DOTALL,
    )
    if cleaned != content:
        filepath.write_text(cleaned, encoding="utf-8")

# Now insert fresh video blocks
count = 0
for filename, resources in VIDEOS.items():
    filepath = CHAPTERS / filename
    if not filepath.exists():
        print(f"  SKIP: {filename} not found")
        continue

    content = filepath.read_text(encoding="utf-8")
    block = make_video_block(resources)

    # Insert after <p class="source-tag"> if exists
    if '<p class="source-tag">' in content:
        lines = content.split("\n")
        new_lines = []
        inserted = False
        for line in lines:
            new_lines.append(line)
            if not inserted and 'class="source-tag"' in line:
                new_lines.append(block)
                inserted = True
        if inserted:
            content = "\n".join(new_lines)
        else:
            content += block
    else:
        # Insert before final <hr> or at the end
        content = content.rstrip()
        if content.endswith("<hr>"):
            content = content.rsplit("<hr>", 1)[0] + block + "\n<hr>"
        else:
            content += "\n" + block + "\n"

    filepath.write_text(content, encoding="utf-8")
    count += 1
    print(f"  {filename}: {len(resources)} sources")

print(f"\nDone: {count} chapters updated with original sources only")
