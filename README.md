# Budget 2024 Text Analysis

This repository contains code and resources for analyzing consumer and producer opinions on the 2024 budget. The analysis includes text preprocessing, sentiment classification, and evaluating the impacts of the budget on various groups.

## Overview

The project involves several key components:
- **Data Generation:** Synthetic data for consumer opinions.
- **Text Normalization:** Preprocessing text data to remove noise and prepare it for analysis.
- **Model Training:** Training a DistilBERT model for sentiment classification.
- **Tokenization:** Converting text data into a format suitable for input to BERT-based models.

## Objectives

### Trend Analysis
- **Objective:** Analyze the evolution of consumer opinions and business reactions over time following the budget announcement.
- **Goal:** Identify patterns or shifts in sentiments by tracking changes on a daily, weekly, or monthly basis.

### Impact Analysis
- **Objective:** Assess how changes in taxation, subsidies, and prices have influenced consumer spending habits and business decisions.
- **Goal:** Determine the economic impact by analyzing consumer spending reports and business activity, such as expansion or reduction in operations.

### Comparative Analysis
- **Objective:** Evaluate the differing impacts of Budget 2024 on various consumer groups (e.g., low-income vs. high-income) and industries (e.g., manufacturing vs. services).
- **Goal:** Compare the effects of the budget to determine which groups and sectors benefit the most and which might face challenges.

## Setup

### Prerequisites
- Python 3.x
- PyTorch
- Hugging Face Transformers
- tqdm
- nltk

### Installation

Clone the repository and install the necessary packages:

```bash
git clone <repository_url>
cd <repository_directory>
pip install -r requirements.txt
