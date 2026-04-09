# Data Prep & Feature Engineering

You are given a small passenger dataset. Your task is to apply categorical encoding and feature scaling to prepare it for a machine learning model.

```python3
import pandas as pd

data = {
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female'],
    'City': ['Mumbai', 'Delhi', 'Chennai', 'Mumbai', 'Delhi'],
    'Size': ['Small', 'Large', 'Medium', 'Large', 'Small'],
    'Age': [25, 45, 32, 60, 28],
    'Fare': [15, 300, 85, 450, 20]
}

df = pd.DataFrame(data)
```

## Task 1 - Categorical Encoding

Apply the correct encoding method to each categorical column:

- *Gender :-* Label Encoding
- *City :-* One-Hot Encoding (drop one column to avoid the dummy variable trap)
- *Size :-* Label Encoding with the correct order: Small=0, Medium=1, Large=2

```python3

# 1. Gender -> Label Encoding
le_gender = LabelEncoder()
df['Gender'] = le_gender.fit_transform(df['Gender'])

# 2. City -> One-Hot Encoding (drop_first=True to avoid dummy variable trap)
df = pd.get_dummies(df, columns=['City'], drop_first=True)

# 3. Size -> Label Encoding (Manual Mapping for Ordinal data)
# Note: LabelEncoder assigns values alphabetically. To ensure Small=0, Medium=1, Large=2, 
# we use a manual map.
size_mapping = {'Small': 0, 'Medium': 1, 'Large': 2}
df['Size'] = df['Size'].map(size_mapping)

```

## Task 2 - Feature Scaling

The Fare column contains a value of 450 which is a potential outlier. Apply the appropriate scaler to both Age and Fare, and briefly justify your choice in a comment.

*Code :*

```python3

# We use RobustScaler because the 'Fare' column contains significant outliers (e.g., 450).
# RobustScaler uses the median and the interquartile range (IQR), making it 
# less sensitive to extreme values compared to StandardScaler or MinMaxScaler.
scaler = RobustScaler()

df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

# Display processed dataframe
print("Processed DataFrame:")
print(df)

```

*Output :*

```Terminal

Processed DataFrame:
   Gender  Size       Age      Fare  City_Delhi  City_Mumbai
0       1     0 -0.411765 -0.250000       False         True
1       0     2  0.764706  0.767857        True        False
2       0     1  0.000000  0.000000       False        False
3       1     2  1.647059  1.303571       False         True
4       0     0 -0.235294 -0.232143        True        False

```

## Step-by-Step Breakdown

### Categorical Encoding Logic

- **Gender (Binary):** LabelEncoder is efficient here because there are only two categories.

- **City (Nominal):** Since there is no inherent order between Mumbai and Delhi, we use One-Hot Encoding. Dropping the first column ensures we don't have perfect multicollinearity (the dummy variable trap).

- **Size (Ordinal):** Because the size has a logical progression (Small < Medium < Large), we use Ordinal Mapping. Using a standard LabelEncoder would have likely assigned Large=0, Medium=1, and Small=2 based on alphabetization, which ruins the mathematical relationship.

### Feature Scaling Logic

I chose the RobustScaler for this task.

- **StandardScaler** relies on the mean and standard deviation, which are heavily skewed by outliers like the $450$ fare.

- **MinMaxScaler** would compress all other values into a tiny range (e.g., $15$ and $20$ would become nearly identical) to accommodate the $450$ maximum.

- **RobustScaler** centers the data based on the median, ensuring the "typical" fares remain distinct and meaningful.
