# Changelog

All notable changes to this project will be documented in this file.

---

## Sprint 09 — Hyperparameter Tuning

### Added

- GridSearchCV optimization for Logistic Regression.
- GridSearchCV optimization for Random Forest.
- GridSearchCV optimization for Support Vector Machine.
- Cross-validation based hyperparameter search.
- Final comparison of tuned candidate models.

### Changed

- Updated README project status.
- Updated PROJECT_JOURNAL.
- Added Sprint 09 report.

### Result

Logistic Regression remained the best overall model after hyperparameter optimization.

---

## Sprint 08

### Added

- Baseline model comparison notebook
- Engineering analysis of model performance
- Model ranking
- Candidate model selection
- Technical and business evaluation

### Improved

- Project documentation
- README progress tracking

### Decision

Selected Logistic Regression, Random Forest, and Support Vector Machine for hyperparameter tuning.

<<<<<<< HEAD
### Changed

- Updated hyperparameter tuning candidates.
- Replaced Gaussian Naive Bayes with Random Forest based on engineering analysis and overall model suitability.

=======
>>>>>>> 93476cbc7be3de91c7797db8bb3edb1df0192764
---

## Sprint 07 - Support Vector Machine Baseline

### Added
- Implemented baseline Support Vector Machine (SVM) classifier
- Added SVM pipeline using the shared preprocessing pipeline
- Evaluated SVM using Accuracy, Precision, Recall, F1-score, Confusion Matrix, and Classification Report
- Compared SVM against all previously implemented baseline models
- Documented research questions and theoretical background for Support Vector Machine
- Updated project documentation and README

### Findings
- SVM achieved competitive performance close to Logistic Regression.
- Precision remained similar to Logistic Regression, while Recall decreased.
- Logistic Regression continues to provide the best overall trade-off among baseline models.

---

## [Sprint 06] - Random Forest Baseline

### Added
- Implemented a baseline Random Forest classifier.
- Integrated Random Forest into the existing preprocessing pipeline.
- Evaluated model performance using Accuracy, Precision, Recall, and F1-score.
- Generated Confusion Matrix and Classification Report.
- Compared Random Forest with all previously implemented baseline models.

### Findings
- Random Forest outperformed the default Decision Tree.
- Logistic Regression remained the strongest baseline model.
- Default Random Forest favored the majority class, resulting in lower Recall.
- Hyperparameter tuning will be explored in a future sprint.

---

## Sprint 05 - K-Nearest Neighbors & Gaussian Naive Bayes

### Added

- Implemented K-Nearest Neighbors (KNN) classification pipeline.
- Implemented Gaussian Naive Bayes classification pipeline.
- Evaluated both models using Accuracy, Precision, Recall, and F1-score.
- Generated confusion matrices and classification reports.
- Compared four baseline classification models:
  - Logistic Regression
  - Decision Tree
  - K-Nearest Neighbors
  - Gaussian Naive Bayes

### Insights

- Logistic Regression remained the strongest overall baseline model.
- Gaussian Naive Bayes achieved the highest Recall while producing many false positives.
- KNN outperformed the default Decision Tree baseline.
- Model evaluation emphasized business-oriented metric selection rather than relying solely on Accuracy.

---

## [1.4.0] - 2026-07-27

### Added
- Implemented the baseline Decision Tree classifier.
- Built a complete Scikit-learn Pipeline for Decision Tree.
- Evaluated the model using multiple classification metrics.
- Compared Decision Tree against the Logistic Regression baseline.

### Documentation
- Added Sprint 04 report.
- Updated project documentation.

---

## [1.3.0] - 2026-07-27

### Added
- Implemented the first baseline classification model using Logistic Regression.
- Built an end-to-end Scikit-learn Pipeline.
- Integrated preprocessing with ColumnTransformer.
- Performed train-test split with stratification.
- Evaluated the model using Accuracy, Precision, Recall, F1-score, Confusion Matrix, and Classification Report.

### Documentation
- Added Sprint 03 report.
- Updated project documentation.

---

## [0.2.0] - Sprint 02

### Added

- Data Cleaning notebook
- Feature Preprocessing notebook
- Feature classification documentation
- Preprocessing strategy documentation

### Changed

- Converted `TotalCharges` to numeric.
- Removed `customerID`.
- Saved cleaned dataset.

### Engineering

- Designed Pipeline-based preprocessing workflow.
- Prevented data leakage by postponing encoding and scaling until model training.

---

## v0.2.0 — Sprint 01 Completed

### Added

- Business problem definition
- Initial project documentation
- Dataset exploration notebook
- Exploratory Data Analysis (EDA)
- Numerical feature analysis
- Categorical feature analysis
- Initial business insights
- Correlation analysis
- Data quality investigation
- Sprint documentation

### Identified

- Hidden blank-string values within the `TotalCharges` feature
- Several features with strong relationships to customer churn

### Planned

- Data Cleaning
- Feature Engineering
- Preprocessing Pipeline

---


