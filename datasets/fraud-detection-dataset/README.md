---
license: apache-2.0
language:
- en
task_categories:
- tabular-classification
tags:
- fraud-detection
- tabular
- financial
- trustworthy-ai
- responsible-ai
- explainable-ai
- xai
- synthetic-data
- lead-ai-labs
size_categories:
- 1K<n<10K
---

# 📊 Lead.AI Fraud Detection Dataset

### 5,000-Row Synthetic Tabular Benchmark — Ready to Train, Ready to Publish

[![Upgrade to 100K rows](https://img.shields.io/badge/Need%20More%20Data%3F-Dataset%20v2%20%28100K%29-green?style=for-the-badge)](https://huggingface.co/datasets/arun-gharami/lead-ai-fraud-detection-dataset-v2)
[![Train a model on this data](https://img.shields.io/badge/Ready--to--use%20Model-Fraud%20Shield-FF6B35?style=for-the-badge)](https://huggingface.co/arun-gharami/lead-ai-fraud-shield)

> Published by [Lead.AI Labs](https://www.lead-ai.us) · Author: [Arun Kumar Gharami](https://huggingface.co/arun-gharami)

---

## What This Dataset Is For

A clean, Parquet-formatted, immediately loadable synthetic fraud detection dataset built
for researchers, ML engineers, and course instructors who need realistic tabular financial
data **without the legal complexity of real transaction data**.

Use it to:
- Build and benchmark fraud classifiers in hours, not weeks
- Run XAI / SHAP experiments on financial features
- Teach imbalanced classification in courses or workshops
- Prototype a fraud detection proof-of-concept for a client demo

> ⚠️ **Synthetic data.** No real customers, no real transactions, no PII.
> Safe to use, share, and publish.

---

## Dataset at a Glance

| Property | Value |
|----------|-------|
| Rows | 5,000 |
| Features | 14 |
| Target | `risk_label` (0 = normal, 1 = fraud) |
| Format | Parquet |
| License | Apache 2.0 |
| Split | train (5,000 rows) |

---

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| `transaction_id` | string | Unique transaction identifier |
| `customer_id` | string | Unique customer identifier |
| `transaction_amount` | float | Transaction value |
| `transaction_hour` | int | Hour of day (0–23) |
| `account_age_days` | int | Days since account creation |
| `previous_chargebacks` | int | Historical chargeback count |
| `merchant_category` | string | online_services / grocery / electronics / travel / fuel / fashion / restaurant |
| `transaction_country` | string | US / UK / CA / AU / IN |
| `device_type` | string | mobile / desktop / tablet |
| `is_international` | int | 1 = international transaction |
| `is_high_risk_merchant` | int | 1 = high-risk merchant |
| `transaction_velocity_1h` | int | Transactions in last 1 hour |
| `transaction_velocity_24h` | int | Transactions in last 24 hours |
| `avg_transaction_amount_30d` | float | 30-day average transaction amount |
| `risk_label` | int | **Target** — 0 = normal, 1 = fraud |

---

## Load in 3 Lines

```python
from datasets import load_dataset

ds = load_dataset("arun-gharami/lead-ai-fraud-detection-dataset")
df = ds["train"].to_pandas()
```

### With pandas directly
```python
import pandas as pd

df = pd.read_parquet(
    "hf://datasets/arun-gharami/lead-ai-fraud-detection-dataset/data/train-00000-of-00001.parquet"
)
print(df["risk_label"].value_counts())
```

### With DuckDB (fast SQL on Parquet)
```python
import duckdb

duckdb.query("""
    SELECT risk_label, COUNT(*) as n, ROUND(AVG(transaction_amount), 2) as avg_amount
    FROM read_parquet('hf://datasets/arun-gharami/lead-ai-fraud-detection-dataset/data/train-00000-of-00001.parquet')
    GROUP BY risk_label
""").df()
```

---

## Ready-to-Use Model Trained on This Data

Don't want to train your own? The [Lead.AI Fraud Shield](https://huggingface.co/arun-gharami/lead-ai-fraud-shield)
is already trained and ready to load:

```python
import joblib, pandas as pd
model = joblib.load("model/model.joblib")   # from lead-ai-fraud-shield repo
```

---

## Need More Data?

This dataset has 5K rows and 14 features — good for fast prototyping and course projects.

For production model training or research publication, use
**[Dataset v2 → 100K rows, 21 features](https://huggingface.co/datasets/arun-gharami/lead-ai-fraud-detection-dataset-v2)**
which adds transaction type, day-of-week, geographic region, customer risk score, and more.

---

## Bias & Fairness Note

Synthetically generated. Country and device features may encode assumptions that don't
reflect real fraud distributions. Audit for proxy discrimination before using a model
trained here in any context involving real individuals.

---

## Privacy

No PII. All IDs, amounts, and behavioral features are synthetically generated.

---

## Citation

```bibtex
@misc{gharami2024frauddataset,
  author       = {Arun Kumar Gharami},
  title        = {Lead.AI Fraud Detection Dataset: Synthetic Tabular Benchmark for XAI Research},
  year         = {2024},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/arun-gharami/lead-ai-fraud-detection-dataset}}
}
```

---

*Lead.AI Labs — Trustworthy AI Systems for Practical Business Intelligence*  
[lead-ai.us](https://www.lead-ai.us) · [LinkedIn](https://www.linkedin.com/in/arunkgharami) · [GitHub](https://github.com/Arungharami)
