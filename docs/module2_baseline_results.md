# Module 2 — Baseline Results

## Exploratory Data Analysis

The MoRTH road-condition dataset contains 37 rows, including 36 State/UT records and one national Total row. The Total row was excluded from State/UT-level analysis.

### Accident Distribution

The 2014 accident distribution varies substantially across State/UTs. Maharashtra and Tamil Nadu are among the states with the highest reported accident counts, while several smaller states and Union Territories have substantially lower counts.

### Pothole-related Accidents

Pothole-related accident counts vary considerably across State/UTs.

In 2014, the highest reported counts were:
- Madhya Pradesh: 2,962
- Uttar Pradesh: 2,406
- Tamil Nadu: 1,665
- Maharashtra: 565
- Gujarat: 506

In 2016, the highest reported counts were:
- Uttar Pradesh: 1,436
- Maharashtra: 1,064
- Tamil Nadu: 621
- Madhya Pradesh: 609
- Kerala: 536

The lowest reported counts included several State/UTs with zero pothole-related accidents in the selected fields.

These results are descriptive only. The dataset is State/UT-level, covers 2014 and 2016, and uses different labels for the pothole-related fields between the two years.

## Baseline Risk Model

A preliminary Logistic Regression model was developed as a first prototype.

### Target

The target was defined as:
- 1: State/UT had more than zero reported pothole-related accidents in 2014
- 0: State/UT had zero reported pothole-related accidents in 2014

Class distribution:
- Class 1: 22
- Class 0: 14

### Features

Eight MoRTH-derived road-condition and pothole-related features were used.

Weather and time-of-day were not available in the current MoRTH CSV and therefore were not included in this first baseline.

### Results

- Accuracy: 77.78%
- F1 Score: 0.75

### Interpretation

These are preliminary prototype results. The modeling dataset contains only 36 State/UT observations, with 27 training samples and 9 test samples. In addition, some selected features are closely related to the pothole-based target, so target leakage may be present. The results should therefore not be treated as final real-world predictive performance.

## Weather Pipeline

A reusable `weather_api.py` script was created to retrieve weather information for a specified city.

The script returns:
- City
- Temperature
- Humidity
- Weather condition
- Timestamp

The OpenWeatherMap API key is supplied through an environment variable and is not stored in the repository.

## Limitations

- State/UT-level rather than road-segment-level data
- Only 2014 and 2016 in the current MoRTH dataset
- Small modeling sample size
- Weather and time-of-day are not yet joined to the accident dataset
- Baseline is intended only as an initial prototype

## Day 4 — Leakage Review and Leakage-Reduced Model

### Target Leakage Review

The Day 3 baseline used features including 2014 pothole-related killed/injured counts and 2016 pothole-related accident, killed, and injured counts.

The 2014 pothole killed/injured features are closely related to the 2014 pothole-accident target and were therefore excluded from the revised model.

The 2016 pothole-related fields were also excluded from the revised model because they represent a later year than the 2014 target.

### Leakage-Reduced Features

The revised Logistic Regression model used:

- `speed_breakers_number_of_accidents_2016`
- `sharp_curve_number_of_accidents_2016`
- `steep_gradient_number_of_accidents_2016`

### Results Comparison

| Model | Accuracy | F1 Score |
|---|---:|---:|
| Day 3 original baseline | 77.78% | 0.7500 |
| Day 4 leakage-reduced model | 66.67% | 0.5714 |

Both models used the same 36 State/UT observations, with a 27/9 train-test split, `random_state=42`, and stratification.

### Interpretation

The leakage-reduced model produced lower Accuracy and F1 than the original baseline. This indicates that the original performance was partly supported by features closely related to the target.

This revised model reduces direct target overlap, but it is not a fully forecast-safe temporal model because the remaining MoRTH features are from 2016 while the target is based on 2014 data.

The results remain preliminary because the dataset contains only 36 State/UT observations.

## Day 5 — Weather-Integrated Model

### Weather Integration

The reusable `src/weather_api.py` pipeline was integrated into the modeling workflow.

For a 10-State/UT demonstration set, current weather was retrieved for representative cities and merged with the MoRTH records.

Weather features used in the model:

- `temperature`
- `humidity`

The existing leakage-reduced road-condition features were retained:

- `speed_breakers_number_of_accidents_2016`
- `sharp_curve_number_of_accidents_2016`
- `steep_gradient_number_of_accidents_2016`

### Results

| Model | Dataset / Setup | Accuracy | F1 Score |
|---|---|---:|---:|
| Day 3 original baseline | 36 State/UTs | 77.78% | 0.7500 |
| Day 4 leakage-reduced | 36 State/UTs | 66.67% | 0.5714 |
| Day 5 weather-integrated | 10-State demo | 66.67% | 0.6667 |

The Day 5 experiment used 7 training observations and 3 testing observations with `random_state=42` and stratification.

### Important Limitation

The weather values retrieved by OpenWeatherMap represent current weather conditions rather than historical weather conditions for the 2014 accident records.

Therefore, the Day 5 result demonstrates the technical integration of weather features into the model pipeline. It should not be interpreted as a valid historical 2014 weather-performance comparison.

The Day 5 test set is also different from the 36-State/UT dataset used for Days 3 and 4, so the metrics are not directly comparable as a controlled performance experiment.

### Finer-Granularity Indian Data Sources

The current MoRTH dataset is State/UT-level. The Government of India's Open Government Data platform provides additional road-accident datasets, including State/UT-level data and datasets for Million Plus cities. These datasets can be investigated as potential sources for finer-granularity features.

Future work can also investigate accident-location data from systems such as IRAD/e-DAR and relevant state or city traffic authorities, subject to data availability and access.