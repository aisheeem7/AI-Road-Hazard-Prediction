# Week 1, Day 3 Progress Report

**Date:** Wednesday, September 16, 2026
**Team:** Aishee, Adrija, Debopriya

## Planned Tasks

### Aishee
- Write formal label-mapping decision document
- Update architecture diagram and feature plan for the 3-class severity signal
- Coordinate with team, resolve any blockers
- Create and fill Day 3 report

### Adrija
- Class-count verification across RDD2022 + Kaggle datasets
- Label remapping (raw classes to severity buckets)
- YOLO format conversion and data.yaml setup
- Optional: short sanity-check training run

### Debopriya
- Exploratory data analysis on cleaned MoRTH dataset
- Build baseline risk-prediction model
- Convert weather API test into a reusable script
- Document results and limitations

## Tasks Completed

### Adrija — Partial (Blocked Mid-Day, Resolved by End of Day)
- [x] Class counts completed across RDD2022 India+Japan (18,212 files, 32,957 instances)
      and Kaggle Potholes (1,740 instances) — pushed to `docs/module1_class_counts.md`
- [x] **Major finding:** discovered the official CRDDC2022 label scheme only defines
      4 classes (D00/D10/D20/D40). The other 6 codes present in the raw data
      (D01/D0w0/D11/D43/D44/D50) are not part of that scheme, together accounting for
      ~29% of all instances
- [x] **Correctly paused** label remapping and YOLO conversion rather than guessing
      bucket assignments for unconfirmed classes — flagged the team for a decision
      instead of proceeding on assumptions
- [x] Continued non-blocked work (folder structure) while waiting
- [ ] Label remapping — **unblocked end of day**, resumes Day 4 (see decision below)
- [ ] YOLO format conversion and data.yaml — resumes Day 4
- [ ] Sanity-check training run — deferred to Day 4

### Debopriya — Complete
- [x] EDA completed on cleaned MoRTH dataset across 36 State/UTs, comparing 2014 vs
      2016 pothole-related accident counts, with high/low-count states documented
- [x] Baseline Logistic Regression model built: 36 State/UT observations, 8
      MoRTH-derived features, 77.78% accuracy, 0.75 F1 score
- [x] **Self-identified limitation:** flagged possible target leakage, since some
      features are closely related to the pothole-based target — noted as a real
      caveat rather than presenting the accuracy figure uncritically
- [x] `weather_api.py` built — reusable script returning temperature, humidity,
      condition, and timestamp for a given city; API key handled via environment
      variable, not committed
- [x] **Independently verified the class-taxonomy question** by checking the official
      CRDDC2022 challenge documentation directly — confirmed only D00/D10/D20/D40 are
      official, and correctly declined to guess a remapping without team alignment
- [x] Full results and limitations documented in `docs/module2_baseline_results.md`
- [x] Submitted via PR #3 (`daisy/day3-baseline`), reviewed and merged

### Aishee
- [x] Investigated the class-taxonomy question raised by Adrija; initially traced the
      extra codes to the Maeda et al. 2018 classification (RDD2022 paper Table 1)
- [x] **Revised the decision** after Debopriya independently found the official
      CRDDC2022 challenge site, which explicitly states non-official classes "may be
      ignored" — adopted this simpler, more authoritative source over the original
      inference-based approach
- [x] Finalized label-mapping decision — see `docs/label_mapping_decision.md`
- [x] Communicated the decision to Adrija to unblock Day 4 work
- [x] Reviewed and merged PR #3

## Challenges Faced

- **Class taxonomy was more complex than assumed:** RDD2022's raw India/Japan data
  contains 10 codes, not the expected 4 or the originally-assumed 6. Root cause was
  identified and the decision was **revised same-day** after a more authoritative
  source (the official CRDDC2022 site) was found, superseding an earlier
  inference-based rubric. Resolved same day, but cost roughly half a day of Adrija's
  planned work.
- **Process note:** Adrija and Debopriya independently investigated the same question
  in parallel without coordinating — both reached compatible answers, so no harm done,
  but worth flagging so effort isn't duplicated again.
- D50 remains formally unresolved (excluded per official guidance, no confirmed
  definition found), representing 10.9% of instances.
- **Target leakage risk** in Debopriya's baseline model — documented as an open
  limitation, not yet resolved, will need revisiting when more granular data becomes
  available.

## Tasks Carried Over / Blockers

- Adrija's label remapping, YOLO conversion, and sanity-check training run carry over
  to Day 4, now unblocked with the finalized rubric
- D50 class definition remains an open research item, not currently blocking, but
  worth revisiting if time allows

## Plan for Next Week

Day 4 priorities: Adrija resumes and completes label remapping + YOLO conversion using
the finalized rubric, then runs the sanity-check training. Debopriya begins addressing
the target-leakage question in the baseline model and explores whether any additional
Indian data sources (state PWD, traffic police, if available) can improve granularity.
Aishee to review Day 4 outputs against the updated architecture diagram for consistency.
