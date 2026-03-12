# Question: Create, Save, and Explore a Student DataFrame Using Pandas

## Tasks to Perform
- Create a pandas DataFrame using the student data provided below
- Save the DataFrame as a CSV file named students.csv
- Reoad students.csv into a new DataFrame
- Display the first 3 rows using df.head(3)
- Display the statistical summary using df.describe()
- Explore the data further using df.shape, df.dtypes, and df.info()

## Data Provided
<table>
	<tr><th>StudentID</th><th>Name</th><th>Age</th><th>Marks</th><th>Grade</th></tr>
	<tr><td>101</td><td>Alice</td><td>20</td><td>88</td><td>A</td></tr>
	<tr><td>102</td><td>Bob</td><td>21</td><td>75</td><td>B</td></tr>
	<tr><td>103</td><td>Charlie</td><td>19</td><td>92</td><td>A</td></tr>
	<tr><td>104</td><td>Diana</td><td>22</td><td>65</td><td>C</td></tr>
	<tr><td>105</td><td>Ethan</td><td>20</td><td>78</td><td>B</td></tr>
	<tr><td>106</td><td>Fiona</td><td>21</td><td>85</td><td>A</td></tr>
	<tr><td>107</td><td>George</td><td>23</td><td>70</td><td>B</td></tr>
	<tr><td>108</td><td>Hannah</td><td>19</td><td>95</td><td>A</td></tr>
	<tr><td>109</td><td>Ivan</td><td>22</td><td>60</td><td>C</td></tr>
	<tr><td>110</td><td>Julia</td><td>20</td><td>80</td><td>B</td></tr>
</table>

## Code
```python3
import pandas as pd
```

### Step 1: Create the student DataFrame

```python3
data = {
    'StudentID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan', 'Fiona', 'George', 'Hannah', 'Ivan', 'Julia'],
    'Age': [20, 21, 19, 22, 20, 21, 23, 19, 22, 20],
    'Marks': [88, 75, 92, 65, 78, 85, 70, 95, 60, 80],
    'Grade': ['A', 'B', 'A', 'C', 'B', 'A', 'B', 'A', 'C', 'B']
}

df = pd.DataFrame(data)
print("DataFrame created successfully!")
print(df)
```

**output:**
```terminal
DataFrame created successfully!
   StudentID     Name  Age  Marks Grade
0        101    Alice   20     88     A
1        102      Bob   21     75     B
2        103  Charlie   19     92     A
3        104    Diana   22     65     C
4        105    Ethan   20     78     B
5        106    Fiona   21     85     A
6        107   George   23     70     B
7        108   Hannah   19     95     A
8        109     Ivan   22     60     C
9        110    Julia   20     80     B
```

### Step 2: Save the DataFrame as a CSV file

```python3
df.to_csv('students.csv', index=False)
print("\nDataFrame saved to students.csv")
```

**output:**
```terminal

DataFrame saved to students.csv
```

### Step 3: Reload students.csv into a new DataFrame

```python3
df = pd.read_csv('students.csv')
print("\nCSV reloaded successfully!")
```

**output:**
```terminal

CSV reloaded successfully!
```

### Step 4: Display the first 3 rows

```python3
print("\nFirst 3 rows (df.head(3)):")
print(df.head(3))
```

**output:**
```terminal

First 3 rows (df.head(3)):
   StudentID     Name  Age  Marks Grade
0        101    Alice   20     88     A
1        102      Bob   21     75     B
2        103  Charlie   19     92     A
```

### Step 5: Display the statistical summary

```python3
print("\nStatistical Summary (df.describe()):")
print(df.describe())
```

**output:**
```terminal

Statistical Summary (df.describe()):
       StudentID        Age      Marks
count   10.00000  10.000000  10.000000
mean   105.50000  20.700000  78.800000
std      3.02765   1.337494  11.535453
min    101.00000  19.000000  60.000000
25%    103.25000  20.000000  71.250000
50%    105.50000  20.500000  79.000000
75%    107.75000  21.750000  87.250000
max    110.00000  23.000000  95.000000
```

### Step 6: Explore the DataFrame further

```python3
print("\nShape of DataFrame (df.shape):")
print(df.shape)
```

**output:**
```terminal

Shape of DataFrame (df.shape):
(10, 5)
```

```python3
print("\nData Types (df.dtypes):")
print(df.dtypes)
```

**output:**
```terminal

Data Types (df.dtypes):
StudentID     int64
Name         object
Age           int64
Marks         int64
Grade        object
dtype: object
```

```python3
print("\nDataFrame Info (df.info()):")
df.info()
```

**output:**
```terminal

DataFrame Info (df.info()):
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 5 columns):
 #   Column     Non-Null Count  Dtype 
---  ------     --------------  ----- 
 0   StudentID  10 non-null     int64 
 1   Name       10 non-null     object
 2   Age        10 non-null     int64 
 3   Marks      10 non-null     int64 
 4   Grade      10 non-null     object
dtypes: int64(3), object(2)
memory usage: 532.0+ bytes
```

