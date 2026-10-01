# Credit Card Fraud Prediction — Labs 3 to 6

This project adapts the supplied Lab 3, Lab 4, Lab 5 and Lab 6 pipeline structure to `creditcard.csv`.

- Lab 3: Baseline ML Pipeline
- Lab 4: MLflow Experiment Tracking (local tracking artifact included; install MLflow for full MLflow UI)
- Lab 5: Production Data Pipeline
- Lab 6: Model Registry & Lifecycle

Run from the project root:

```bash
python pipelines/run_lab3_baseline.py
python pipelines/run_lab4_tracking.py
python pipelines/run_lab5_pipeline.py
python pipelines/run_lab6_registry.py
```

Dataset target: `Class` (0 = non-fraud, 1 = fraud). Model: Random Forest with the reference parameters `n_estimators=100`, `max_depth=10`, `random_state=42`, `class_weight='balanced'`.
