# Module 1 — Dataset Plan

## Datasets downloaded
- **RDD2022 (India + Japan subsets)** — official sekilab dataset. Note: the direct S3 links
  listed in the RoadDamageDetector repo README are currently dead (403 Forbidden — the bucket
  now blocks anonymous access). Worked around this by pulling from the official Figshare
  mirror (https://doi.org/10.6084/m9.figshare.21431547) instead: the mirror hosts one combined
  13GB zip containing per-country sub-zips, so India.zip (502.3MB) and Japan.zip (1022.9MB)
  were extracted selectively via HTTP range requests (remotezip) without downloading the
  full 13GB. Pascal VOC XML annotations. Note: actual class labels found in the data include
  more than the four "headline" classes (D00/D10/D20/D40) — e.g. D43, D50 also appear; don't
  hardcode a 4-class assumption later.
  Actual structure: {Country}/train/images/, {Country}/train/annotations/xmls/,
  {Country}/test/images/.
- **Annotated Potholes Dataset** (Kaggle, chitholian/annotated-potholes-dataset) — smaller
  pothole-only set for fast early prototyping before scaling up to RDD2022.

## Folder structure (Colab/Drive)
data/
  raw/                              (unmodified downloaded data)
    India/train/images/, India/train/annotations/xmls/, India/test/images/
    Japan/train/images/, Japan/train/annotations/xmls/, Japan/test/images/
    annotated-potholes/
  train/
    images/
    annotations/
  val/
    images/
    annotations/
  negatives/
    images/
    annotations/

## Negative-sample plan (scoped, not final)
Per the iWatchRoadv2 finding, false positives on shadows/manholes trace back to missing
labeled negatives, not a model architecture gap. Plan:
- Source 1: crop background regions from RDD2022 images with no annotated damage
  (empty/partial XML) — free, no extra download needed.
- Source 2 (if Source 1 lacks variety): a small supplementary road-surface dataset
  specifically for shadows, manhole covers, tar patches, oil stains — to be sourced in a
  later session if Source 1 proves insufficient.
- Target ratio: starting around 1:3 to 1:2 (negative:positive), to be tuned once real
  false-positive rates show up in evaluation — not locking this in today.

## Environment check
Pascal VOC XML parsing confirmed on a sample RDD2022 annotation file — class labels and
bounding boxes parse correctly.
