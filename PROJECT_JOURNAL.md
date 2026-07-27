# Project Journal

---

# Sprint 01 — Business Understanding & Exploratory Data Analysis

## Objective

Establish a clear understanding of the business problem, explore the dataset, evaluate data quality, and identify initial patterns related to customer churn.

---

## Completed Tasks

- Defined the business problem and project objectives.
- Explored the dataset structure and feature descriptions.
- Identified numerical and categorical variables.
- Performed Exploratory Data Analysis (EDA).
- Analyzed target distribution.
- Investigated numerical feature distributions.
- Explored categorical features using count plots and contingency tables.
- Conducted an initial data quality assessment.
- Identified hidden blank-string values in the `TotalCharges` feature.
- Created an initial correlation matrix for numerical variables.
- Documented business insights obtained from EDA.

---

## Key Findings

- Customer churn is moderately imbalanced.
- Contract type is one of the strongest indicators of churn.
- Customers with shorter tenure tend to churn more frequently.
- Fiber optic customers appear to have higher churn rates.
- Online Security and Technical Support services are associated with lower churn.
- Gender and MultipleLines show relatively weak relationships with churn.
- The `TotalCharges` column contains blank string values that require preprocessing.

---

## Challenges

- The `TotalCharges` feature was loaded as an object despite representing numerical values.
- Investigation revealed hidden blank-string values that prevented automatic numeric conversion.

---

## Decisions

- `customerID` will not be used for model training.
- `TotalCharges` will be cleaned and converted to a numeric feature during preprocessing.
- Data preprocessing will be implemented using reusable Scikit-learn Pipelines.

---

## Next Sprint

- Data Cleaning
- Missing Value Handling
- Data Type Conversion
- Feature Selection
- Encoding Strategy
- Build the preprocessing pipeline

---

## Sprint 02

Focused on improving dataset quality and designing a reproducible preprocessing workflow.

Major decisions included converting `TotalCharges` into a numerical feature, removing unnecessary features, classifying feature types, and planning a Pipeline-based preprocessing strategy to avoid data leakage.

This sprint emphasized engineering decisions rather than model development.

---

## Sprint 03 — Baseline Classification Model

### Goal
Develop the first baseline classification model using a complete machine learning pipeline.

### Completed Tasks

- Prepared feature matrix (X) and target vector (y).
- Encoded the target variable.
- Performed train-test split using stratification.
- Built a preprocessing pipeline with ColumnTransformer.
- Trained a Logistic Regression baseline model.
- Evaluated the model using multiple classification metrics.
- Interpreted the confusion matrix and business implications.

### Key Findings

- Baseline Accuracy: approximately 81%.
- Recall for churned customers remains relatively low.
- The baseline model serves as a reliable benchmark for future experiments.
- Class imbalance may have influenced the model's performance and should be investigated in future sprints.

### Lessons Learned

- Accuracy alone is insufficient for classification problems.
- Precision, Recall, and F1-score provide more meaningful insights.
- Pipeline-based preprocessing effectively prevents data leakage.

---

## Sprint 04 — Decision Tree Baseline

### Goal

Implement the first tree-based classification model and compare its performance against the Logistic Regression baseline.

### Completed Tasks

- Built a Decision Tree classification pipeline.
- Reused the existing preprocessing pipeline.
- Trained the baseline Decision Tree model.
- Evaluated model performance using Accuracy, Precision, Recall, F1-score, Confusion Matrix, and Classification Report.
- Compared Decision Tree with Logistic Regression.

### Key Findings

- The default Decision Tree achieved lower performance than the Logistic Regression baseline.
- Recall decreased noticeably, indicating that more churned customers were missed.
- Model complexity alone does not guarantee better predictive performance.
- Hyperparameter tuning may significantly improve Decision Tree performance in future sprints.

### Lessons Learned

- Tree-based models can overfit when using default settings.
- Model evaluation should consider multiple metrics rather than accuracy alone.
- Baseline comparisons provide valuable references for future optimization.

---

## Sprint 05

This sprint introduced two additional baseline classification algorithms: K-Nearest Neighbors (KNN) and Gaussian Naive Bayes.

Both models were implemented using the existing preprocessing pipeline to ensure a fair comparison with previous models.

Performance evaluation showed that Logistic Regression remained the strongest overall baseline model. KNN provided balanced performance, while Gaussian Naive Bayes achieved excellent Recall at the expense of Precision and Accuracy.

The sprint reinforced the importance of selecting evaluation metrics according to business objectives rather than relying solely on overall Accuracy.