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
- 100K<n<1M
---

# 📊 Lead.AI Fraud Detection Dataset v2

### 100,000-Row Extended Synthetic Benchmark — 21 Features, Production-Scale Training Data

[![Train on this data](https://img.shields.io/badge/Ready--to--use%20Model-Fraud%20Detection%20Model-FF6B35?style=for-the-badge)](https://huggingface.co/arun-gharami/lead-ai-fraud-detection-model)
[![Smaller version](https://img.shields.io/badge/Smaller%20Version-Dataset%20v1%20%285K%29-green?style=for-the-badge)](https://huggingface.co/datasets/arun-gharami/lead-ai-fraud-detection-dataset)

> Published by [Lead.AI Labs](https://www.lead-ai.us) · Author: [Arun Kumar Gharami](https://huggingface.co/arun-gharami)

---

## What This Dataset Is For

The most complete open synthetic fraud detection dataset in the Lead.AI Labs portfolio —
100,000 transactions, 21 features, and realistic behavioral signals including transaction
type, geographic region, day-of-week patterns, and individual customer risk scores.

Built for:
- **Training production-scale fraud models** that need enough data to learn edge cases
- **XAI / SHAP research at scale** — large enough for statistically meaningful attribution
- **Imbalanced learning experiments** — SMOTE, threshold tuning, class weighting
- **Gradient boosting and deep learning** benchmarks on financial tabular data
- **Research publication** — cite this dataset and train reproducible models

> ⚠️ **Synthetic data.** No real customers, no real transactions, no PII.
> Safe to use, share, and publish without data governance overhead.

---

## Dataset at a Glance

| Property | Value |
|----------|-------|
| Rows | 100,000 |
| Features | 21 |
| Target | `risk_label` (0 = normal, 1 = fraud) |
| Format | Parquet |
| License | Apache 2.0 |
| Split | train (100,000 rows) |

---

## What's New vs v1 (5K rows, 14 features)

| Addition | Why it matters |
|----------|---------------|
| 20× more rows (100K) | Enough data for deep learning, gradient boosting, ensemble methods |
| `transaction_type` | ATM / POS / online / card-present — critical fraud signal |
| `transaction_day_of_week` + `is_weekend` | Temporal fraud pattern detection |
| `geo_location_region` | Regional fraud clustering |
| `customer_risk_score` | Pre-computed customer-level risk aggregation |
| `customer_total_transactions_30d` | Velocity at the customer level, not just session |
| Wearable device type | More realistic device diversity |

---

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| `transaction_id` | string | Unique transaction ID |
| `customer_id` | string | Unique customer ID |
| `transaction_amount` | float | Transaction value |
| `transaction_hour` | int | Hour of day (0–23) |
| `transaction_day_of_week` | int | 0 = Monday … 6 = Sunday |
| `is_weekend` | int | 1 = weekend |
| `account_age_days` | int | Days since account creation |
| `previous_chargebacks` | int | Historical chargeback count |
| `merchant_category` | string | gambling / travel / fuel / luxury / electronics / digital subscriptions / etc. |
| `transaction_country` | string | US / CA / UK / AU / etc. |
| `geo_location_region` | string | North America / Europe / Asia-Pacific / etc. |
| `device_type` | string | mobile / desktop / tablet / wearable |
| `transaction_type` | string | online / pos / atm_withdrawal / card_present_moto |
| `is_international` | int | 1 = international |
| `is_high_risk_merchant_category` | int | 1 = high-risk merchant |
| `customer_total_transactions_30d` | int | Customer's 30-day transaction count |
| `customer_risk_score` | float | Aggregated customer risk (0.0–1.0) |
| `avg_transaction_amount_30d_customer` | float | Customer's 30-day average amount |
| `transaction_velocity_1h` | int | Transactions in last 1 hour |
| `transaction_velocity_24h` | int | Transactions in last 24 hours |
| `risk_label` | int | **Target** — 0 = normal, 1 = fraud |

---

## Load in 3 Lines

```python
from datasets import load_dataset

ds = load_dataset("arun-gharami/lead-ai-fraud-detection-dataset-v2")
df = ds["train"].to_pandas()
print(df.shape)  # (100000, 21)
```

### With pandas
```python
import pandas as pd

df = pd.read_parquet(
    "hf://datasets/arun-gharami/lead-ai-fraud-detection-dataset-v2/data/train-00000-of-00001.parquet"
)
print(df["risk_label"].value_counts(normalize=True))
```

### Fraud rate by merchant category (DuckDB)
```python
import duckdb

duckdb.query("""
    SELECT
        merchant_category,
        COUNT(*) as total,
        SUM(risk_label) as fraud_count,
        ROUND(AVG(risk_label) * 100, 2) as fraud_rate_pct
    FROM read_parquet('hf://datasets/arun-gharami/lead-ai-fraud-detection-dataset-v2/data/train-00000-of-00001.parquet')
    GROUP BY merchant_category
    ORDER BY fraud_rate_pct DESC
""").df()
```

---

## Quick XAI Example (SHAP on This Dataset)

```python
import pandas as pd
import shap
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split

df = pd.read_parquet("hf://datasets/arun-gharami/lead-ai-fraud-detection-dataset-v2/data/train-00000-of-00001.parquet")

features = ["transaction_amount","transaction_hour","account_age_days",
            "previous_chargebacks","transaction_velocity_1h",
            "transaction_velocity_24h","is_international",
            "is_high_risk_merchant_category","customer_risk_score"]

X = df[features]
y = df["risk_label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)
model = GradientBoostingClassifier().fit(X_train, y_train)

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values, X_test)
```

---

## Need a Smaller Version?

For quick prototyping or course projects, use
**[Dataset v1 → 5K rows, 14 features](https://huggingface.co/datasets/arun-gharami/lead-ai-fraud-detection-dataset)**
— loads faster, easier to inspect.

---

## Bias & Fairness Note

Synthetically generated. Geographic, device, and merchant category features may encode
assumptions that don't reflect real fraud distributions. Audit for proxy discrimination
before training models intended for deployment affecting real individuals.

---

## Privacy

No PII. All IDs, amounts, and behavioral features are synthetically generated.

---

## Citation

```bibtex
@misc{gharami2024frauddatasetv2,
  author       = {Arun Kumar Gharami},
  title        = {Lead.AI Fraud Detection Dataset v2: 100K Synthetic Benchmark for XAI and Fraud Detection Research},
  year         = {2024},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/arun-gharami/lead-ai-fraud-detection-dataset-v2}}
}
```

---

*Lead.AI Labs — Trustworthy AI Systems for Practical Business Intelligence*  
[lead-ai.us](https://www.lead-ai.us) · [LinkedIn](https://www.linkedin.com/in/arunkgharami) · [GitHub](https://github.com/Arungharami)
