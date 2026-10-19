# Expense Tracker Analysis
# Reads my expenses from a CSV file and shows where the money goes.

import pandas as pd
import numpy as np


# Function 1: label an expense as High, Medium or Low
def get_level(amount):
    if amount > 500:
        return "High"
    elif amount >= 200:
        return "Medium"
    else:
        return "Low"


# Function 2: print the total of each category using a loop
def show_category_totals(df, total):
    category_total = df.groupby("Category")["Amount"].sum()
    for category in category_total.index:
        amount = category_total[category]
        percent = round(amount / total * 100, 1)
        print(category, ":", amount, "(", percent, "% )")
    print("Biggest category:", category_total.idxmax())


# Step 1: read the file
df = pd.read_csv("expenses.csv")
print("Number of records:", len(df))
print("Columns:", list(df.columns))
print(df.head())

# Step 2: total, average, highest, lowest using NumPy
amounts = df["Amount"].to_numpy()
total = np.sum(amounts)
print("\nTotal spent:", total)
print("Average expense:", round(np.mean(amounts), 2))
print("Highest expense:", np.max(amounts))
print("Lowest expense:", np.min(amounts))

# Step 3: spending by category
print("\nSpending by category:")
show_category_totals(df, total)

# Step 4: spending per day
daily = df.groupby("Date")["Amount"].sum()
print("\nDays with expenses:", len(daily))
print("Average spent per day:", round(total / len(daily), 2))
print("Most expensive day:", daily.idxmax(), "-", daily.max())

# Step 5: High / Medium / Low
df["Level"] = df["Amount"].apply(get_level)
print("\nExpense levels:")
print(df["Level"].value_counts())

# Step 6: top 3 expenses
print("\nTop 3 expenses:")
print(df.nlargest(3, "Amount"))