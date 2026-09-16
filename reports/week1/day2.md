# Week 1, Day 2 Progress Report

**Date:** Tuesday, September 15, 2026
**Team:** Aishee, Adrija, Debopriya

## Planned Tasks

### Aishee
- Draft system architecture diagram, updated for Day 1 findings
- Coordinate with Adrija and Debopriya
- Create and fill Day 2 report

### Adrija
- Download RDD2022 (India + Japan) and Kaggle Annotated Potholes dataset
- Scope negative-sample sourcing plan
- Set up dataset folder structure (train/val/negatives)
- Confirm Pascal VOC XML parsing works
- Push dataset plan to documentation

### Debopriya
- Clean and standardize the MoRTH accident CSV
- Confirm OpenWeatherMap key is active, test a live city pull
- Draft initial feature list for the risk-prediction model
- Push cleaned data script and feature plan

## Tasks Completed

### Aishee
- [x] System architecture diagram updated to reflect negative-sample handling
      (Module 1) and city-level data enrichment (Module 2)
- [x] Coordinated with both teammates and reviewed their pull requests/commits

### Adrija
- [x] RDD2022 India + Japan subsets downloaded via the official Figshare mirror
      (DOI: 10.6084/m9.figshare.21431547) — **the direct S3 links in the repo README
      are currently dead (403 Forbidden)**, documented the workaround (selective
      extraction via HTTP range requests) so the team doesn't hit the same issue again
- [x] Annotated Potholes Dataset (Kaggle) downloaded for fast prototyping
- [x] Pascal VOC XML parsing confirmed working on sample annotations
- [x] **Key finding:** the dataset contains additional damage classes beyond the four
      headline categories (D00/D10/D20/D40) — D43 and D50 also appear. Label-mapping
      logic must not hardcode a 4-class assumption.
- [x] Folder structure set up (`train/`, `val/`, `negatives/`, each with images/annotations)
- [x] Negative-sample sourcing plan scoped and pushed to `docs/module1_dataset_plan.md`
      — primary source: cropped background regions from RDD2022's own un-annotated
      areas; target negative:positive ratio 1:3–1:2, to be tuned during evaluation

### Debopriya
- [x] MoRTH accident CSV cleaned and column-standardized across 2014/2016 sections
- [x] OpenWeatherMap key confirmed active, live pull tested for a demo city
- [x] Feature plan drafted (`docs/module2_feature_plan.md`), combining weather/time/
      location features (Moosavi approach) with MoRTH pothole-cause data used as a
      coarse historical prior rather than a precise segment-level input
- [x] Reproducible cleaning script (`src/clean_road_conditions.py`) pushed, raw CSV
      correctly excluded from the repo per `.gitignore`
- [x] Work submitted via PR #2, reviewed and merged

## Challenges Faced

- **RDD2022's official download links are broken** — worked around via Figshare mirror;
  flagged so it doesn't cost time again later in the project
- **Damage class taxonomy is larger than initially assumed** (six classes, not four) —
  affects how Module 1's output labels will map to Module 2's risk categories, needs
  a short design decision before training begins
- MoRTH data's coarse granularity (from Day 1) is now formally addressed in the feature
  plan, treated as a prior signal rather than the primary input

## Tasks Carried Over / Blockers

- None outstanding for Day 2 — all planned tasks completed and verified
- Minor process note: Adrija pushed directly to `main` this round instead of via
  branch/PR — flagged as a habit to keep consistent going forward, not a blocker

## Plan for Next Week

Day 3 priorities: begin actual YOLOv8 fine-tuning setup using the prepared dataset
(Adrija), start exploratory data analysis and initial risk-model prototyping using the
cleaned CSV and feature plan (Debopriya), and finalize the label-mapping decision for
the six-class taxonomy (team decision, led by Aishee) before training begins.
