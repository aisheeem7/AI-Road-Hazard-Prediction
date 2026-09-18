# Module 1 — Label Mapping Decision

## Background

RDD2022's India and Japan subsets contain 10 raw class codes, not the 4 headline classes
(D00/D10/D20/D40) originally expected. A class-count check on Day 3 found the following
distribution across 32,957 annotated instances:

| Class | Instances | % of total |
|-------|-----------|------------|
| D00   | 5604      | 17.0%      |
| D01   | 179       | 0.5%       |
| D0w0  | 1         | 0.0%       |
| D10   | 4047      | 12.3%      |
| D11   | 45        | 0.1%       |
| D20   | 8220      | 24.9%      |
| D40   | 5430      | 16.5%      |
| D43   | 793       | 2.4%       |
| D44   | 5057      | 15.3%      |
| D50   | 3581      | 10.9%      |

## Source of the Extra Classes

The **official CRDDC2022 challenge website** (crddc2022.sekilab.global/data/) states
directly: although the RDD2022 data includes annotations for multiple categories, only
four are considered for the challenge — D00 (Longitudinal Crack), D10 (Transverse Crack),
D20 (Alligator Crack), and D40 (Potholes). A news update on the same site (August 30,
2022) states explicitly: **"annotations for other categories may be ignored."**

This is corroborated by Table 1 of the RDD2022 paper (Arya et al., 2022, arXiv:2209.08538),
which traces the extra codes to the original Japanese road-damage classification scheme
(Maeda et al., 2018): D01 and D11 are construction-joint subtypes of D00/D10, while D43 and
D44 belong to a separate "road marking deterioration" category rather than pavement damage.
D50 is not part of either the official 4-class scheme or the Maeda 8-class scheme, and no
confirmed definition was found for it in this dataset specifically.

Both Adrija and Debopriya independently investigated this question on Day 3 — Adrija via
the RDD2022 paper's classification table, Debopriya via the official CRDDC2022 challenge
site directly. The official site is the more authoritative and simpler source, so it takes
precedence in the decision below.

## Decision

**Adopt the official CRDDC2022 4-class scheme exactly, with no classes folded together:**

| Severity Bucket | Classes Included | Reasoning |
|---|---|---|
| **Minor** | D00, D10 | Official CRDDC2022 classes |
| **Major** | D20 | Official CRDDC2022 class |
| **Severe/Pothole** | D40 | Official CRDDC2022 class |
| **Excluded** | D01, D0w0, D11, D43, D44, D50 | Not part of the official CRDDC2022 scheme — the challenge's own site explicitly states these "may be ignored" |

The Kaggle Annotated Potholes Dataset's generic `pothole` label maps to **Severe/Pothole**,
consistent with D40.

## Why This Is Simpler Than the Original Approach

An earlier version of this decision folded D01 into D00 and D11 into D10 based on inference
from the paper's classification table. That inference was reasonable, but unnecessary — the
challenge organizers already settled this question directly. Excluding all six non-official
codes is both simpler to implement and easier to justify in the report: it is a direct,
citable instruction from the dataset's own official source, not an inference.

## Data Retained vs. Excluded

- **Retained for training:** D00, D10, D20, D40 — 23,301 instances (70.7%)
- **Excluded:** D01, D0w0, D11, D43, D44, D50 — 9,656 instances (29.3%)

This matches the official CRDDC2022 scope exactly, which also means our results remain
directly comparable to published benchmark numbers on this dataset.

## Process Note

Adrija and Debopriya researched this question independently and in parallel on Day 3.
Both reached compatible conclusions, so no harm done, but worth flagging so overlapping
investigation doesn't happen again — a quick "I'm looking into X" message in the group
chat would have avoided the duplication.

## Status

Decision finalized Day 3 (September 16, 2026), revised same day after Debopriya's
independent finding. Adrija cleared to resume label remapping and YOLO format conversion
using this rubric.
