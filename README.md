# 💹 Financial Transactions Analysis & Fraud Detection
=====

This project focuses on analyzing large-scale financial transaction data to uncover spending patterns, categorize consumer behavior, and identify fraudulent activities. The workflow includes:
1. **Exploratory Data Analysis (EDA):** Clean, transform, and explore transaction data using **Python**.
2. **Data Visualization:** Create interactive dashboards in **Power BI** to visualize key metrics and trends.
3. **Actionable Insights:** Deliver data-driven recommendations to support business decision-making. 

====
* Author: Nguyen Quoc Hoang Lan
* Duration: Febuarary 6th - 
* Tools used: Python, Power BI

## ❓ Business Problem
In the modern financial ecosystem, institutions face two major challenges:
1.  **Fraud Prevention:** Identifying suspicious transactions in real-time to minimize financial loss.
2.  **Customer Understanding:** Analyzing transaction history to segment users and predict future spending habits for better marketing strategies.

## 🛠 Tech Stack
* **Language:** Python
* **Data Manipulation:** `Pandas`, `NumPy`
* **Visualization:** `Matplotlib`, `Seaborn`, `Plotly`
* **Machine Learning:** `Scikit-Learn`, `XGBoost`, `Imbalanced-learn`
* **Environment:** Jupyter Notebook / VS Code

## 📂 Dataset Description
The dataset contains historical transaction records with the following key features:
| Feature | Description |
| :--- | :--- |
| `step` | Maps a unit of time in the real world (e.g., 1 step is 1 hour). |
| `type` | Type of transaction (CASH-IN, CASH-OUT, DEBIT, PAYMENT, TRANSFER). |
| `amount` | The value of the transaction in local currency. |
| `oldbalanceOrg` | Initial balance before the transaction. |
| `newbalanceOrig` | New balance after the transaction. |
| `isFraud` | Binary label (1 if fraudulent, 0 otherwise). |

## 🚀 Project Roadmap

### 1. Data Cleaning & Preprocessing
* Handled missing values and outliers in transaction amounts.
* Performed feature scaling on high-variance numerical data.
* Encoded categorical variables (Transaction Types) using One-Hot Encoding.

### 2. Exploratory Data Analysis (EDA)
* **Transaction Distribution:** Visualized the volume of different transaction types.
* **Time-Series Analysis:** Identified peak hours/days for transactions and potential fraud windows.
* **Correlation Heatmaps:** Analyzed relationships between balance changes and fraud likelihood.

### 3. Feature Engineering
* Created new metrics: `Balance_Error` (checking if math adds up) and `Transaction_Frequency`.
* Derived time-based features from timestamps.

### 4. Model Development & Evaluation
* Addressed **Class Imbalance** using **SMOTE** (Synthetic Minority Over-sampling Technique).
* Trained multiple classifiers: **Random Forest**, **Logistic Regression**, and **XGBoost**.
* **Evaluation Metrics:** Focused on **Precision-Recall AUC** and **F1-Score** due to the rarity of fraud cases.

## 📊 Key Insights (Sample)
* **Insight 1:** Over 90% of fraudulent transactions occur via 'TRANSFER' or 'CASH-OUT' methods.
* **Insight 2:** Transactions exceeding 75% of the account's historical average amount are 5x more likely to be flagged.
* **Insight 3:** Fraudulent activities show a specific pattern during late-night hours (2 AM - 4 AM).

## 💻 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/Financial-Transactions-Analysis.git](https://github.com/your-username/Financial-Transactions-Analysis.git)
   cd Financial-Transactions-Analysis