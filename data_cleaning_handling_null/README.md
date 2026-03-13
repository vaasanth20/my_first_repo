
# Problem Statement
You are a data analyst at a healthcare clinic. Your manager has provided you with a patient dataset that needs cleaning before analysis. The dataset contains missing values, duplicate records, and incorrect data types that must be fixed.

Create the DataFrame using the code below, then complete all cleaning tasks.

```python3
import pandas as pd
import numpy as np
data = {
    'patient_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                   111, 112, 113, 114, 115, 101, 107, 118, 119, 120],
    'age': ['25', '34', None, '45', '29', None, '38', '52', '27', '41',
            '33', 'unknown', '48', '26', '35', '25', '38', '31', None, '44'],
    'weight': ['70', '65', '80', None, '75', None, '68', '90', '72', '85',
               '78', None, '82', '69', 'N/A', '70', '68', '74', None, '88'],
    'blood_pressure': [120, 130, None, 140, 125, None, 135, None, 118, 145,
                      128, None, 138, 122, None, 120, 135, 126, None, 142],
    'medication': ['Aspirin', 'Metformin', 'Lisinopril', None, 'Aspirin',
                   'Metformin', 'Lisinopril', 'Aspirin', None, 'Metformin',
                   'Lisinopril', 'Aspirin', None, 'Metformin', 'Aspirin',
                   'Aspirin', 'Lisinopril', 'Metformin', 'Aspirin', None],
    'insurance_provider': ['Blue Cross', 'Aetna', 'Cigna', 'UnitedHealth', None,
                          'Blue Cross', 'Aetna', 'Cigna', 'UnitedHealth', 'Blue Cross',
                          'Aetna', None, 'UnitedHealth', 'Blue Cross', 'Aetna',
                          'Blue Cross', 'Aetna', 'Cigna', 'UnitedHealth', None]
}

df = pd.DataFrame(data)
```

## Task 1: Inspect the Data
* Use df.info() to view column data types and non-null counts
* Use df.isnull().sum() to count missing values per column
* Calculate the percentage of missing values using: (df.isnull().sum() / len(df)) * 100
* Use df.duplicated().sum() to count duplicate rows


**Coding**
```python3
print("\n--- df.info() ---------------------")
df.info()
```
**Output**
```terminal

--- df.info() ---------------------
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20 entries, 0 to 19
Data columns (total 6 columns):
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   patient_id          20 non-null     int64  
 1   age                 17 non-null     object 
 2   weight              16 non-null     object 
 3   blood_pressure      14 non-null     float64
 4   medication          16 non-null     object 
 5   insurance_provider  17 non-null     object 
dtypes: float64(1), int64(1), object(4)
memory usage: 1.1+ KB
```

**Coding**
```python3
print("\n--- Missing values per column ---------------------")
missing = df.isnull().sum()
print(missing)
```
**Output**
```terminal

--- Missing values per column ---------------------
patient_id            0
age                   3
weight                4
blood_pressure        6
medication            4
insurance_provider    3
dtype: int64
```

**Coding**
```python3
print("\n--- Missing values (%) ---------------------")
missing_pct = (df.isnull().sum() / len(df)) * 100
print(missing_pct.round(2).astype(str) + "%")
```
**Output**
```terminal

--- Missing values (%) ---------------------
patient_id             0.0%
age                   15.0%
weight                20.0%
blood_pressure        30.0%
medication            20.0%
insurance_provider    15.0%
dtype: object
```

**Coding**
```python3
print("\n--- Duplicate rows ---------------------")
print(f"Total fully-duplicate rows: {df.duplicated().sum()}")
```
**Output**
```terminal

--- Duplicate rows ---------------------
Total fully-duplicate rows: 2
```

## Task 2: Data Type Conversion
* Convert age column to numeric using pd.to_numeric(df['age'], errors='coerce')
* Convert weight column to numeric using pd.to_numeric(df['weight'], errors='coerce')
* Check how many NEW missing values were created after conversion
* Convert insurance_provider to category type using astype('category')
* Use df.dtypes to verify all conversions


**Coding**
```python3
missing_before = df.isnull().sum()

# Convert age & weight to numeric; non-parseable values become NaN
df['age']    = pd.to_numeric(df['age'],    errors='coerce')
df['weight'] = pd.to_numeric(df['weight'], errors='coerce')

# Convert insurance_provider to category
df['insurance_provider'] = df['insurance_provider'].astype('category')

#Check how many NEW missing values were created after conversion
missing_after = df.isnull().sum()
new_nulls     = missing_after - missing_before

print("\n --- New NaN values created by type conversion ---")
print(new_nulls[new_nulls > 0].rename("new_nulls"))
```
**Output**
```terminal

 --- New NaN values created by type conversion ---
age       1
weight    1
Name: new_nulls, dtype: int64
```


**Coding**
```python3
# Use df.dtypes to verify all conversions
print("\n --- Data types after conversion  ---------------------")
print(df.dtypes)
```
**Output**
```terminal

 --- Data types after conversion  ---------------------
patient_id               int64
age                    float64
weight                 float64
blood_pressure         float64
medication              object
insurance_provider    category
dtype: object
```



## Task 3: Handle Missing Values
Apply appropriate strategies for each column:

* age: Fill with median using fillna(df['age'].median())
* weight: Fill with median using fillna(df['weight'].median())
* blood_pressure: Fill with median using fillna(df['blood_pressure'].median())
* medication: Fill with mode using fillna(df['medication'].mode()[0])
* insurance_provider: Fill with constant value 'Unknown'
Verify no missing values remain using df.isnull().sum()


**Coding**
```python3
df['age']                = df['age'].fillna(df['age'].median())
df['weight']             = df['weight'].fillna(df['weight'].median())
df['blood_pressure']     = df['blood_pressure'].fillna(df['blood_pressure'].median())
df['medication']         = df['medication'].fillna(df['medication'].mode()[0])

# Add 'Unknown' to categories before filling so pandas accepts the new value
df['insurance_provider'] = df['insurance_provider'].cat.add_categories(['Unknown'])
df['insurance_provider'] = df['insurance_provider'].fillna('Unknown')

print(df.isnull().sum())
print("\n No missing values remain" if df.isnull().sum().sum() == 0
      else "\n Some missing values still present")
```
**Output**
```terminal
patient_id            0
age                   0
weight                0
blood_pressure        0
medication            0
insurance_provider    0
dtype: int64

 No missing values remain
```


## Task 4: Handle Duplicates
* View duplicate rows using df[df.duplicated(keep=False)]
* Identify duplicates based on patient_id only using df.duplicated(subset=['patient_id'])
* Remove duplicates keeping first occurrence: df.drop_duplicates(subset=['patient_id'], keep='first')
* Print shape before and after to show how many rows were removed

**Coding**
```python3
# View duplicate rows
print("\n --- All rows involved in duplicates (keep=False) ---")
print(df[df.duplicated(keep=False)].to_string())
```
**Output**
```terminal

 --- All rows involved in duplicates (keep=False) ---
    patient_id   age  weight  blood_pressure  medication insurance_provider
0          101  25.0    70.0           120.0     Aspirin         Blue Cross
6          107  38.0    68.0           135.0  Lisinopril              Aetna
15         101  25.0    70.0           120.0     Aspirin         Blue Cross
16         107  38.0    68.0           135.0  Lisinopril              Aetna
```

**Coding**
```python3
# Identify duplicates based on patient_id
print("\n --- Duplicate patient_id entries (2nd+ occurrences) ---")
dup_mask = df.duplicated(subset=['patient_id'])
print(df[dup_mask][['patient_id']].to_string())
```
**Output**
```terminal

 --- Duplicate patient_id entries (2nd+ occurrences) ---
    patient_id
15         101
16         107
```

**Coding**
```python3
# Remove duplicates keeping first occurrence
shape_before = df.shape
df = df.drop_duplicates(subset=['patient_id'], keep='first')
shape_after  = df.shape

# Shape before removing duplicates
print(f"\nShape before removing duplicates : {shape_before}")
```
**Output**
```terminal

Shape before removing duplicates : (20, 6)
```

**Coding**
```python3
# Shape after  removing duplicates
print(f"\nShape after  removing duplicates : {shape_after}")
```
**Output**
```terminal

Shape after  removing duplicates : (18, 6)
```

**Coding**
```python3
# how many rows were removed
print(f"Rows removed                     : {shape_before[0] - shape_after[0]}")
```
**Output**
```terminal
Rows removed                     : 2
```


## Task 5: Complete Workflow with Verification
* Start fresh: reload the DataFrame and create a copy using df_clean = df.copy()
* Perform ALL cleaning steps in order: types → missing values → duplicates
* Create a verification report showing:
   * Shape before and after
   * Missing values before and after
   * Duplicates before and after
   * Data types before and after

**Coding**
```python3
# Reload & copy 
df_orig  = pd.DataFrame(data)
df_clean = df_orig.copy()

# Record BEFORE snapshots
shape_before_full      = df_clean.shape
missing_before_full    = df_clean.isnull().sum()
duplicates_before_full = df_clean.duplicated(subset=['patient_id']).sum()
dtypes_before          = df_clean.dtypes.copy()

# Step 1: Type conversion 
df_clean['age']                = pd.to_numeric(df_clean['age'],    errors='coerce')
df_clean['weight']             = pd.to_numeric(df_clean['weight'], errors='coerce')
df_clean['insurance_provider'] = df_clean['insurance_provider'].astype('category')

# Step 2: Fill missing values 
df_clean['age']                = df_clean['age'].fillna(df_clean['age'].median())
df_clean['weight']             = df_clean['weight'].fillna(df_clean['weight'].median())
df_clean['blood_pressure']     = df_clean['blood_pressure'].fillna(df_clean['blood_pressure'].median())
df_clean['medication']         = df_clean['medication'].fillna(df_clean['medication'].mode()[0])
df_clean['insurance_provider'] = df_clean['insurance_provider'].cat.add_categories(['Unknown'])
df_clean['insurance_provider'] = df_clean['insurance_provider'].fillna('Unknown')

# Step 3: Remove duplicates 
df_clean = df_clean.drop_duplicates(subset=['patient_id'], keep='first')

# Record AFTER snapshots
shape_after_full      = df_clean.shape
missing_after_full    = df_clean.isnull().sum()
duplicates_after_full = df_clean.duplicated(subset=['patient_id']).sum()
dtypes_after          = df_clean.dtypes.copy()
```

**Coding**
```python3
# Print verification report 
print("-" * 60)
print(f"{'Metric':<30} {'Before':>10} {'After':>10}")
print("-" * 60)
print(f"{'Shape (rows × cols)':<30} {str(shape_before_full):>10} {str(shape_after_full):>10}")
print(f"{'Total missing values':<30} {missing_before_full.sum():>10} {missing_after_full.sum():>10}")
print(f"{'Duplicate patient_ids':<30} {duplicates_before_full:>10} {duplicates_after_full:>10}")
```
**Output**
```terminal
------------------------------------------------------------
Metric                             Before      After
------------------------------------------------------------
Shape (rows × cols)               (20, 6)    (18, 6)
Total missing values                   20          0
Duplicate patient_ids                   2          0
```


**Coding**
```python3
print(f"\n--- Missing values per column ------")
print("-" * 40)
print(f"{'Column':<22} {'Before':>8} {'After':>8}")
print("-" * 40)
for col in df_orig.columns:
    b = missing_before_full[col]
    a = missing_after_full[col]
    print(f"{col:<22} {b:>8} {a:>8}")
```
**Output**
```terminal

--- Missing values per column ------
----------------------------------------
Column                   Before    After
----------------------------------------
patient_id                    0        0
age                           3        0
weight                        4        0
blood_pressure                6        0
medication                    4        0
insurance_provider            3        0
```


**Coding**
```python3
print(f"\n--- Data types per column ------")
print("-" * 52)
print(f"{'Column':<22} {'Before':>14} {'After':>14}")
print("-" * 52)
for col in df_orig.columns:
    print(f"{col:<22} {str(dtypes_before[col]):>14} {str(dtypes_after[col]):>14}")
```
**Output**
```terminal

--- Data types per column ------
----------------------------------------------------
Column                         Before          After
----------------------------------------------------
patient_id                      int64          int64
age                            object        float64
weight                         object        float64
blood_pressure                float64        float64
medication                     object         object
insurance_provider             object       category
```

**Coding**
```python3
print(f"\n--- Final cleaned DataFrame preview ------")
print(df_clean.head(10).to_string(index=True))
```
**Output**
```terminal

--- Final cleaned DataFrame preview ------
   patient_id   age  weight  blood_pressure  medication insurance_provider
0         101  25.0    70.0           120.0     Aspirin         Blue Cross
1         102  34.0    65.0           130.0   Metformin              Aetna
2         103  34.5    80.0           129.0  Lisinopril              Cigna
3         104  45.0    74.0           140.0     Aspirin       UnitedHealth
4         105  29.0    75.0           125.0     Aspirin            Unknown
5         106  34.5    74.0           129.0   Metformin         Blue Cross
6         107  38.0    68.0           135.0  Lisinopril              Aetna
7         108  52.0    90.0           129.0     Aspirin              Cigna
8         109  27.0    72.0           118.0     Aspirin       UnitedHealth
9         110  41.0    85.0           145.0   Metformin         Blue Cross
```


**Coding**
```python3
print(f"Cleaning complete — {shape_after_full[0]} clean patient records ready for analysis.")
```
**Output**
```terminal
Cleaning complete — 18 clean patient records ready for analysis.
```
