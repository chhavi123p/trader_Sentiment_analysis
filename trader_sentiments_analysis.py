import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

sns.set(style="whitegrid")

print("Loading datasets...\n")

sentiment = pd.read_csv(r"C:\Users\hp\vaishali\bitcoin_sentiment.csv")
trader = pd.read_csv(r"C:\Users\hp\vaishali\historical_data.csv")

print("Sentiment shape:", sentiment.shape)
print("Trader shape:", trader.shape)

# ==========================================================
# CLEAN SENTIMENT DATA
# ==========================================================

# Convert sentiment date
sentiment['date'] = pd.to_datetime(sentiment['date']).dt.date

# Rename classification column properly
sentiment.rename(columns={'classification': 'Classification'}, inplace=True)

# ==========================================================
# CLEAN TRADER DATA
# ==========================================================

# Convert timestamp
# Convert timestamp properly (DD-MM-YYYY format)
trader['Timestamp IST'] = pd.to_datetime(
    trader['Timestamp IST'],
    dayfirst=True
)

trader['date'] = trader['Timestamp IST'].dt.date

# Rename columns for easier use
trader.rename(columns={
    'Account': 'account',
    'Closed PnL': 'closedPnL',
    'Side': 'side'
}, inplace=True)

# ==========================================================
# MERGE DATASETS
# ==========================================================

merged = trader.merge(
    sentiment[['date', 'Classification']],
    on='date',
    how='left'
)

print("\nMerged Shape:", merged.shape)

# ==========================================================
# FEATURE ENGINEERING
# ==========================================================

merged['win'] = merged['closedPnL'] > 0

# Performance by sentiment
print("\nPerformance by Sentiment\n")

performance = merged.groupby('Classification')['closedPnL'].agg(
    ['mean', 'median', 'std', 'count']
)
print(performance)

# Win rate
print("\nWin Rate by Sentiment:")
print(merged.groupby('Classification')['win'].mean())

# Average trade size (USD)
print("\nAverage Trade Size by Sentiment:")
print(merged.groupby('Classification')['Size USD'].mean())

# Trade frequency
print("\nTrade Count by Sentiment:")
print(merged.groupby('Classification').size())

# Long/Short ratio
print("\nLong/Short Ratio:")
print(merged.groupby(['Classification', 'side']).size().unstack(fill_value=0))

# ==========================================================
# SEGMENTATION
# ==========================================================

# High vs Low trade size
median_size = merged['Size USD'].median()

merged['size_segment'] = np.where(
    merged['Size USD'] > median_size,
    'Large',
    'Small'
)

print("\nSegment Performance (Large vs Small):")
print(merged.groupby(['size_segment', 'Classification'])['closedPnL'].mean())

# Consistency (Volatility-based)
volatility = merged.groupby('account')['closedPnL'].std().reset_index()
median_vol = volatility['closedPnL'].median()

volatility['consistency'] = np.where(
    volatility['closedPnL'] < median_vol,
    'Consistent',
    'Inconsistent'
)

merged = merged.merge(
    volatility[['account', 'consistency']],
    on='account'
)

print("\nConsistency Performance:")
print(merged.groupby(['consistency', 'Classification'])['closedPnL'].mean())

# ==========================================================
# STRATEGY OUTPUT
# ==========================================================

print("\n================ STRATEGY IDEAS ================\n")

print("1. Reduce position size during Fear periods for large traders.")
print("2. Allow higher activity during Greed days for consistent traders.")
print("3. Use sentiment regime as a risk management filter.")

print("\n================================================")

# ==========================================================
# BONUS MODEL
# ==========================================================

daily = merged.groupby(['account', 'date']).agg({
    'closedPnL': 'sum',
    'Size USD': 'mean',
    'win': 'mean'
}).reset_index()

daily['profitable'] = daily['closedPnL'] > 0

X = daily[['Size USD', 'win']]
y = daily['profitable']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("\nPredictive Model Report:\n")
print(classification_report(y_test, pred))

print("\nAssignment Completed Successfully.")