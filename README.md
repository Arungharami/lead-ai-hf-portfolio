# Lead.AI Labs — Hugging Face Portfolio

**Trustworthy AI Systems for Practical Business Intelligence**

This repository contains all professional README and model card files for the
[arun-gharami](https://huggingface.co/arun-gharami) Hugging Face profile.

## Structure

```
huggingface-portfolio/
├── profile/
│   └── README.md                          ← HF profile landing page
├── models/
│   ├── fraud-shield/README.md             ← lead-ai-fraud-shield model card
│   ├── customer-predictor/README.md       ← lead-ai-customer-predictor model card
│   ├── review-sentinel/README.md          ← lead-ai-review-sentinel model card
│   └── fraud-detection-model/README.md   ← lead-ai-fraud-detection-model card
├── datasets/
│   ├── fraud-detection-dataset/README.md  ← Dataset v1 (5K rows)
│   └── fraud-detection-dataset-v2/README.md ← Dataset v2 (100K rows)
└── spaces/
    └── fraud-detection-xai-demo/README.md ← XAI Demo Space README
```

## Upload Commands

```bash
export HF_TOKEN=your_token_here

# Profile
hf upload arun-gharami/arun-gharami profile/README.md README.md --token $HF_TOKEN

# Models
hf upload arun-gharami/lead-ai-fraud-shield models/fraud-shield/README.md README.md --token $HF_TOKEN
hf upload arun-gharami/lead-ai-customer-predictor models/customer-predictor/README.md README.md --token $HF_TOKEN
hf upload arun-gharami/lead-ai-review-sentinel models/review-sentinel/README.md README.md --token $HF_TOKEN
hf upload arun-gharami/lead-ai-fraud-detection-model models/fraud-detection-model/README.md README.md --token $HF_TOKEN

# Datasets
hf upload arun-gharami/lead-ai-fraud-detection-dataset datasets/fraud-detection-dataset/README.md README.md --repo-type dataset --token $HF_TOKEN
hf upload arun-gharami/lead-ai-fraud-detection-dataset-v2 datasets/fraud-detection-dataset-v2/README.md README.md --repo-type dataset --token $HF_TOKEN

# Space
hf upload arun-gharami/fraud-detection-xai-demo spaces/fraud-detection-xai-demo/README.md README.md --repo-type space --token $HF_TOKEN
```

## Author

**Arun Kumar Gharami** — [lead-ai.us](https://www.lead-ai.us) · [LinkedIn](https://www.linkedin.com/in/arunkgharami)
