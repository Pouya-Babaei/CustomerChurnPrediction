# Sprint 06 — Random Forest Baseline

## Objective

Implement a baseline Random Forest classifier using the existing preprocessing pipeline and compare its performance with all previously implemented baseline models.

---

## Tasks Completed

- Reviewed the fundamentals of ensemble learning and Random Forest.
- Implemented a baseline Random Forest pipeline.
- Trained the model using default hyperparameters.
- Generated predictions on the test dataset.
- Evaluated model performance using:
  - Accuracy
  - Precision
  - Recall
  - F1-score
- Generated the Confusion Matrix.
- Generated the Classification Report.
- Compared Random Forest with:
  - Logistic Regression
  - Decision Tree
  - K-Nearest Neighbors (KNN)
  - Gaussian Naive Bayes

---

## Key Findings

- Random Forest improved over the default Decision Tree.
- Logistic Regression remained the strongest baseline model overall.
- Random Forest achieved competitive Precision but lower Recall.
- Increasing model complexity does not necessarily improve predictive performance.
- Hyperparameter tuning may further improve Random Forest performance.

---

## Lessons Learned

- Random Forest is an ensemble learning algorithm that reduces variance by combining multiple Decision Trees.
- Bootstrap sampling and random feature selection improve generalization.
- Ensemble methods reduce overfitting but do not guarantee superior performance.
- Business objectives should guide model selection rather than relying solely on overall Accuracy.

---

## Status

✅ Completed