# Team Guide

## Development Philosophy

This project follows an incremental Sprint-based development methodology inspired by real-world machine learning engineering workflows.

Each Sprint focuses on a single engineering objective while maintaining reproducibility, documentation quality, and version control throughout the project lifecycle.

---

# Sprint Workflow

Each Sprint should follow the same development cycle:

1. Research & Planning
2. Implementation
3. Model Evaluation
4. Engineering Analysis
5. Documentation
6. Deployment Validation (when applicable)
7. Git Commit & Push

---

# Coding Standards

- Follow PEP 8 guidelines.
- Use descriptive and meaningful variable names.
- Prefer reusable functions over duplicated code.
- Keep notebooks clean and organized.
- Avoid unnecessary code repetition.
- Build reusable preprocessing pipelines whenever possible.
- Use a fixed `random_state` to ensure reproducibility.
- Keep baseline models simple unless the Sprint explicitly focuses on optimization.

---

# Documentation Rules

Every completed Sprint must update the following files:

- README.md
- PROJECT_JOURNAL.md
- CHANGELOG.md
- sprint_xx.md

Documentation should include:

- Sprint Goal
- Work Completed
- Key Findings
- Lessons Learned
- Next Steps (when applicable)
- Engineering Decisions

---

# Model Development Rules

When implementing machine learning models:

- Keep baseline models as close to default settings as possible.
- Modify only the parameters required for reproducibility (e.g., `random_state`).
- Use the shared preprocessing pipeline across all models.
- Ensure that all models are evaluated using the same train/test split for fair comparison.
- Compare models using multiple evaluation metrics rather than Accuracy alone.
- Always save the complete preprocessing pipeline together with the trained model.
- Never fit preprocessing on the entire dataset before train/test split.

---

# Evaluation Strategy

Each classification model should be evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Classification Report
- ROC-AUC
- Precision-Recall Curve
- Threshold Analysis

Business objectives should always be considered before selecting the final model.

---

# Git Workflow

Each Sprint should conclude with:

- Documentation updates
- Git commit
- Git push

Commit messages should clearly describe the completed Sprint.

Example:

```
Sprint 03: Implement Logistic Regression baseline
Sprint 04: Add Decision Tree baseline
Sprint 05: Implement KNN and Gaussian Naive Bayes
```

Every major milestone should be tagged with a GitHub Release.

---

# Project Principles

Throughout the project we aim to:

- Maintain reproducible experiments.
- Keep preprocessing consistent across all models.
- Compare models fairly.
- Prioritize business objectives over isolated performance metrics.
- Document every important engineering decision.
- Explain model predictions whenever possible.
- Separate training code from inference code.

---

# Deployment Rules

- Load the trained model only once at application startup.
- Store deployment configuration separately from the trained model.
- Validate all incoming requests using Pydantic.
- Never retrain the model inside the API.
- Always return prediction probabilities together with the final prediction.

# Future Engineering Roadmap

Future projects may additionally include:

- Docker
- Model Monitoring
- Concept Drift Detection
- Automated Retraining
- CI/CD
- Cloud Deployment