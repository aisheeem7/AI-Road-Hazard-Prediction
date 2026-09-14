# Literature Summary: iWatchRoadv2 (arXiv:2510.16375)

**Title:** iWatchRoadv2: Pothole Detection, Geospatial Mapping, and Intelligent Road Governance
**Authors:** Sahoo, Mohanty, Mishra (NISER Bhubaneswar / Silicon Institute of Technology)

## What they built
An end-to-end pipeline that goes from dashcam footage to a public, governance-aware map:
YOLOv8-based pothole detection → OCR-based timestamp extraction from the video overlay →
synchronization with an external GPS log to geotag each detection → results pushed to an
OpenStreetMap/Leaflet dashboard. Their v2 extension adds a "Smart Road Construction Mapper"
that links road segments to contractor and warranty metadata and auto-alerts officials when a
segment's condition worsens.

## What's different from a plain detector (relevant to our Module 1)
1. **Dataset — BharatPotHole.** Over 7,000 self-collected, self-annotated dashcam frames from
   Indian roads, deliberately spanning rain, night, dawn/dusk, and multiple road types (rural,
   urban, highway). This is a forward-facing dashcam perspective, not the overhead/top-down
   framing most academic pothole datasets use — closer to what a real vehicle-mounted or
   crowdsourced camera would see.
2. **False-positive handling (shadows/manholes) — their core trick.** Rather than a detection
   architecture change, they treat this as a data problem: they deliberately include large
   numbers of *negative* samples — road images with shadows, manhole covers, tar patches, oil
   stains, and cracks — labeled as **no pothole**. Without these negatives, they found the model
   learns to key on "dark blob on road surface" as its proxy for pothole, which is exactly what
   a shadow or manhole cover looks like from a moving dashcam at distance. Adding balanced
   negatives forces the model to learn actual pothole shape cues (irregular boundary, depth
   discontinuity, edge profile) instead of surface darkness.
3. **Scale mattered more than architecture tweaks.** They report a clear jump in detection
   reliability going from their 3k-frame subset to the full 7k-frame set, suggesting the
   negative-sample coverage (not just raw positive count) was the main driver.
4. **Everything downstream depends on getting this right.** Because their system geotags and
   escalates alerts automatically, a false positive doesn't just mislabel one image — it can
   trigger a contractor/authority notification. That raises the practical cost of false positives
   well above a typical benchmark-only detector.

## Takeaway for our project
Our RDD2022-based training set (and any of our own frames) should deliberately include
negative/no-damage examples — shadows, manhole covers, patched surfaces, plain wet roads —
rather than only positive crack/pothole crops, if we want the detector to hold up on
Indian road imagery instead of overfitting to "dark region = damage."

*(Source: arXiv:2510.16375, Sahoo et al. 2025 — summarized, not quoted.)*
