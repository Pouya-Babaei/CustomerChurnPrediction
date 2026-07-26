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