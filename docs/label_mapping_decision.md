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

**Note on D50:** D50 does not appear in the Maeda et al. 2018 8-class scheme that explains the
other extra codes (D01, D0w0, D11, D43, D44). One unrelated, newer 10-class scheme (N-RDD2024,
a 2024 dataset with different numbering) defines D50 as "pedestrian crossing blur" — but that
is a different paper's taxonomy, not confirmed to apply to RDD2022's raw India/Japan labels.
Without a confirmed definition specific to this dataset, D50 is excluded below rather than
guessed into a bucket, for the same reason D43/D44 were not guessed.

## Source of the Extra Classes

The official CRDDC2022 `label_map.pbtxt` defines only 4 classes: D00, D10, D20, D40.

The additional codes trace back to the original Japanese road-damage classification scheme
(Maeda et al., 2018), based on Japan's official Road Maintenance Guidebook, and documented in
Table 1 of the RDD2022 paper (Arya et al., 2022, arXiv:2209.08538). That table draws a clear
distinction between two fundamentally different types of deterioration:

- **Pavement deterioration:** D00, D01, D10, D11, D20, D40
- **Road marking deterioration:** D43, D44

Specifically:
- **D01** — longitudinal crack, construction-joint variant (a subtype of D00)
- **D11** — transverse crack, construction-joint variant (a subtype of D10)
- **D43** — crosswalk marking blur (road marking, not pavement damage)
- **D44** — white line marking blur (road marking, not pavement damage)
- **D0w0** — 1 instance total, likely an annotation artifact

## Decision

**Revised severity mapping:**

| Severity Bucket | Classes Included | Reasoning |
|---|---|---|
| **Minor** | D00, D01, D10, D11 | All crack subtypes fold in naturally — same damage type, finer official subcategories |
| **Major** | D20 | Unchanged — alligator cracking |
| **Severe/Pothole** | D40 | Unchanged — official definition already covers potholes, rutting, bumps, and separation |
| **Excluded from this project** | D43, D44 | Road-marking degradation is a categorically different hazard type (visibility of markings, not structural pavement damage) — out of scope for this module |
| **Excluded — unconfirmed** | D50 | No confirmed definition for this dataset specifically; not part of the Maeda 2018 scheme that explains the other extra codes |
| **Excluded — negligible** | D0w0 | Single instance, not statistically meaningful |

The Kaggle Annotated Potholes Dataset's generic `pothole` label maps to **Severe/Pothole**,
consistent with D40.

## Why D43/D44 Were Excluded Rather Than Force-Mapped

D43 and D44 together account for ~17.75% of all instances (5,850 of 32,957), with D44 alone
larger than D43, D50, or D10. This is too large a share to fold into an unrelated bucket
without a real justification. Since the source paper itself treats road-marking deterioration
as a separate category from pavement deterioration, excluding them here is a defensible,
citable methodological choice — not a guess, and not an arbitrary data loss.

This keeps the project's scope consistent with the original problem statement (pavement
hazard detection), and leaves road-marking degradation as a documented, honest limitation
rather than a hidden one.

## Follow-Up Item

D50 (3,581 instances, 10.9% of the dataset) is currently excluded because its definition for
this specific dataset is unconfirmed. If time allows later in the project, it's worth checking
the original per-image XML source or contacting the dataset maintainers to confirm its meaning
— it's a large enough share of the data that recovering it properly (rather than leaving it
excluded indefinitely) would be a reasonable use of spare time.

## Data Retained vs. Excluded

- **Retained for training:** D00, D01, D10, D11, D20, D40 — 23,525 instances (71.4%)
- **Excluded:** D43, D44, D50, D0w0 — 9,432 instances (28.6%)

This is a larger exclusion than initially expected, but each exclusion is individually
justified above rather than being a single blanket guess.

## Status

Decision finalized Day 3 (September 16, 2026). Adrija cleared to resume label remapping and
YOLO format conversion using this rubric.
