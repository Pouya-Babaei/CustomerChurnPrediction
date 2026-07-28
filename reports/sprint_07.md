# Sprint 07 — Support Vector Machine Baseline

## Sprint Goal

Build a baseline Support Vector Machine classifier using the shared preprocessing pipeline and compare its performance with previous baseline models.

---

## Research

- Why evaluate SVM after Random Forest?
- How does SVM separate classes?
- Why is feature scaling important for SVM?
- What is the role of kernel functions?
- When should SVM be preferred over Logistic Regression?
- Which additional factors should influence model selection besides predictive performance?

---

## Implementation

- Built SVC pipeline
- Reused shared preprocessing pipeline
- Trained baseline model
- Generated predictions
- Evaluated model performance

---

## Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Classification Report

---

## Results

| Model | Accuracy | Precision | Recall | F1 |
|------|---------:|----------:|-------:|------:|
| Logistic Regression | **0.806** | **0.656** | **0.567** | **0.608** |
| Decision Tree | 0.712 | 0.458 | 0.458 | 0.458 |
| KNN | 0.761 | 0.552 | 0.544 | 0.548 |
| GaussianNB | 0.679 | 0.445 | **0.843** | 0.583 |
| Random Forest | 0.780 | 0.612 | 0.467 | 0.530 |
| Support Vector Machine | 0.795 | 0.655 | 0.485 | 0.557 |

---

## Key Findings

- SVM achieved competitive performance.
- Precision remained close to Logistic Regression.
- Recall was lower, increasing the number of False Negatives.
- Logistic Regression remains the strongest baseline classifier.
- SVM is a promising candidate for future hyperparameter tuning.

---

## Sprint Retrospective

### What went well

- Successfully implemented the baseline SVM pipeline.
- Reused the shared preprocessing pipeline.
- Completed a fair comparison across all baseline classifiers.

### Challenges

- SVM produced lower Recall than Logistic Regression.
- Selecting models based on business objectives rather than a single metric required careful analysis.

### Lessons Learned

- SVM is highly sensitive to feature scaling.
- Kernel functions allow SVM to model complex decision boundaries.
- Simpler models can outperform more sophisticated algorithms depending on the dataset.

### Next Sprint

Perform a comprehensive comparison of all baseline models and identify the most promising candidates for hyperparameter tuning.