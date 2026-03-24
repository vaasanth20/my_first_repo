# Intermediate SQL Querying

Load both CSVs into a SQLite database using pandas and sqlite3

**Code:**
```python3
# Public dataset URLs
import pandas as pd
import sqlite3

customers_url = "https://raw.githubusercontent.com/graphql-compose/graphql-compose-examples/master/examples/northwind/data/csv/customers.csv"
orders_url = "https://raw.githubusercontent.com/graphql-compose/graphql-compose-examples/master/examples/northwind/data/csv/orders.csv"

# Read CSVs
customers_df = pd.read_csv(customers_url)
orders_df = pd.read_csv(orders_url)

# Load into in-memory SQLite
conn = sqlite3.connect(":memory:")
customers_df.to_sql("customers", conn, index=False, if_exists="replace")
orders_df.to_sql("orders", conn, index=False, if_exists="replace")

# Quick sanity checks
print(f"customers table : {len(customers_df):>4} rows  |  columns: {list(customers_df.columns)}")
print(f"orders    table : {len(orders_df):>4} rows  |  columns: {list(orders_df.columns)}")
```

**Output:**
```Terminal
customers table :   91 rows  |  columns: ['customerID', 'companyName', 'contactName', 'contactTitle', 'address', 'city', 'region', 'postalCode', 'country', 'phone', 'fax']
orders    table :  830 rows  |  columns: ['orderID', 'customerID', 'employeeID', 'orderDate', 'requiredDate', 'shippedDate', 'shipVia', 'freight', 'shipName', 'shipAddress', 'shipCity', 'shipRegion', 'shipPostalCode', 'shipCountry']
```


## Task 1 - Aggregation and Grouping

Using **only** the `orders` table, retrieve each customer's:
- total number of orders (`order_count`)
- total freight (`total_freight`)
- average freight per order (`avg_freight`)

Sorted by `total_freight` descending; top 10 rows displayed.

**Code:**
```python3
query_task1 = 
SELECT
    CustomerID,
    COUNT(OrderID) AS order_count,
    ROUND(SUM(Freight), 2) AS total_freight,
    ROUND(AVG(Freight), 2) AS avg_freight
FROM orders
GROUP BY CustomerID
ORDER BY total_freight DESC;


task1_df = pd.read_sql_query(query_task1, conn)

print("--- Task 1 - Top 10 Customers by Total Freight ---")
print(task1_df.head(10).to_string(index=False))
```
**Output:**
```Terminal
--- Task 1 - Top 10 Customers by Total Freight ---
customerID  order_count  total_freight  avg_freight
     SAVEA           31        6683.70       215.60
     ERNSH           30        6205.39       206.85
     QUICK           28        5605.63       200.20
     HUNGO           19        2755.24       145.01
     RATTC           18        2134.21       118.57
     QUEEN           13        1982.70       152.52
     FOLKO           19        1678.08        88.32
     BERGS           18        1559.52        86.64
     FRANK           15        1403.44        93.56
     MEREP           13        1394.22       107.25
```

## Task 2 - WHERE vs. HAVING

Two queries that both reference a freight threshold — but at different stages of query execution.

### Query A: From the orders table, filter rows where Freight is greater than 50 before aggregation, then group by CustomerID and return the count of such orders as high_freight_orders

**Code:**
```python3
query_A = 
SELECT
    CustomerID,
    COUNT(OrderID) AS high_freight_orders
FROM orders
WHERE Freight > 50
GROUP BY CustomerID
ORDER BY high_freight_orders DESC;


task2a_df = pd.read_sql_query(query_A, conn)

print("--- Query A — WHERE Freight > 50 (row-level filter BEFORE aggregation) ---\n")
print(task2a_df.head(10).to_string(index=False))
print(f"\nCustomers returned: {len(task2a_df)}")
```

**Output:**
```Terminal
--- Query A — WHERE Freight > 50 (row-level filter BEFORE aggregation) ---

customerID  high_freight_orders
     ERNSH                   27
     SAVEA                   25
     QUICK                   17
     HUNGO                   12
     RATTC                   11
     BERGS                   11
     QUEEN                   10
     FRANK                   10
     BONAP                   10
     HILAA                    9

Customers returned: 74
```

### Query B: From the orders table, group by CustomerID and return only those customers whose total freight exceeds 500, using HAVING. Return CustomerID and total_freight.

**Code:**
```python3
query_B = 
SELECT
    CustomerID,
    ROUND(SUM(Freight), 2) AS total_freight
FROM orders
GROUP BY CustomerID
HAVING SUM(Freight) > 500
ORDER BY total_freight DESC;


task2b_df = pd.read_sql_query(query_B, conn)

print("--- Query B — HAVING SUM(Freight) > 500 (group-level filter AFTER aggregation) ---\n")
print(task2b_df.to_string(index=False))
print(f"\nCustomers returned: {len(task2b_df)}")
```

**Output:**
```Terminal
=== Query B — HAVING SUM(Freight) > 500 (group-level filter AFTER aggregation) ===
customerID  total_freight
     SAVEA        6683.70
     ERNSH        6205.39
     QUICK        5605.63
     HUNGO        2755.24
     RATTC        2134.21
     QUEEN        1982.70
     FOLKO        1678.08
     BERGS        1559.52
     FRANK        1403.44
     MEREP        1394.22
     BONAP        1357.87
     WHITC        1353.06
     HILAA        1259.16
     PICCO        1186.11
     GREAL        1087.61
     LEHMS        1017.03
     RICSU        1001.29
     OLDWO         983.53
     VAFFE         947.34
     SEVES         913.81
     OTTIK         862.74
     EASTC         832.34
     WARTH         822.48
     SUPRD         821.23
     KOENE         813.68
     BOTTM         793.95
     LILAS         734.41
     HANAR         724.77
     LINOD         673.81
     FOLIG         637.94
     LAMAI         635.82
     RICAR         632.95
     BLONP         623.66
     GODOS         568.27
     SPLIR         558.67

Customers returned: 35
```

### Explanation — WHERE vs. HAVING

`WHERE` and `HAVING` apply their filters at **completely different points** in SQL's logical execution order.  

- **Query A (`WHERE Freight > 50`)** eliminates individual order rows whose freight is ≤ 50 *before* any grouping takes place. The resulting `high_freight_orders` count tells us how many qualifying single orders each customer had — a customer who placed 10 orders of \$40 each would be **excluded entirely**, because no single order clears the threshold.  

- **Query B (`HAVING SUM(Freight) > 500`)** first groups *all* rows by `CustomerID` and sums every order's freight — including small ones — then discards groups whose accumulated total falls below 500. That same customer with 10 × \$40 orders would show a `total_freight` of \$400 and be excluded, but a customer with 15 × \$40 orders (\$600 total) would be **included**, even though no individual order exceeded any threshold.  

In short: `WHERE` is a **row-level pre-filter** that shapes which data enters the aggregation, while `HAVING` is a **group-level post-filter** that shapes which aggregated results are returned.

## Task 3 - JOIN and Aggregation

Join customers and orders to enrich the aggregation with company name and country.

**Code:**
```python3
# ---INNER JOIN — only customers who have at least one order ---

query_inner = 
SELECT
    c.CompanyName,
    c.Country,
    COUNT(o.OrderID)        AS order_count,
    ROUND(SUM(o.Freight), 2)  AS total_freight
FROM customers c
INNER JOIN orders o
    ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID, c.CompanyName, c.Country
ORDER BY total_freight DESC;


inner_df = pd.read_sql_query(query_inner, conn)

print("--- INNER JOIN — Customers WITH Orders ---\n")
print(inner_df.head(10).to_string(index=False))
print(f"\nTotal customers returned: {len(inner_df)}")
```

**Output:**
```Terminal
--- INNER JOIN — Customers WITH Orders ---

                 companyName country  order_count  total_freight
          Save-a-lot Markets     USA           31        6683.70
                Ernst Handel Austria           30        6205.39
                  QUICK-Stop Germany           28        5605.63
Hungry Owl All-Night Grocers Ireland           19        2755.24
  Rattlesnake Canyon Grocery     USA           18        2134.21
               Queen Cozinha  Brazil           13        1982.70
              Folk och fä HB  Sweden           19        1678.08
          Berglunds snabbköp  Sweden           18        1559.52
              Frankenversand Germany           15        1403.44
              Mère Paillarde  Canada           13        1394.22

Total customers returned: 89
```

**LEFT JOIN — all customers; NULL / 0 for those with no orders**

**COALESCE converts NULL freight (unmatched customers) to 0 for readability.**

**Code:**
```python3
query_left = 
SELECT
    c.CompanyName,
    c.Country,
    COUNT(o.OrderID)                   AS order_count,
    ROUND(COALESCE(SUM(o.Freight), 0), 2) AS total_freight
FROM customers c
LEFT JOIN orders o
    ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID, c.CompanyName, c.Country
ORDER BY total_freight DESC;


left_df = pd.read_sql_query(query_left, conn)

print("--- LEFT JOIN — ALL Customers (including those with no orders) ---\n")
print(left_df.head(10).to_string(index=False))
print(f"\nTotal customers returned: {len(left_df)}")
```

**Output:**
```Terminal
--- LEFT JOIN — ALL Customers (including those with no orders) ---

                 companyName country  order_count  total_freight
          Save-a-lot Markets     USA           31        6683.70
                Ernst Handel Austria           30        6205.39
                  QUICK-Stop Germany           28        5605.63
Hungry Owl All-Night Grocers Ireland           19        2755.24
  Rattlesnake Canyon Grocery     USA           18        2134.21
               Queen Cozinha  Brazil           13        1982.70
              Folk och fä HB  Sweden           19        1678.08
          Berglunds snabbköp  Sweden           18        1559.52
              Frankenversand Germany           15        1403.44
              Mère Paillarde  Canada           13        1394.22

Total customers returned: 91
```

**Code:**
```python3
# --- Identify customers with no orders (the rows INNER JOIN would have dropped) ---
no_orders = left_df[left_df["order_count"] == 0]
print(f"Customers with no orders (LEFT JOIN extras): {len(no_orders)}")
if len(no_orders) > 0:
    print(no_orders.to_string(index=False))
```

**Output:**
```Terminal
Customers with no orders (LEFT JOIN extras): 2
                         companyName country  order_count  total_freight
FISSA Fabrica Inter. Salchichas S.A.   Spain            0            0.0
                   Paris spécialités  France            0            0.0
```

### Explanation — INNER JOIN vs. LEFT JOIN

**INNER JOIN** returns only rows where a matching `CustomerID` exists in **both** tables. Any customer in the `customers` table who has never placed an order is silently excluded from the result, because there is no corresponding row in `orders` to pair with.

**LEFT JOIN** keeps *every* row from the **left** table (`customers`) regardless of whether a match exists in `orders`. For customers with no orders, all columns from the `orders` side arrive as `NULL`. `COALESCE(SUM(o.Freight), 0)` converts that NULL to `0` for a cleaner display, and `COUNT(o.OrderID)` naturally returns `0` when there are no matching order rows.


The practical difference is that the LEFT JOIN result set is **larger** — it includes the full customer catalogue — making it the right choice when you need to report on *all* customers and simply want to note that some have no activity, rather than hiding them from the analysis entirely.
