# Module 2 — Initial Feature Plan

## Objective

The risk-prediction model will combine computer-vision-based road-hazard information with historical accident data, weather, time, and location information.

## Initial Feature List

| Feature | Source | Granularity | Purpose |
|---|---|---|---|
| Weather condition | OpenWeatherMap API | City | Capture current environmental conditions |
| Temperature | OpenWeatherMap API | City | Represent current weather conditions |
| Time of day | Weather timestamp / event time | City | Capture temporal patterns |
| Location | City / geographic coordinates | City | Identify the geographic area |
| Pothole accident history | MoRTH | State/UT | Provide a coarse historical risk prior |
| Surface-condition accident history | MoRTH | State/UT | Represent historical road-surface-related risk |
| Detected potholes/cracks | Computer vision model | Image / road observation | Represent current visible road hazards |

## Limitation of Current Accident Data

The available MoRTH road-condition dataset is at State/UT level and covers 2014 and 2016. Therefore, it should be treated as a coarse historical prior rather than a precise road-segment-level feature.

## Potential Future Indian Data Sources

Potential sources for finer-grained accident and road-condition information include:

- State Public Works Department (PWD) portals
- City traffic police open-data portals
- Other government open-data sources that provide city- or road-level information

These are candidates for later investigation and are not being fully resolved as part of Day 2.

## Planned Risk-Prediction Concept

The initial concept is to combine current visual road-hazard indicators with contextual information such as weather, time, location, and historical road-condition/accident information to estimate relative risk for a road area.
