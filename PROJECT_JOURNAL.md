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

---

## Outcome

Logistic Regression remained the strongest baseline while GaussianNB demonstrated the highest Recall.

---

# Sprint 06 — Random Forest Baseline

## Goal

Implement a baseline Random Forest classifier using the shared preprocessing pipeline and compare its performance with all previously implemented baseline models.

---

## Work Completed

- Implemented the Random Forest classifier within the shared preprocessing pipeline.
- Trained the baseline Random Forest model using default hyperparameters.
- Generated predictions on the test dataset.
- Evaluated model performance using multiple classification metrics.
- Compared Random Forest against Logistic Regression, Decision Tree, KNN, and Gaussian Naive Bayes.
- Documented implementation decisions and research findings.

---

## Key Findings

- Random Forest outperformed the single Decision Tree, confirming the benefit of ensemble learning.
- The model achieved higher Accuracy than several baseline models but lower Recall than Logistic Regression.
- Logistic Regression continued to provide the best overall trade-off between Precision, Recall, and F1-score.
- Default Random Forest provides a strong foundation for future hyperparameter tuning.

---

## Lessons Learned

- Ensemble methods generally improve robustness compared to a single Decision Tree.
- More complex models do not necessarily outperform simpler models on every dataset.
- Model selection should consider business objectives rather than Accuracy alone.
- Hyperparameter tuning is essential to fully leverage Random Forest's capabilities.

---

# Sprint 07 — Support Vector Machine Baseline

## Goal

Implement a baseline Support Vector Machine classifier using the existing preprocessing pipeline and compare its performance with all previously implemented baseline models.

---

## Work Completed

- Implemented SVC inside the shared preprocessing pipeline.
- Trained the baseline SVM classifier.
- Generated predictions on the test dataset.
- Evaluated model performance using multiple classification metrics.
- Compared SVM with Logistic Regression, Decision Tree, KNN, Gaussian Naive Bayes, and Random Forest.
- Documented research findings and implementation decisions.

---

## Key Findings

- SVM achieved performance close to Logistic Regression.
- Precision remained almost identical to Logistic Regression.
- Recall decreased, resulting in more False Negatives.
- Logistic Regression remains the strongest baseline model for customer churn prediction.
- Default SVM shows potential for future hyperparameter tuning.

---

## Lessons Learned

- SVM maximizes the decision margin between classes.
- Feature scaling is essential for SVM.
- Kernel functions enable SVM to model non-linear decision boundaries.
- More complex algorithms do not necessarily outperform simpler linear models.

---

# Sprint 08 — Baseline Model Comparison

## Objective

Compare all baseline classification models and identify the most promising candidates for hyperparameter tuning.

## Completed Tasks

- Compared six baseline classifiers.
- Evaluated Accuracy, Precision, Recall, and F1-score.
- Analyzed model trade-offs from both technical and business perspectives.
- Ranked the baseline models.
- Selected candidate models for optimization.

## Key Findings

- Logistic Regression achieved the strongest overall baseline performance.
- Gaussian Naive Bayes produced the highest Recall but with a significant loss in Accuracy and Precision.
- Support Vector Machine delivered competitive results.
- Random Forest remained a promising candidate due to its optimization potential.
- Three candidate models were selected for the next Sprint.

## Next Sprint

Hyperparameter tuning of the selected models.

## Project Decision Update

After the baseline comparison, Gaussian Naive Bayes was removed from the hyperparameter tuning stage.

Although it achieved the highest Recall, its overall trade-off (Accuracy, Precision, and modeling assumptions) made it a less suitable candidate.

The final tuning candidates became:

• Logistic Regression
• Random Forest
• Support Vector Machine

The comparison stage reduced experimentation cost by selecting only the most promising models for further optimization.

---

# Sprint 09 — Hyperparameter Tuning

## Objective

Optimize the strongest baseline models using GridSearchCV and cross-validation.

## Candidate Models

- Logistic Regression
- Random Forest
- Support Vector Machine

## Work Completed

- Defined hyperparameter search spaces for all candidate models.
- Applied GridSearchCV with 5-fold cross-validation.
- Optimized models using Recall as the primary scoring metric.
- Evaluated tuned models on the held-out test dataset.
- Compared cross-validation performance with final test performance.

## Engineering Decisions

- Selected only the strongest baseline models for tuning to reduce unnecessary computational cost.
- Used Recall as the optimization metric because minimizing false negatives is critical for customer churn prediction.
- Kept all preprocessing inside the Pipeline to prevent data leakage during cross-validation.

## Outcome

Hyperparameter tuning produced only minor improvements.

Logistic Regression retained its baseline configuration and remained the strongest overall model.

The results indicate that future improvements are more likely to come from feature engineering, threshold optimization, and explainability rather than increasing model complexity.

---

## Lessons Learned

- Hyperparameter tuning cannot compensate for limited feature information.
- Better features often improve performance more than more complex algorithms.

---

# Sprint 10 — Model Explainability

## Goal

Improve model interpretability by understanding why the Logistic Regression model makes its predictions and identifying the most influential customer features.

---

## Tasks Completed

- Extracted Logistic Regression coefficients
- Ranked features based on coefficient magnitude
- Visualized positive and negative feature effects
- Applied Permutation Importance
- Implemented SHAP explainability
- Generated SHAP Summary Plot
- Generated SHAP Waterfall Plot
- Generated SHAP Force Plot
- Compared global and local explanations
- Documented engineering findings

---

## Outcome

The explainability analysis confirmed that customer tenure, contract type, and internet service are the strongest drivers of churn prediction.

Combining Logistic Regression coefficients, Permutation Importance, and SHAP produced consistent explanations, increasing confidence in the model and making it suitable for business interpretation.

---

## Lessons Learned

- Model interpretability is essential for stakeholder trust.
- SHAP provides both global and local explanations.
- Multiple explainability techniques increase confidence in model behavior.
  
---

## Sprint Status

✅ Completed

---

# Sprint11 — Error Analysis

## Goal

- Analyze prediction errors to understand model weaknesses.
- Error Analysis
- Failure Case Investigation
- Customer Segment Analysis

Deliverables:
- Prediction Analysis Table
- False Positive / False Negative Investigation
- Feature Comparison
- Error Visualizations

Outcome:
The project moved beyond evaluation metrics and identified customer groups responsible for most prediction errors, providing valuable insights for threshold optimization and future model improvements.

---

# Sprint 12 — Threshold Optimization & Deployment Preparation

## Goal

Optimize the classification threshold to maximize business value and prepare the trained model for deployment.

---

## Work Completed

- Evaluated multiple classification thresholds.
- Compared Accuracy, Precision, Recall, and F1 across thresholds.
- Selected the optimal threshold (0.40).
- Generated Threshold vs Precision, Recall, and F1 visualizations.
- Generated ROC Curve.
- Generated Precision–Recall Curve.
- Loaded the saved Logistic Regression pipeline.
- Performed inference on unseen customer data.
- Validated deployment workflow.

---

## Engineering Decisions

- Selected 0.40 as the final operating threshold.
- Prioritized Recall over Precision due to business requirements.
- Reused the saved pipeline to simulate production inference.
- Stored deployment configuration separately from the trained model.

---

## Outcome

Threshold optimization significantly improved the business usefulness of the model without retraining.

The deployment workflow was successfully validated using the saved pipeline.

The project is now production-ready and fully prepared for FastAPI deployment.

---

## Sprint Status

✅ Completed

---

## Lessons Learned

- Threshold optimization can significantly improve business value without retraining the model.
- A complete saved pipeline greatly simplifies deployment.
- Separating configuration (threshold) from the trained model improves maintainability.
- The project is now production-ready and prepared for API deployment.

---

---

# Overall Project Reflection

This project successfully followed an end-to-end machine learning engineering workflow including:

- Business Understanding
- Exploratory Data Analysis
- Data Cleaning
- Feature Engineering
- Model Development
- Hyperparameter Tuning
- Explainability
- Error Analysis
- Threshold Optimization
- Deployment Preparation
- FastAPI Deployment

The project is considered portfolio-ready and serves as a complete demonstration of a production-oriented machine learning pipeline.