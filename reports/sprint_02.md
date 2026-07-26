# Sprint 02 — Data Cleaning & Feature Preprocessing

## Sprint Goal

Prepare a clean and consistent dataset for machine learning while designing a reproducible preprocessing strategy.

---

## Tasks Completed

- Investigated data quality issues.
- Converted `TotalCharges` to a numerical feature.
- Identified and handled missing values.
- Removed the `customerID` feature.
- Saved the cleaned dataset.
- Classified all features according to their preprocessing requirements.
- Designed the preprocessing strategy for numerical and categorical variables.
- Documented engineering decisions for future Pipeline implementation.

---

## Key Decisions

- Raw data remains unchanged.
- Cleaned data is stored separately.
- Binary numerical features remain unchanged.
- Encoding and scaling will be implemented inside a Scikit-learn Pipeline.
- No permanently encoded dataset will be created.

---

## Deliverables

- Clean dataset
- Feature classification
- Preprocessing plan
- Engineering documentation

---

## Sprint Outcome

The dataset is now ready for model development.

The preprocessing strategy has been fully designed and documented, enabling the next sprint to focus on building the first baseline classification pipeline.