# Sprint 03 — Baseline Classification Model

## Objective

The objective of this sprint was to develop the first baseline classification model for customer churn prediction. A complete machine learning pipeline was implemented to establish a reliable benchmark for future model comparison while preventing data leakage through proper preprocessing.

---

## Tasks Completed

- Defined feature matrix (X) and target variable (y).
- Encoded the target variable (`No → 0`, `Yes → 1`).
- Split the dataset into training and testing sets using stratified sampling.
- Built a preprocessing pipeline using `ColumnTransformer`.
- Applied:
  - Ordinal Encoding for binary categorical features.
  - One-Hot Encoding for multi-class categorical features.
  - Standard Scaling for numerical features.
  - Passthrough for `SeniorCitizen`.
- Integrated preprocessing with Logistic Regression using Scikit-learn Pipeline.
- Trained the baseline model.
- Evaluated model performance using multiple classification metrics.

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
 ├── Binary Features → OrdinalEncoder
 ├── Multi-class Features → OneHotEncoder
 ├── Numerical Features → StandardScaler
 └── SeniorCitizen → Passthrough
      │
      ▼
Logistic Regression
      │
      ▼
Predictions
      │
      ▼
Model Evaluation
```

---

## Evaluation Metrics

The baseline model was evaluated using the following metrics:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Classification Report

---

## Results

| Metric | Value |
|---------|------:|
| Accuracy | 0.81 |
| Precision | 0.66 |
| Recall | 0.57 |
| F1-score | 0.61 |

### Confusion Matrix

```
[[1382  167]
 [ 243  318]]
```

---

## Key Findings

- The baseline model achieved approximately **81% accuracy**.
- Precision and Recall for churn prediction remain moderate.
- The model successfully identified general customer behavior but missed a considerable number of churned customers.
- Class imbalance may have contributed to the relatively low recall for the positive class.
- The baseline provides a reliable benchmark for future model comparison.

---

## Challenges

Several implementation challenges were encountered during this sprint:

- The target variable was initially stored as string labels (`Yes` / `No`), which caused metric calculation errors.
- The issue was resolved by encoding the target into binary values before model training.
- Care was taken to ensure that preprocessing was performed inside the pipeline to eliminate data leakage.

---

## Sprint Retrospective

This sprint successfully established the first production-style machine learning pipeline for the project.

Beyond implementing Logistic Regression, the sprint reinforced several important engineering concepts, including preprocessing pipelines, target encoding, stratified sampling, and evaluation using business-oriented classification metrics instead of relying solely on accuracy.

The resulting baseline model serves as the reference point for all future experiments.

---

## Next Sprint

Sprint 04 will focus on implementing the first tree-based classification model and comparing its performance against the Logistic Regression baseline.