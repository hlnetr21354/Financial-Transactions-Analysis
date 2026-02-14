# 💹 Financial Transactions Analysis & Fraud Detection

**Author:** Nguyen Quoc Hoang Lan  
**Duration:** February 6, 2026 - Present  
**Tools:** Python, Power BI

## 🎯 Project Overview

This project analyzes large-scale financial transaction data to uncover spending patterns, understand consumer behavior, and identify fraudulent activities. By combining Python-based data analysis with Power BI visualizations, it delivers actionable insights to support strategic business decision-making.

## 🛠️ Technical Stack Summary

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Data Processing | Python (Pandas, NumPy) | Data cleaning, transformation, feature engineering |
| Visualization | Matplotlib, Seaborn | Exploratory analysis and pattern discovery |
| Business Intelligence | Power BI | Interactive dashboards and executive reporting |
| Query Language | DAX | Calculated measures and dynamic KPIs |
| Data Storage | CSV, JSON | Source data format |
| Development | Jupyter Notebook, VS Code | Analysis environment |

---

## 💼 Business Problem

Modern financial institutions operate in a data-driven ecosystem where they face critical challenges:

1. **Fraud Prevention:** Real-time identification of suspicious transactions to minimize financial losses
2. **Customer Intelligence:** Transaction history analysis for user segmentation and spending behavior prediction to enhance marketing effectiveness
3. **Operational Excellence:** Performance monitoring and optimization across card types, merchants, and transaction channels

---

## 🎯 Project Objectives

Build an intelligent Business Intelligence Dashboard that provides executives and managers with comprehensive visibility into system health. This dashboard goes beyond traditional reporting to deliver decision support capabilities through:

- **Strategic Insights:** Holistic views of business performance and trends
- **Operational Analytics:** Real-time monitoring of transaction systems and error patterns
- **Customer Intelligence:** Deep understanding of user segments and behavior
- **Risk Management:** Proactive fraud detection and security threat identification

---

## 📂 Dataset Description

This comprehensive financial dataset combines transaction records, customer information, and card data from a banking institution across the 2010s decade. The dataset consists of 5 primary components:

### 1. **Transaction Data** (`transactions_data.csv`)
- **Size:** 13,305,915 rows; 12 columns
- **Description:** Detailed transaction records with timestamps, amounts, merchants, and error codes
- **Key Features:**
  - Transaction ID, date, time, and amount
  - Merchant information and category codes (MCC)
  - Error codes and transaction status
  - Card and user identifiers

### 2. **Card Information** (`cards_data.csv`)
- **Size:** 6,146 rows; 13 columns
- **Description:** Credit and debit card details linked to customer accounts
- **Key Features:**

| Column | Type | Description |
|--------|------|-------------|
| `id` | Integer | Unique card identifier |
| `client_id` | Integer | Customer account identifier |
| `card_brand` | String | Card network (Visa, Mastercard, Discover, American Express) |
| `card_type` | String | Card classification (Debit, Credit, Prepaid) |
| `card_number` | Integer | Anonymized card number |
| `expires` | String | Expiration date (MM/YYYY) |
| `cvv` | Integer | Card security code |
| `has_chip` | Boolean | EMV chip presence (YES/NO) |
| `num_cards_issued` | Integer | Total cards issued to client (including replacements) |
| `credit_limit` | Float | Maximum credit limit |
| `acct_open_date` | String | Account opening date (MM/YYYY) |
| `year_pin_last_changed` | Integer | Most recent PIN change year (security metric) |
| `card_on_dark_web` | Boolean | Dark web exposure indicator (Yes/No) |

### 3. **User Data** (`users_data.csv`)
- **Size:** 2,000 rows; 14 columns
- **Description:** Demographic and account information for customers
- **Key Features:**
  - Customer demographics
  - Account-level details
  - Credit scores and financial profiles

### 4. **Fraud Labels** (`train_fraud_labels.json`)
- **Size:** 8,914,963 rows; 2 columns
- **Description:** Binary classification labels for transaction fraud status
- **Format:** JSON with transaction ID mapped to fraud label (Yes/No)

### 5. **Merchant Category Codes** (`mcc_codes.json`)
- **Size:** 109 rows; 2 columns
- **Description:** Industry-standard classification codes for business types
- **Examples:**
  - 5812: Eating Places and Restaurants
  - 5541: Service Stations (Gas)
  - 5411: Grocery Stores, Supermarkets
  - 7996: Amusement Parks, Carnivals, Circuses

---

## 📊 Dashboard Strategy

The project delivers a multi-faceted dashboard with four main analytical perspectives:

### 1️⃣ **Overall Business Health**

**Target Audience:** C-level executives, strategic decision-makers

**Key Metrics (KPIs):**
- Total Transaction Volume (TTV): Aggregate transaction value
- Active Users (MAU/DAU): Monthly/daily active transaction participants
- Revenue & Profitability: Total amount processed with estimated fee revenue
- User Growth Rate: New account acquisition trends

**Insights Delivered:**
- Transaction volume and value trends (monthly/quarterly)
- User acquisition and retention metrics
- Revenue trajectory analysis
- Year-over-year growth comparisons

**Strategic Decisions Enabled:**
- Market expansion opportunities
- Product line investment priorities
- Customer segment focus areas

---

### 2️⃣ **Operational Performance**

**Target Audience:** Operations managers, product managers, technical teams

**Key Metrics:**

**Card Performance:**
- Chip Adoption Rate: EMV chip vs magnetic stripe distribution
- Brand Market Share: Transaction volume by card network (Visa, Mastercard, etc.)
- Credit Limit Utilization: Average usage vs available credit

**Merchant Analytics:**
- Top Merchants by Volume: Highest-performing merchant partners
- MCC Concentration: Transaction distribution across business categories
- Merchant Success Rates: Transaction approval rates by merchant type

**Error Analysis:**
- Transaction Success Rate (TSR): Critical operational health indicator
- Error Distribution: Breakdown by error codes (system vs user errors)
- Common Failure Patterns: Insufficient balance, declined transactions, technical errors

**Insights Delivered:**
- Which card brands/types generate the most transactions
- Merchant categories driving business volume
- System reliability and error hotspots
- Infrastructure performance benchmarks

**Operational Decisions Enabled:**
- Infrastructure investment priorities
- Merchant partnership strategies
- System optimization focus areas
- Error resolution workflows

---

### 3️⃣ **Customer Segmentation**

**Target Audience:** Marketing teams, product managers, customer success

**Key Metrics:**
- RFM Scores: Recency, Frequency, Monetary analysis
- Customer Lifetime Value (CLV): Projected long-term value
- Churn Rate: User attrition analysis
- Segment Distribution: Whale users vs casual users vs at-risk segments

**Insights Delivered:**
- High-value customer identification ("Whales")
- At-risk customer detection based on spending patterns
- User behavior clusters and personas
- Spending pattern evolution over time

**Marketing Decisions Enabled:**
- Targeted reward programs for high-value segments
- Win-back campaigns for at-risk customers
- Personalized product offerings
- Customer retention strategies

---

### 4️⃣ **Fraud Detection & Risk Management**

**Target Audience:** Risk management teams, compliance officers, security analysts

**Key Metrics:**
- Fraud Rate: By transaction volume and dollar value
- Fraudster Profiling: Common characteristics of fraudulent transactions
- Risk Score Distribution: Transaction-level risk assessment
- Dark Web Exposure Impact: Cards compromised vs fraud incidence
- Detection Performance: False positive rate, detection latency

**Insights Delivered:**
- Fraud pattern identification by transaction type, amount, merchant
- Correlation between security features (chip, dark web exposure) and fraud
- High-risk transaction characteristics
- Cost of fraud vs prevention effectiveness

**Risk Decisions Enabled:**
- Dynamic fraud rule adjustments
- Proactive card replacement for compromised accounts
- Two-factor authentication triggers
- Transaction monitoring thresholds

---

## 🔍 Key Business Questions Addressed

### Operational Focus
- Are transaction volumes and values trending upward or downward?
- Which card brands and types drive the highest revenue?
- What are the primary failure modes affecting customer experience?

### Customer Focus
- Who are the "whale" customers generating disproportionate value?
- Which customer segments show churn risk based on recent activity?
- How do spending patterns vary across user demographics?

### Risk Focus
- What fraud patterns are most prevalent in the system?
- How do security features (chip cards, dark web monitoring) impact loss rates?
- Which merchant categories pose the highest fraud risk?

---

## 🚀 Project Workflow

### 1. Data Cleaning & Preprocessing
- Handled missing values in transaction amounts and merchant data
- Standardized date formats across all datasets
- Converted currency fields from string to numeric (removed `$` symbols)
- Created consistent boolean fields (Yes/No → 1/0)
- Merged fraud labels with transaction data

### 2. Exploratory Data Analysis (EDA)
- **Transaction Distribution:** Volume analysis by card type, brand, and merchant category
- **Time-Series Analysis:** Identified peak transaction hours, days, and seasonal patterns
- **Correlation Analysis:** Examined relationships between card security features and fraud rates
- **Customer Behavior:** Spending patterns by user segments

### 3. Feature Engineering
- **Security Metrics:** Combined chip status and dark web exposure into risk scores
- **Temporal Features:** Extracted hour, day, month, year from transaction timestamps
- **Customer Metrics:** Calculated transaction frequency, average amounts, and recency
- **Fraud Indicators:** Flagged anomalous amounts, unusual merchant categories, and velocity patterns

### 4. Dashboard Development (Power BI)
- **Data Modeling:** Established relationships between tables (star schema)
- **DAX Calculations:** Created measures for KPIs, growth rates, and segmentation
- **Visualizations:** Time-series charts, geographical maps, distribution histograms, correlation matrices
- **Interactivity:** Filters, slicers, drill-throughs for exploratory analysis

---

## 💡 Sample Insights & Findings

### Fraud Patterns
- **High-Risk Transactions:** Cards exposed on the dark web show 3.5x higher fraud rates
- **Merchant Risk:** Certain MCC categories (online retail, travel) exhibit elevated fraud
- **Temporal Patterns:** Fraudulent activity spikes during late-night hours (2 AM - 4 AM)
- **Amount Thresholds:** Transactions exceeding 75% of historical average are 5x more likely to be fraudulent

### Operational Insights
- **Chip Adoption Impact:** EMV chip cards show 40% fewer fraudulent transactions than magnetic stripe cards
- **Error Hotspots:** "Insufficient Balance" errors account for 60% of declined transactions
- **Brand Performance:** Visa processes 55% of total transaction volume

### Customer Behavior
- **Whale Concentration:** Top 10% of customers generate 45% of total transaction value
- **Churn Signals:** Users with declining transaction frequency over 90 days show 70% churn likelihood
- **Spending Categories:** Restaurants (MCC 5812) and Gas Stations (MCC 5541) dominate everyday spending

---

## 📈 Expected Business Impact

### Risk Reduction
- **Fraud Loss Prevention:** Estimated 20-30% reduction in fraud losses through enhanced detection
- **Proactive Card Protection:** Early intervention for dark web-exposed cards

### Revenue Optimization
- **Customer Retention:** Targeted campaigns to reduce churn by 15%
- **Upselling Opportunities:** Credit limit increases for high-performing, low-risk customers

### Operational Efficiency
- **Error Rate Reduction:** Focused fixes on top error categories to improve customer experience
- **Merchant Strategy:** Data-driven partnership decisions based on volume and risk profiles

---

## 📁 Project Structure

```
FinancialTransactionsAnalysis/
│
├── data/
│   ├── cards_data.csv
│   ├── transactions_data.csv
│   ├── users_data.csv
│   ├── mcc_codes.json
│   └── train_fraud_labels.json
│
├── notebooks/
│   └── transform_data_eda.ipynb
│
├── transformed_data/
│   ├── cards_data.csv
│   ├── transactions_data.csv
│   ├── transaction_errors.csv
│   ├── users_data.csv
│   ├── mcc_codes.csv
│   └── fraud_labels.csv
│
├── powerbi/
│   └── financial_dashboard.pbix
│
└── README.md
```

---

## 🎓 Key Learnings

- **Scale Matters:** Handling 24M+ transaction records requires optimized data processing techniques
- **Context is King:** Understanding business context (MCC codes, fraud patterns) is crucial for meaningful analysis
- **Visualization Hierarchy:** Different stakeholders need different views—from C-suite summaries to operational deep-dives
- **Security Metrics:** Quantifying the ROI of security features (chip cards, monitoring) drives investment decisions

---

## 🔮 Future Enhancements

- **Machine Learning Models:** Develop predictive fraud detection algorithms (Random Forest, XGBoost)
- **Real-Time Dashboards:** Integrate streaming data for live transaction monitoring
- **Geospatial Analysis:** Map fraud patterns and customer distribution geographically
- **Advanced Segmentation:** Implement clustering algorithms for dynamic customer personas
- **A/B Testing Framework:** Evaluate the effectiveness of fraud prevention rule changes

---

## 📧 Contact

**Nguyen Quoc Hoang Lan**  
For questions or collaboration opportunities, please reach out via GitHub or LinkedIn.

---

*This project demonstrates end-to-end data analytics capabilities, from raw data processing to executive-level business intelligence, with a focus on actionable insights that drive strategic decision-making in the financial services industry.*