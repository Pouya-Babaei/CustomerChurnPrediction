# Sprint 10 — Model Explainability

---

# Sprint Goal

Understand why the final Logistic Regression model makes its predictions and improve model transparency using multiple explainability techniques.

---

# Objectives

- Analyze Logistic Regression coefficients
- Rank the most influential features
- Visualize positive and negative feature effects
- Apply Permutation Importance
- Explain predictions using SHAP
- Compare global and local explainability
- Interpret model behavior from an engineering perspective

---

# Research Questions

- Why is model explainability important in machine learning projects?
- Is a highly accurate model always useful if we cannot explain its predictions?
- What is the difference between Feature Importance and SHAP values?
- Why are SHAP values considered local explanations while traditional feature importance provides a global explanation?
- How can SHAP help explain individual customer churn predictions?
- How does explainability improve business trust and production readiness?

---

# Practical Tasks

## 1. Logistic Regression Coefficient Analysis

- Extract model coefficients
- Create feature importance table
- Sort by absolute coefficient value

---

## 2. Coefficient Visualization

- Top Positive Features
- Top Negative Features

---

## 3. Permutation Importance

- Compute feature importance on unseen data
- Compare with coefficient-based importance

---

## 4. SHAP Explainability

Generate:

- SHAP Summary Plot
- SHAP Waterfall Plot
- SHAP Force Plot

---

## 5. Engineering Analysis

Interpret:

- Most influential features
- Feature directions
- Global vs Local explanations
- Business implications

---

# Deliverables

- Logistic coefficient table
- Positive coefficient visualization
- Negative coefficient visualization
- Permutation Importance plot
- SHAP Summary Plot
- SHAP Waterfall Plot
- SHAP Force Plot
- Engineering Analysis
- Key Findings
- Sprint Retrospective

---

# Key Results

- Logistic Regression remained fully interpretable.
- Tenure and Contract were identified as the strongest churn indicators.
- SHAP explanations were consistent with Logistic Regression coefficients.
- Global and local explainability provided complementary insights.
- Explainability increased confidence in model deployment decisions.

---

# Sprint Outcome

Status:

✅ Completed

The project now includes both predictive performance evaluation and explainability analysis, making the final model easier to interpret, validate, and communicate to business stakeholders.