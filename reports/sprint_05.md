# Sprint 05

## Objective

Implement K-Nearest Neighbors and Gaussian Naive Bayes classifiers and compare their performance with the previously developed baseline models.

---

## Tasks Completed

- Implemented the KNN classification pipeline.
- Implemented the Gaussian Naive Bayes classification pipeline.
- Trained and evaluated both models.
- Generated confusion matrices and classification reports.
- Compared all baseline classification models.
- Analyzed the trade-off between Precision and Recall.

---

## Key Findings

- Logistic Regression remained the strongest overall baseline model.
- KNN achieved competitive performance and outperformed the default Decision Tree.
- Gaussian Naive Bayes produced the highest Recall but generated a large number of false positive predictions.
- Model selection should be aligned with business objectives rather than Accuracy alone.

---

## Sprint Retrospective

This sprint demonstrated that different algorithms optimize different aspects of model performance. Although Gaussian Naive Bayes produced the lowest Accuracy, it achieved the highest Recall, making it an interesting option for customer churn prediction where identifying at-risk customers is a priority. The sprint also reinforced the importance of evaluating multiple metrics before selecting a model.

---

## Status

✅ Completed