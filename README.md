# Student Dropout Early Warning System (ML)

## Problem Statement
Early identification of students at risk of dropping out allows institutions to take timely preventive actions.

## Dataset
xAPI-Edu-Data containing demographic, academic, and behavioral features.

## Methodology
- Data cleaning & label encoding
- Handling class imbalance using SMOTE
- Model training:
  - Logistic Regression
  - Random Forest (final model)
- Recall-focused threshold tuning
- Risk score generation

## Model Performance
- Accuracy: ~81%
- Recall (Dropout class): 60%
- Optimized to minimize missed at-risk students

## Output
Each student is assigned:
- Risk Score (0–1)
- Risk Level (Low / Medium / High)
- Dropout Prediction (0/1)

## Explainability
Feature importance shows attendance, discussion participation, and resource usage as key indicators.

## Deployment
Interactive Streamlit app for CSV-based predictions.

## Tech Stack
Python, Pandas, NumPy, Scikit-learn, SMOTE, Streamlit

## Limitations
- No psychological or financial factors included
- Dataset size is relatively small

## Future Work
- Add SHAP explainability
- Time-series student monitoring
- Integration with institutional dashboards
