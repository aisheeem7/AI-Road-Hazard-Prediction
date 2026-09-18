# Module 2 - Model Comparison

## Overview

Three modeling stages were completed during Days 3-5:

1. Day 3 - Original Logistic Regression baseline
2. Day 4 - Leakage-reduced Logistic Regression
3. Day 5 - Weather-integrated Logistic Regression

The experiments were conducted as prototype evaluations using the available MoRTH State/UT dataset.

## Model Comparison

| Model | Accuracy | F1 Score | Notes |
|---|---:|---:|---|
| Day 3 Original Baseline | 77.78% | 0.7500 | Preliminary baseline; included features closely related to the pothole-based target, so target leakage may be present. |
| Day 4 Leakage-Reduced | 66.67% | 0.5714 | Direct target-overlap features were excluded, but the remaining road features are from 2016 while the target is based on 2014. |
| Day 5 Weather-Integrated | 66.67% | 0.6667 | Added temperature and humidity using current OpenWeatherMap data for a 10-State/UT demonstration; not a historical 2014 weather evaluation. |

## Features Used

### Day 3 Original Baseline

- `rutted_pot_holes_killed_2014`
- `rutted_pot_holes_injured_2014`
- `pot_holes_number_of_accidents_2016`
- `pot_holes_persons_killed_2016`
- `pot_holes_persons_injured_2016`
- `speed_breakers_number_of_accidents_2016`
- `sharp_curve_number_of_accidents_2016`
- `steep_gradient_number_of_accidents_2016`

### Day 4 Leakage-Reduced

- `speed_breakers_number_of_accidents_2016`
- `sharp_curve_number_of_accidents_2016`
- `steep_gradient_number_of_accidents_2016`

### Day 5 Weather-Integrated

- `speed_breakers_number_of_accidents_2016`
- `sharp_curve_number_of_accidents_2016`
- `steep_gradient_number_of_accidents_2016`
- `temperature`
- `humidity`

## Experimental Setup

### Day 3

- Dataset: 36 State/UT observations
- Training samples: 27
- Test samples: 9
- Model: Logistic Regression
- Test split: 75/25
- `random_state=42`
- Stratified split

### Day 4

- Dataset: 36 State/UT observations
- Training samples: 27
- Test samples: 9
- Model: Logistic Regression
- Test split: 75/25
- `random_state=42`
- Stratified split
- Leakage-prone pothole outcome features were excluded

### Day 5

- Dataset: 10-State/UT demonstration subset
- Training samples: 7
- Test samples: 3
- Model: StandardScaler + Logistic Regression
- Test split: 70/30
- `random_state=42`
- Stratified split
- Current weather obtained through OpenWeatherMap
- Weather inputs: temperature and humidity

## Interpretation

The original Day 3 baseline achieved 77.78% Accuracy and an F1 Score of 0.7500, but its feature set contained variables closely related to the target, so target leakage may be present.

After removing leakage-prone features, the Day 4 model achieved 66.67% Accuracy and an F1 Score of 0.5714.

The Day 5 model retained the leakage-reduced road-condition features and added temperature and humidity from the weather API. It achieved 66.67% Accuracy and an F1 Score of 0.6667.

The Day 5 result should not be interpreted as a controlled improvement over Day 4 because the experiment used only 10 State/UT observations and current weather rather than historical weather corresponding to the 2014 accident records.

## Key Limitations

- The MoRTH modeling data contains only 36 State/UT observations.
- The available data is aggregated at State/UT level rather than road-segment level.
- The current road-condition dataset contains 2014 and 2016 records.
- Weather data retrieved during Day 5 represents current conditions rather than historical 2014 conditions.
- Day 5 uses a smaller 10-State/UT demonstration subset.
- The prototype results should not be treated as final real-world predictive performance.
- A future forecast-safe model should use temporally aligned accident and weather data.

## Module 1 Coordination and Week 2 Scope

Module 1 has defined three severity classes:

- Minor
- Major
- Severe-Pothole

For Week 2, Module 2 will coordinate with the Module 1 team on combining the severity output with the risk-model output through a future risk-score fusion layer.

The fusion layer is currently a coordination and design item only. It is not implemented in the Day 4-6 prototype.

The intended future workflow is:

`Road/Weather Features -> Module 2 Risk Model -> Risk Score`

and

`Road Damage/Severity Features -> Module 1 Severity Model -> Severity Class`

followed by a future fusion layer that combines both outputs for the overall road-hazard assessment.
