# 📊 Trader Performance vs Bitcoin Market Sentiment

## 📌 Project Overview

This project analyzes the relationship between trader performance and Bitcoin market sentiment (Fear & Greed Index).

The objective is to understand how trader behavior and profitability change during different sentiment regimes and to generate strategic insights based on data.

---

## 🎯 Objectives

- Analyze trader profitability under Fear vs Greed conditions
- Compare behavioral patterns across sentiment regimes
- Identify risk exposure trends
- Provide strategy recommendations
- (Bonus) Perform basic predictive modeling

---

## 📂 Dataset Description

### 1️⃣ Bitcoin Sentiment Data
Contains:
- timestamp
- value (Fear & Greed Index)
- classification (Fear / Greed / Neutral)
- date

### 2️⃣ Trader Data
Contains:
- Account
- Coin
- Execution Price
- Size Tokens
- Size USD
- Side
- Timestamp IST
- Closed PnL
- Fee
- Direction
- Trade ID
- etc.

---

## ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## 🔍 Methodology

### Step 1: Data Cleaning
- Checked missing values
- Removed duplicates
- Converted timestamps to datetime format
- Extracted date column for merging

### Step 2: Data Merging
Merged trader data with sentiment data using date.

### Step 3: Analysis Performed
- Average PnL by sentiment regime
- Trade frequency by sentiment
- Volatility comparison
- Risk exposure comparison
- Behavioral segmentation

### Step 4: Insights Generation
Compared performance during:
- Fear periods
- Greed periods
- Neutral periods

---

## 📊 Key Insights

- Traders tend to trade more frequently during Greed periods.
- Higher volatility observed during Greed regimes.
- Fear periods show lower participation but reduced risk exposure.
- Large position traders face higher drawdowns during Fear regimes.
- Consistent traders perform better across all regimes.

---

## 💡 Strategy Recommendations

- Reduce position size during Fear regimes.
- Increase activity selectively during Greed but manage volatility.
- Use sentiment as a risk-adjustment indicator.
- Diversify strategies across sentiment cycles.

---

## ▶️ How to Run the Project

1. Install required libraries:

   
2. Place datasets in the same directory as the script.

3. Run:

---

## 📈 Future Improvements

- Add time-series predictive modeling
- Apply advanced ML classification models
- Perform regime-switching analysis
- Create interactive dashboard (Streamlit / Power BI)

---

## 👩‍💻 Author

Vaishali Rawat  
Junior Data Science Enthusiast

