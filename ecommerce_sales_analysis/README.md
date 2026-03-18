# Question : Problem Statement
You are a data analyst at an e-commerce company. Your manager needs insights about sales performance across different regions, product categories, and salespersons. You have been asked to analyze the sales data to identify top performers and generate summary reports.

Since you cannot access the company database directly, create a synthetic sales dataset using the code below, then complete all analysis tasks.

```python3
import pandas as pd
import random

random.seed(42)

# Define data parameters
regions = ['North', 'South', 'East', 'West']
categories = ['Electronics', 'Clothing', 'Home & Garden', 'Sports', 'Books']
salespersons = ['Alice', 'Bob', 'Carol', 'David', 'Emma', 'Frank']

# Generate 200 sales transactions
data = {
    'transaction_id': range(1001, 1201),
    'region': [random.choice(regions) for _ in range(200)],
    'category': [random.choice(categories) for _ in range(200)],
    'salesperson': [random.choice(salespersons) for _ in range(200)],
    'sales_amount': [round(random.uniform(50, 5000), 2) for _ in range(200)],
    'customer_id': [random.randint(5000, 5100) for _ in range(200)]
}

df = pd.DataFrame(data)
print(df.head(10))
print(f"\nDataset shape: {df.shape}")
```

## Task 1: Basic Grouping and Single Aggregations
Perform the following grouping operations:

1. Calculate total sales amount for each region using groupby() and sum()
2. Count the number of transactions for each product category using groupby() and count()
3. Calculate the average sales amount per salesperson using groupby() and mean()
4. For each result, use reset_index() to convert the result into a clean DataFrame
5. Sort the regional sales results in descending order using sort_values(ascending=False) to identify the top-performing region

## Task 2: Multi-Column Grouping and Multiple Aggregations
Perform advanced grouping analysis:

1. Group by both region AND category to calculate total sales for each combination using:
  ```python3
  df.groupby(['region', 'category'])['sales_amount'].sum().reset_index()
  ```
2. For each salesperson, calculate three metrics simultaneously using the agg() method:
  - Total sales ('sum')
  - Average sales ('mean')
  - Number of transactions ('count')
    
    Use this syntax:
    ```python3
    df.groupby('salesperson')['sales_amount'].agg(['sum', 'mean', 'count']).reset_index()
    ```
3. Sort the salesperson results by total sales in descending order to identify the top performer
4. Use .idxmax() on the grouped category sales to find which category has the maximum total revenue

## Task 3: Custom Aggregation and Complete Sales Report
Create a comprehensive sales analysis report:

1. Define a custom aggregation function that calculates the sales range (max - min) for each group:
```python3
def sales_range(x):
    return x.max() - x.min()
```
2. Apply this custom function along with standard aggregations to analyze sales by region:
```pyhton3
df.groupby('region')['sales_amount'].agg(['sum', 'mean', 'min', 'max', sales_range]).reset_index()
```
3. Create a final summary report that shows for each region:

    - Total number of transactions (using customer_id with count)
    - Total sales amount
    - Average transaction value
    
    Use dictionary syntax in agg():
    ```python3
    df.groupby('region').agg({
        'sales_amount': ['sum', 'mean'],
        'customer_id': 'count'
    }).reset_index()
    ```
4. Explain the multi-level column structure that results from the dictionary-based aggregation and how it differs from single aggregations

