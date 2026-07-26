# Sprint 01 — Business Understanding & Exploratory Data Analysis

**Status:** ✅ Completed

**Duration:** Sprint 01

---

# Sprint Goal

The primary objective of this sprint was to understand the business problem, explore the dataset, assess data quality, and identify the initial factors associated with customer churn.

---

# Tasks Completed

- Established the business objective of the project.
- Explored the dataset structure.
- Identified numerical and categorical features.
- Investigated the target variable distribution.
- Performed Exploratory Data Analysis (EDA).
- Analyzed numerical feature distributions using histograms and boxplots.
- Analyzed categorical features using count plots and contingency tables.
- Generated a correlation matrix for numerical features.
- Investigated hidden data quality issues.
- Documented business insights.

---

# Major Findings

### Dataset

- Number of samples: **7,043**
- Number of features: **20**
- Target variable: **Churn**

### Business Insights

- Month-to-month contracts exhibit the highest churn rate.
- Fiber optic customers tend to churn more frequently.
- Customers without Online Security or Technical Support are more likely to leave the company.
- Customers with shorter tenure have higher churn rates.
- Gender and MultipleLines show relatively weak relationships with churn.

---

# Data Quality Assessment

During the investigation of the dataset, one important issue was identified.

The `TotalCharges` feature was loaded as an object rather than a numeric variable.

Further inspection revealed that the column contains blank string values (" "), preventing Pandas from automatically converting the feature to a numeric data type.

This issue will be addressed during the preprocessing stage.

---

# Engineering Decisions

The following decisions were made during this sprint:

- `customerID` will not be used for model training.
- `TotalCharges` will be converted to a numeric feature after handling blank values.
- Preprocessing will be implemented using reusable Scikit-learn Pipelines.
- Feature engineering will begin after completing data cleaning.

---

# Challenges

- Identifying the cause of the unexpected data type of `TotalCharges`.
- Distinguishing between actual missing values and hidden blank-string values.

---

# Lessons Learned

This sprint reinforced the importance of understanding the dataset before building predictive models.

Exploratory analysis not only revealed useful business insights but also uncovered hidden data quality issues that must be resolved before model development.

---

# Deliverables

- Dataset exploration notebook
- Initial EDA notebook
- Correlation analysis
- Business insights report
- Updated README
- Updated PROJECT_JOURNAL
- Updated CHANGELOG

---

## Sprint Retrospective

### What went well?

- Successfully completed all planned tasks.
- Identified an important hidden data quality issue.
- Generated meaningful business insights.

### What could be improved?

- Improve visualization consistency.
- Reduce repetitive analysis for low-impact features.

### Confidence Level

⭐⭐⭐⭐⭐ (5/5)

---

# Next Sprint

Sprint 02 — Data Cleaning & Preprocessing

Planned tasks:

- Handle missing values
- Convert data types
- Clean `TotalCharges`
- Remove unnecessary features
- Build preprocessing pipeline
- Save cleaned dataset