# Module 1 — Class Count Verification (Day 3)

## RDD2022 (India + Japan) — 18,212 annotation files scanned

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
| **Total** | **32957** | 100%   |

## Kaggle Annotated Potholes — 665 image files scanned
| Class   | Instances |
|---------|-----------|
| pothole | 1740      |

## FLAG — class scheme discrepancy (blocks remapping, not counts)
The official `label_map.pbtxt` shipped with the CRDDC2022 release (the same Figshare source
used for the India/Japan download) defines **only 4 classes: D00, D10, D20, D40**.

D01, D0w0, D11, D43, D44, and D50 are NOT part of the official RDD2022 label scheme — they
appear only in the raw per-country India/Japan XML annotations, outside the challenge's own
recognized set. Together these six "extra" classes account for **9656 instances (~29.3%) of
all annotated damage** — most notably D44 (5057 instances), which is larger than D43, D50,
and even the official D10 class, and is not covered by the current Minor/Major/Severe
remapping rule (Minor: D00,D10 / Major: D20,D43 / Severe: D40,D50).

No confirmed definition for D01/D0w0/D11/D43/D44 is available yet — assigning them a severity
bucket without one would be a guess, not a decision. Label remapping and YOLO conversion are
paused pending team input on how to handle these classes (options: exclude entirely, map by
researching their actual meaning, or treat as a 4th "unclassified" bucket).

The Kaggle Annotated Potholes dataset uses a single generic `pothole` label with no severity
subtype — how this maps into the severity scheme also needs a team decision (current working
assumption: Severe/Pothole bucket, not yet confirmed).

## Environment note
Colab runtime reset mid-session partway through the day (second time this has happened across
Day 2/3) — data now persisted to Google Drive (`/content/drive/MyDrive/road_hazard_data`)
instead of `/content` to avoid re-downloading on future resets.
