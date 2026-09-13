# Problem Statement

Road accidents in India are strongly linked to road surface defects, yet most existing
systems address this reactively rather than proactively. A pothole or crack is typically
only recorded after a citizen complains or a vehicle is damaged, with no continuous,
low-cost way to monitor road conditions. Furthermore, hazard detection and accident-risk
prediction are treated as separate problems: existing tools such as RoadMetrics and
iWatchRoad identify where a defect currently exists, but do not combine this with
historical accident data, weather conditions, and time-of-day patterns to estimate which
road segments are likely to become dangerous. Relevant data does exist, but it is
fragmented, government accident statistics, road-condition imagery, and weather records
are maintained separately with no unified system connecting them. This project addresses
that gap by building an integrated pipeline that detects road hazards from images and
fuses that output with historical accident and weather data into a single, explainable
risk score per road segment.
