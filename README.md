# Expense Tracker Analysis

A beginner-friendly Python project that reads daily expenses from a CSV file and uses **Pandas** and **NumPy** to show where the money goes: totals, category-wise spending, daily spending and High/Medium/Low expense levels.

Built for the **EWB Courses – Python with AI** internship.

**Student:** Vineela Kandi | **College:** Sreenidhi Institute of Science and Technology

## Objective

Many students do not know where their money goes each month. This program reads a list of expenses and gives a clear summary, so spending habits are easy to understand.

## Technologies Used

- Python 3
- Pandas (read CSV, groupby, sorting)
- NumPy (sum, mean, max, min)

## Files

| File | Purpose |
|---|---|
| `main.py` | The program |
| `expenses.csv` | Dataset: 25 expense records (Date, Category, Description, Amount) |
| `Project_Documentation.docx` | Project documentation |

## What the Program Does

1. Loads the CSV and shows the number of records, columns and first rows
2. Calculates total, average, highest and lowest expense (NumPy)
3. Calculates spending for each category and its percentage share (function and loop)
4. Calculates the average spent per day and the most expensive day
5. Labels every expense High (above 500), Medium (200 to 500) or Low (below 200) using a function
6. Lists the top 3 expenses

## How to Run

```
pip install pandas numpy
python main.py
```

Keep `expenses.csv` in the same folder as `main.py`.

## Sample Results

- Total spent: Rs. 8,572 across 25 expenses
- Biggest category: Shopping (30.0%), then Food (24.7%) and Bills (19.2%)
- Highest expense: Headphones, Rs. 1,200 on 2026-10-11
- 6 High, 8 Medium and 11 Low expenses

## Author

Vineela Kandi – Python with AI Internship, EWB Courses