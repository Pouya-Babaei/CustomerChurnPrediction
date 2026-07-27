# Sprint 04 — Decision Tree Baseline

## Objective

The objective of this sprint was to implement the first tree-based classification model and compare its performance against the Logistic Regression baseline.

---

## Tasks Completed

- Implemented a Decision Tree classifier using Scikit-learn.
- Reused the existing preprocessing pipeline.
- Trained the baseline Decision Tree model.
- Evaluated the model using multiple classification metrics.
- Compared Decision Tree with the Logistic Regression baseline.

---

## Pipeline Architecture

```
Raw Dataset
      │
      ▼
Train / Test Split
      │
      ▼
ColumnTransformer
      │
      ▼
Decision Tree Classifier
      │
      ▼
Prediction
      │
      ▼
Evaluation
```

---

## Results

| Model | Accuracy | Precision | Recall | F1-score |
|------|---------:|----------:|-------:|---------:|
| Logistic Regression | 0.806 | 0.656 | 0.567 | 0.608 |
| Decision Tree | 0.712 | 0.458 | 0.458 | 0.458 |

---

## Key Findings

- The baseline Decision Tree underperformed compared to Logistic Regression across all evaluation metrics.
- Recall decreased significantly, resulting in more churned customers being missed.
- The default Decision Tree configuration did not generalize well on unseen data.
- Future hyperparameter tuning may improve the model's performance.

---

## Sprint Retrospective

This sprint introduced the first nonlinear classification model into the project. Despite its ability to capture complex decision boundaries, the default Decision Tree performed worse than the Logistic Regression baseline.

The sprint reinforced the importance of objective model evaluation and demonstrated that increasing model complexity does not necessarily improve predictive performance.

---

## Next Sprint

The next sprint will implement another baseline classification algorithm and continue building a comprehensive model comparison benchmark.