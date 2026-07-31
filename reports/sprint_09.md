# Sprint 09 — Hyperparameter Tuning

## Goal

Optimize the strongest baseline models using GridSearchCV and identify the best-performing classifier for customer churn prediction.

## Models Tuned

- Logistic Regression
- Random Forest
- Support Vector Machine

## Hyperparameter Optimization

- GridSearchCV
- 5-fold Cross Validation
- Recall optimization
- Pipeline-based preprocessing

## Final Results

| Model | Accuracy | Precision | Recall | F1 |
|-------|---------:|----------:|--------:|--------:|
| Logistic Regression | **0.806** | **0.656** | **0.567** | **0.608** |
| Random Forest | 0.788 | 0.630 | 0.488 | 0.550 |
| SVC | 0.777 | 0.588 | 0.535 | 0.560 |

## Key Findings

- Logistic Regression remained the strongest model after tuning.
- Random Forest became more generalized after limiting tree depth.
- SVC achieved its best performance with a polynomial kernel.
- Increasing model complexity did not improve the overall business-oriented performance.

## Sprint Retrospective

This Sprint demonstrated that hyperparameter tuning alone cannot compensate for limitations in feature representation. The strongest baseline model remained the best-performing classifier after optimization, suggesting that future improvements should focus on feature engineering, threshold optimization, and explainability rather than additional model complexity.