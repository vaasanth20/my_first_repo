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
   **Code :**
   ```python3
   regional_sales = (
    df.groupby('region')['sales_amount']   # group rows by region
    .sum()                                  # sum sales_amount within each group
    .reset_index()                          # convert Series index → column
    )
    regional_sales.columns = ['region', 'total_sales']
    regional_sales = regional_sales.sort_values('total_sales', ascending=False)
    
    print(regional_sales)
   ```

   ***Output :**
   ```terminal
     region  total_sales
    2  South    158977.36
    1  North    135181.16
    3   West    109383.07
    0   East     95189.81
   ```
2. Count the number of transactions for each product category using groupby() and count()
   **Code :**
   ```python3
   category_counts = (
    df.groupby('category')['transaction_id']  # group by category
    .count()                                   # count non-null rows per group
    .reset_index()                             # flatten to DataFrame
    )
    category_counts.columns = ['category', 'transaction_count']
    category_counts = category_counts.sort_values('transaction_count', ascending=False)
    
    print(category_counts)
   ```

   **Output :**
   ```terminal
           category  transaction_count
    2    Electronics                 45
    3  Home & Garden                 43
    1       Clothing                 42
    0          Books                 39
    4         Sports                 31
   ```   
3. Calculate the average sales amount per salesperson using groupby() and mean()
   **Code :**
   ```python3
   salesperson_avg = (
    df.groupby('salesperson')['sales_amount']  # group by salesperson
    .mean()                                     # mean of sales_amount per group
    .reset_index()                              # flatten to DataFrame
    )
    salesperson_avg.columns = ['salesperson', 'avg_sales']
    salesperson_avg['avg_sales'] = salesperson_avg['avg_sales'].round(2)
    salesperson_avg = salesperson_avg.sort_values('avg_sales', ascending=False)
    
    print(salesperson_avg)
   ```

   **Output :**
   ```terminal
     salesperson  avg_sales
    3       David    2743.04
    1         Bob    2554.92
    4        Emma    2493.46
    5       Frank    2464.14
    2       Carol    2454.37
    0       Alice    1998.43
   ```   
4. For each result, use reset_index() to convert the result into a clean DataFrame
   **Code :**
   ```python3
   # --- BEFORE reset_index() ---
    before = df.groupby('region')['sales_amount'].sum()
    
    print(type(before))          # <class 'pandas.Series'>
    print(before)
    print("-"*40)
    print(before.index.tolist())
    
    # --- AFTER reset_index() ---
    after = df.groupby('region')['sales_amount'].sum().reset_index()
    
    print(type(after))           # <class 'pandas.DataFrame'>
    print(after)
    print("-"*40)
    print(after.columns.tolist()) 
    print("-"*40)
    print(after.index.tolist())

   # --- Applied to all three groupby results ---
    print("-"*40)
    print("--- 1. Regional total sales ---");
    print("-"*40)
    # 1. Regional total sales
    regional_sales = df.groupby('region')['sales_amount'].sum().reset_index()
    regional_sales.columns = ['region', 'total_sales']
    regional_sales['total_sales'] = regional_sales['total_sales'].round(2)
    print(regional_sales)
    
    print("-"*40)
    print("--- 2. Category transaction counts ---");
    print("-"*40)
    # 2. Category transaction counts
    category_counts = df.groupby('category')['transaction_id'].count().reset_index()
    category_counts.columns = ['category', 'transaction_count']
    print(category_counts)
    
    print("-"*40)
    print("--- 3. Salesperson average sales ---");
    print("-"*40)
    # 3. Salesperson average sales
    salesperson_avg = df.groupby('salesperson')['sales_amount'].mean().reset_index()
    salesperson_avg.columns = ['salesperson', 'avg_sales']
    salesperson_avg['avg_sales'] = salesperson_avg['avg_sales'].round(2)
    print(salesperson_avg)
    print("-"*40)

   ```

   **Output :**
   ```terminal
   <class 'pandas.core.series.Series'>
    region
    East      95189.81
    North    135181.16
    South    158977.36
    West     109383.07
    Name: sales_amount, dtype: float64
    ----------------------------------------
    ['East', 'North', 'South', 'West']
    
    <class 'pandas.core.frame.DataFrame'>
      region  sales_amount
    0   East      95189.81
    1  North     135181.16
    2  South     158977.36
    3   West     109383.07
    ----------------------------------------
    ['region', 'sales_amount']
    ----------------------------------------
    [0, 1, 2, 3]

   ----------------------------------------
    --- 1. Regional total sales ---
    ----------------------------------------
      region  total_sales
    0   East     95189.81
    1  North    135181.16
    2  South    158977.36
    3   West    109383.07
    
    ----------------------------------------
    --- 2. Category transaction counts ---
    ----------------------------------------
            category  transaction_count
    0          Books                 39
    1       Clothing                 42
    2    Electronics                 45
    3  Home & Garden                 43
    4         Sports                 31
    
    ----------------------------------------
    --- 3. Salesperson average sales ---
    ----------------------------------------
      salesperson  avg_sales
    0       Alice    1998.43
    1         Bob    2554.92
    2       Carol    2454.37
    3       David    2743.04
    4        Emma    2493.46
    5       Frank    2464.14
    ----------------------------------------
   ```   
5. Sort the regional sales results in descending order using sort_values(ascending=False) to identify the top-performing region
   **Code :**
   ```python3
   # --- Build regional sales DataFrame ---
    regional_sales = df.groupby('region')['sales_amount'].sum().reset_index()
    regional_sales.columns = ['region', 'total_sales']
    regional_sales['total_sales'] = regional_sales['total_sales'].round(2)
    
    # --- BEFORE sort_values() — alphabetical order (default) ---
    print("-"*50)
    print(" BEFORE sort_values() - alphabetical order (default)");
    print("-"*50)
    print(regional_sales)
    
    # --- ascending=True — lowest sales first ---
    print("-"*50)
    print(" ascending=True - lowest sales first");
    print("-"*50)
    print(regional_sales.sort_values('total_sales', ascending=True))
    
    # --- ascending=False — highest sales first ---
    print("-"*50)
    print("  ascending=False - highest sales first ");
    print("-"*50)
    descending = regional_sales.sort_values('total_sales', ascending=False)
    print(descending)
    
    # --- Identify top-performing region ---
    print("-"*50)
    print(" Identify top-performing region");
    print("-"*50)
    top_region = descending.iloc[0]           # first row = highest value
    print(f"Top region : {top_region['region']}")         # South
    print(f"Total sales: ${top_region['total_sales']:,.2f}")  # $158,977.36
    
    # --- Full ranking with gap vs top ---
    print("-"*50)
    print(" Full ranking with gap vs top");
    print("-"*50)
    ranked = descending.reset_index(drop=True)   # clean 0-based index after sort
    print(ranked)
   ```

   **Output :**
   ```terminal
   --------------------------------------------------
     BEFORE sort_values() - alphabetical order (default)
    --------------------------------------------------
      region  total_sales
    0   East     95189.81
    1  North    135181.16
    2  South    158977.36
    3   West    109383.07
    --------------------------------------------------
     ascending=True - lowest sales first
    --------------------------------------------------
      region  total_sales
    0   East     95189.81
    3   West    109383.07
    1  North    135181.16
    2  South    158977.36
    --------------------------------------------------
      ascending=False - highest sales first 
    --------------------------------------------------
      region  total_sales
    2  South    158977.36
    1  North    135181.16
    3   West    109383.07
    0   East     95189.81
    --------------------------------------------------
     Identify top-performing region
    --------------------------------------------------
    Top region : South
    Total sales: $158,977.36
    --------------------------------------------------
     Full ranking with gap vs top
    --------------------------------------------------
      region  total_sales
    0  South    158977.36
    1  North    135181.16
    2   West    109383.07
    3   East     95189.81
   ``` 

## Task 2: Multi-Column Grouping and Multiple Aggregations
Perform advanced grouping analysis:

1. Group by both region AND category to calculate total sales for each combination using:
  ```python3
  df.groupby(['region', 'category'])['sales_amount'].sum().reset_index()
  ```

   **Code :**
   ```python3
    # --- Task 1: Multi-column groupby ---
    region_category = (
        df.groupby(['region', 'category'])['sales_amount']
        .sum()
        .reset_index()
    )
    region_category.columns = ['region', 'category', 'total_sales']
    print("-"*60)
    print(" Task 1: Multi-column groupby");
    print("-"*60)
    print(region_category)
   ```

   **Output :**
   ```terminal
    ------------------------------------------------------------
     Task 1: Multi-column groupby
    ------------------------------------------------------------
       region       category  total_sales
    0    East          Books     20027.53
    1    East       Clothing     19926.20
    2    East    Electronics     22791.55
    3    East  Home & Garden     15949.08
    4    East         Sports     16495.45
    5   North          Books     42592.53
    6   North       Clothing     18959.06
    7   North    Electronics     38889.84
    8   North  Home & Garden     19344.48
    9   North         Sports     15395.25
    10  South          Books     21007.68
    11  South       Clothing     50878.36
    12  South    Electronics     39229.63
    13  South  Home & Garden     22592.00
    14  South         Sports     25269.69
    15   West          Books     20359.41
    16   West       Clothing     16548.81
    17   West    Electronics     13553.27
    18   West  Home & Garden     33069.36
    19   West         Sports     25852.22
   ```
2. For each salesperson, calculate three metrics simultaneously using the agg() method:
  - Total sales ('sum')
  - Average sales ('mean')
  - Number of transactions ('count')
    
    Use this syntax:
    ```python3
    df.groupby('salesperson')['sales_amount'].agg(['sum', 'mean', 'count']).reset_index()
    ```


   **Code :**
   ```python3
    # --- Task 2: agg() — three metrics in one call ---
    salesperson_metrics = (
        df.groupby('salesperson')['sales_amount']
        .agg(['sum', 'mean', 'count'])
        .reset_index()
    )
    salesperson_metrics.columns = ['salesperson', 'total_sales', 'avg_sales', 'transaction_count']
    salesperson_metrics['total_sales'] = salesperson_metrics['total_sales'].round(2)
    salesperson_metrics['avg_sales']   = salesperson_metrics['avg_sales'].round(2)
    print("-"*60)
    print(" Task 2: agg() - three metrics in one call");
    print("-"*60)
    print(salesperson_metrics)
   ```

   **Output :**
   ```terminal
    ------------------------------------------------------------
     Task 2: agg() - three metrics in one call
    ------------------------------------------------------------
      salesperson  total_sales  avg_sales  transaction_count
    0       Alice     43965.51    1998.43                 22
    1         Bob     81757.41    2554.92                 32
    2       Carol     68722.32    2454.37                 28
    3       David    123436.64    2743.04                 45
    4        Emma     82284.09    2493.46                 33
    5       Frank     98565.43    2464.14                 40
   ```    
3. Sort the salesperson results by total sales in descending order to identify the top performer

   **Code :**
   ```python3
   # --- Task 3: Sort by total_sales descending ---
    salesperson_sorted = (
        salesperson_metrics
        .sort_values('total_sales', ascending=False)
        .reset_index(drop=True)
    )
    print("-"*60)
    print(" Task 3: Sort by total_sales descendingl");
    print("-"*60)
    print(salesperson_sorted)
    print("-"*60)
    top = salesperson_sorted.iloc[0]
    print(top)
   ```

   **Output :**
   ```terminal
       ------------------------------------------------------------
     Task 3: Sort by total_sales descendingl
    ------------------------------------------------------------
      salesperson  total_sales  avg_sales  transaction_count
    0       David    123436.64    2743.04                 45
    1       Frank     98565.43    2464.14                 40
    2        Emma     82284.09    2493.46                 33
    3         Bob     81757.41    2554.92                 32
    4       Carol     68722.32    2454.37                 28
    5       Alice     43965.51    1998.43                 22
    ------------------------------------------------------------
    salesperson              David
    total_sales          123436.64
    avg_sales              2743.04
    transaction_count           45
    Name: 0, dtype: object
   ```
4. Use .idxmax() on the grouped category sales to find which category has the maximum total revenue

   **Code :**
   ```python3
   # --- Task 4: idxmax() — find the category label with max revenue ---
    category_sales = df.groupby('category')['sales_amount'].sum()
    print("-"*60)
    print(" Task 4: idxmax() — find the category label with max revenue ");
    print("-"*60)
    print(category_sales)
    print("-"*60)
    max_category = category_sales.idxmax()
    print(f" Max category : {max_category}") 
    print(f" Revenue      : ${category_sales[max_category]:,.2f}") 
   ```

   **Output :**
   ```terminal
    ------------------------------------------------------------
     Task 4: idxmax() — find the category label with max revenue 
    ------------------------------------------------------------
    category
    Books            103987.15
    Clothing         106312.43
    Electronics      114464.29
    Home & Garden     90954.92
    Sports            83012.61
    Name: sales_amount, dtype: float64
    ------------------------------------------------------------
     Max category : Electronics
     Revenue      : $114,464.29
   ```

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

   **Code :**
   ```python3
    region_custom = (
        df.groupby('region')['sales_amount']
        .agg(['sum', 'mean', 'min', 'max', sales_range])  # strings + function object
        .reset_index()
    )
    region_custom.columns = ['region', 'total_sales', 'avg_sales',
                              'min_sale', 'max_sale', 'sales_range']
    
    print( "-" * 70)
    print("  Task 2 - Region aggregation with custom sales_range")
    print( "-" * 70)
    print(region_custom.to_string(index=False))
   ```

   **Output :**
   ```terminal
    ----------------------------------------------------------------------
      Task 2 - Region aggregation with custom sales_range
    ----------------------------------------------------------------------
    region  total_sales   avg_sales  min_sale  max_sale  sales_range
      East     95189.81 2213.716512    307.82   4758.46      4450.64
     North    135181.16 2413.949286    110.71   4788.56      4677.85
     South    158977.36 2789.076491    373.45   4983.33      4609.88
      West    109383.07 2485.978864    203.60   4903.53      4699.93
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

    
   **Code :**
   ```python3
   # --- Step 1: Build the raw multi-level result ---
    summary_raw = (
        df.groupby('region').agg({
            'sales_amount': ['sum', 'mean'],  # two functions on one column
            'customer_id':  'count'           # one function on a different column
        })
        .reset_index()
    )
    
    print( "\n"+"-" * 70)
    print("  1. RAW output (multi-level column header)")
    print( "-" * 70)
    print("  Column tuples:", summary_raw.columns.tolist())
    
    print(summary_raw.to_string(index=False))
    
    # --- Step 2: Flatten to a clean single-level DataFrame ---
    summary_raw.columns = ['region', 'total_sales', 'avg_sales', 'transaction_count']
    summary = summary_raw.sort_values('total_sales', ascending=False).reset_index(drop=True)
    print( "\n"+"-" * 70)
    print("2. CLEAN summary report (after flattening columns)")
    print( "-" * 70)
    print(summary.to_string(index=False))
    
    # --- Step 3: Formatted report output ---
    print("\n"+"-" * 70)
    print("3. Regional Sales Summary Report")
    print("-" * 70)
    print(f"  {'Rank':<6}{'Region':<10}{'Transactions':>14}{'Total Sales':>14}{'Avg / Deal':>12}")
    print("-" * 70)
    for i, row in summary.iterrows():
        print(
            f"  #{i+1:<5}{row['region']:<10}"
            f"{row['transaction_count']:>14,}"
            f"{row['total_sales']:>14,.2f}"
            f"{row['avg_sales']:>12,.2f}"
        )
    print("-" * 70)
    print(
        f"  {'TOT':<6}{'ALL':<10}"
        f"{summary['transaction_count'].sum():>14,}"
        f"{summary['total_sales'].sum():>14,.2f}"
    )

   ```

   **Output :**
   ```terminal
   
    ----------------------------------------------------------------------
      1. RAW output (multi-level column header)
    ----------------------------------------------------------------------
      Column tuples: [('region', ''), ('sales_amount', 'sum'), ('sales_amount', 'mean'), ('customer_id', 'count')]
    region sales_amount             customer_id
                    sum        mean       count
      East     95189.81 2213.716512          43
     North    135181.16 2413.949286          56
     South    158977.36 2789.076491          57
      West    109383.07 2485.978864          44
    
    ----------------------------------------------------------------------
    2. CLEAN summary report (after flattening columns)
    ----------------------------------------------------------------------
    region  total_sales   avg_sales  transaction_count
     South    158977.36 2789.076491                 57
     North    135181.16 2413.949286                 56
      West    109383.07 2485.978864                 44
      East     95189.81 2213.716512                 43
    
    ----------------------------------------------------------------------
    3. Regional Sales Summary Report
    ----------------------------------------------------------------------
      Rank  Region      Transactions   Total Sales  Avg / Deal
    ----------------------------------------------------------------------
      #1    South                 57    158,977.36    2,789.08
      #2    North                 56    135,181.16    2,413.95
      #3    West                  44    109,383.07    2,485.98
      #4    East                  43     95,189.81    2,213.72
    ----------------------------------------------------------------------
      TOT   ALL                  200    498,731.40
   ```
4. Explain the multi-level column structure that results from the dictionary-based aggregation and how it differs from single aggregations


   **Code :**
   ```python3   
    raw = (
        df.groupby('region').agg({
            'sales_amount': ['sum', 'mean'],
            'customer_id':  'count'
        }).reset_index()
    )
    
    print("\n" + "-" * 70)
    print("4. Three column-flattening methods")
    print("-" * 70)
    print("  Original columns:", raw.columns.tolist())
    print("\n" + "-" * 70)
    
    # Method 1 - Direct rename (recommended: full control over names)
    m1 = raw.copy()
    m1.columns = ['region', 'total_sales', 'avg_sales', 'transaction_count']
    print("Method 1 - direct rename:")
    #print(" ", m1.columns.tolist())
    print(m1.to_string(index=False))
    print("\n" + "-" * 70)
    
    # Method 2 - Auto-join with underscore separator
    m2 = raw.copy()
    m2.columns = ['_'.join(col).strip('_') for col in m2.columns.values]
    print("Method 2 - underscore join:")
    #print(" ", m2.columns.tolist())
    print(m2.to_string(index=False))
    
    print("\n" + "-" * 70)
    # Method 3 - f-string conditional (skips '_' when level-1 is empty)
    m3 = raw.copy()
    m3.columns = [f"{a}_{b}" if b else a for a, b in m3.columns]
    print("Method 3 - f-string conditional:")
    #print(" ", m3.columns.tolist())
    print(m3.to_string(index=False))
    print("\n" + "-" * 70)
    
    # Accessing columns BEFORE flattening (using tuple keys)
    raw2 = df.groupby('region').agg({
        'sales_amount': ['sum', 'mean'],
        'customer_id':  'count'
    })
    
    print(raw2)
    
    print( "\n"+"-" * 70)
    print("Accessing multi-level columns with tuple keys:")
    print( "-" * 70)
    print(raw2[('sales_amount', 'sum')])        # one sub-column
    print( "\n"+"-" * 70)
    print("Selecting all sales_amount sub-columns:")
    print( "-" * 70)
    print(raw2['sales_amount'])                 # returns both sum and mean
    print( "-" * 70)

   ```

   **Output :**
   ```terminal
   
    ----------------------------------------------------------------------
    4. Three column-flattening methods
    ----------------------------------------------------------------------
      Original columns: [('region', ''), ('sales_amount', 'sum'), ('sales_amount', 'mean'), ('customer_id', 'count')]
    
    ----------------------------------------------------------------------
    Method 1 - direct rename:
    region  total_sales   avg_sales  transaction_count
      East     95189.81 2213.716512                 43
     North    135181.16 2413.949286                 56
     South    158977.36 2789.076491                 57
      West    109383.07 2485.978864                 44
    
    ----------------------------------------------------------------------
    Method 2 - underscore join:
    region  sales_amount_sum  sales_amount_mean  customer_id_count
      East          95189.81        2213.716512                 43
     North         135181.16        2413.949286                 56
     South         158977.36        2789.076491                 57
      West         109383.07        2485.978864                 44
    
    ----------------------------------------------------------------------
    Method 3 - f-string conditional:
    region  sales_amount_sum  sales_amount_mean  customer_id_count
      East          95189.81        2213.716512                 43
     North         135181.16        2413.949286                 56
     South         158977.36        2789.076491                 57
      West         109383.07        2485.978864                 44
    
    ----------------------------------------------------------------------
           sales_amount              customer_id
                    sum         mean       count
    region                                      
    East       95189.81  2213.716512          43
    North     135181.16  2413.949286          56
    South     158977.36  2789.076491          57
    West      109383.07  2485.978864          44
   ----------------------------------------------------------------------
    Accessing multi-level columns with tuple keys:
    ----------------------------------------------------------------------
    region
    East      95189.81
    North    135181.16
    South    158977.36
    West     109383.07
    Name: (sales_amount, sum), dtype: float64
    
    ----------------------------------------------------------------------
    Selecting all sales_amount sub-columns:
    ----------------------------------------------------------------------
                  sum         mean
    region                        
    East     95189.81  2213.716512
    North   135181.16  2413.949286
    South   158977.36  2789.076491
    West    109383.07  2485.978864
    ----------------------------------------------------------------------
   ```
## SUMMARY: When do you get multi-level columns?**

.agg(['sum','mean']) on ONE column -- flat (single-level)

.agg({'col1':['sum','mean'], -- MultiIndex (two-level)

'col2':'count'}) -- must flatten before rename


Think of it like a table with two rows of headings instead of one.

When you use a simple list aggregation on one column, pandas only needs one row of headings because everything came from the same place — `sales_amount`. So the result looks like a normal table:

```terminal
region  |  sum      |  mean
South   |  158977   |  2789
North   |  135181   |  2414
```

But when you use a dictionary and ask for results from **two different columns at once**, pandas gets confused about how to label things with just one header row. For example, both `sum` and `mean` came from `sales_amount`, but `count` came from `customer_id`. If it just wrote `sum, mean, count` across the top, you would have no idea which original column each one belonged to.

So pandas solves this by adding a **second header row above the first**, like a parent label sitting over its children:

```terminal
        |    sales_amount    |  customer_id
        |  sum    |  mean    |  count
South   | 158977  |  2789    |   57
North   | 135181  |  2414    |   56
```

The top row tells you **where the data came from**. The bottom row tells you **what was calculated**. Together they remove all ambiguity.

The practical consequence is that before you can rename columns or do anything else with the result, you have to collapse those two header rows into one — which is what the three flattening methods do. Until you flatten, each column has a two-part name like `('sales_amount', 'sum')` instead of a simple name like `total_sales`.


