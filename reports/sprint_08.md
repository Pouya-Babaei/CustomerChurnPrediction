# Sprint 08 — Baseline Model Comparison

## Goal

Compare all baseline classifiers and determine which models should proceed to hyperparameter tuning.

## Completed Work

- Reviewed all baseline model results.
- Compared evaluation metrics.
- Ranked model performance.
- Selected candidate models.
- Documented engineering decisions.

## Candidate Models

- Logistic Regression
- Random Forest
- Support Vector Machine

## Key Findings

- Logistic Regression provided the best overall trade-off.
- Gaussian Naive Bayes achieved the highest Recall.
- Random Forest showed strong optimization potential.
- SVM delivered competitive baseline performance.
- Although GaussianNB achieved the highest Recall, it was not selected for hyperparameter tuning because of its weaker overall trade-off and stronger modeling assumptions.

The final candidate models are:
    - Logistic Regression
    - Random Forest
    - SVC

## Sprint Outcome

The project is now ready for the hyperparameter tuning phase.