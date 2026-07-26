# Changelog

All notable changes to this project will be documented in this file.

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