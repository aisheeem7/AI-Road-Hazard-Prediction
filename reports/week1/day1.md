# Week 1, Day 1 Progress Report

**Date:** Monday, September 14, 2026
**Team:** Aishee, Adrija, Debopriya

## Planned Tasks

### Aishee
- Set up GitHub repository and invite collaborators
- Create folder skeleton and initial documentation files
- Draft problem statement
- Read RDD2022 paper and write summary
- Create and fill Day 1 report

### Adrija
- Set up Colab and confirm GPU access
- Create Kaggle account
- Review RDD2022 GitHub repo structure
- Read iWatchRoad v2 paper and write summary
- Sanity-check YOLOv8 environment with a pretrained model

### Debopriya
- Review data.gov.in accident dataset structure
- Sign up for OpenWeatherMap API key
- Read MoRTH accident report, note key statistics
- Confirm Python data-science environment works
- Read Moosavi et al. US-Accidents paper and write summary

## Tasks Completed

### Repository Setup (Aishee)
- [x] GitHub repository created and made public
- [x] README.md, LICENSE-NOTES.md, .gitignore pushed
- [x] Both collaborators accepted invites
- [x] Folder skeleton created (docs, notebooks, reports, src)
- [x] Problem statement drafted and pushed
- [x] RDD2022 summary written and pushed

### Adrija
- [x] Colab set up, **T4 GPU confirmed** via `!nvidia-smi`
- [x] Kaggle account created
- [x] RDD2022 repo structure reviewed — Pascal VOC XML format, four damage classes
      (D00, D10, D20, D40)
- [x] iWatchRoadv2 paper summary written and pushed
      (`docs/literature/iwatchroadv2_summary.md`)
- [x] **Key finding:** the paper's main false-positive fix is a data strategy, not an
      architecture change — deliberately including negative samples (shadows, manholes,
      tar patches) so the model doesn't learn "dark blob = pothole." This directly informs
      how we should build our own training set.
- [x] YOLOv8n sanity-check inference ran cleanly on a sample image

### Debopriya
- [x] Verified the actual MoRTH/data.gov.in road-condition CSV — confirmed
      pothole-related fields are genuinely present: "Rutted/Pot Holes" (2014) and
      "Pot Holes" (2016), each broken down by accidents, killed, and injured
- [x] **Key finding:** this dataset is state/UT-level only, covering just 2014 and
      2016 — no GPS coordinates or road-segment granularity
- [x] Confirmed pandas, NumPy, and scikit-learn import successfully
- [x] Created OpenWeatherMap API key (initial 401 was expected activation delay)
- [x] Reviewed MoRTH Road Accidents report and noted key national statistics
- [x] Read Moosavi et al. (2019) and wrote literature summary with citation, focused
      on weather, time-of-day, location, and points-of-interest features
- [x] Used a branch and PR (`daisy/day1-literature`) rather than pushing directly to
      main — reviewed and merged into main

## Challenges Faced

- **MoRTH dataset granularity is coarser than needed** for segment-level prediction
  (state/UT-level, only two years of data) — the risk-modeling approach will need to
  combine this with city-level weather/time features rather than relying on it alone
- **False-positive risk in hazard detection** — both the iWatchRoadv2 findings and general
  CV experience suggest shadows/manholes will be a real problem; our training data
  strategy needs negative samples built in from the start, not added later as a fix

## Tasks Carried Over / Blockers

- None outstanding — all planned Day 1 tasks completed by all three team members
- Debopriya to do a final live-weather-pull test once the OpenWeatherMap key is
  confirmed fully active (expected to resolve on its own)

## Plan for Next Week

Day 2 priorities: begin dataset acquisition in earnest (download RDD2022 subset and
Kaggle pothole dataset for Adrija; pull and clean the MoRTH accident CSV for Debopriya),
and start drafting the system architecture diagram for mentor sign-off. Given today's
finding on negative samples, Day 2 should also include planning for how negative
examples will be sourced/labeled alongside the positive damage classes.
