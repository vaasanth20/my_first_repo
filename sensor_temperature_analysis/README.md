# Sensor Temperature Analysis
You are given daily temperature readings from 4 weather stations, each with 5 daily readings:

```python3
import numpy as np

data = np.array([[22.5, 19.0, 31.2, 28.7, 25.1],
                 [17.3, 22.8, 30.5, 26.4, 21.9],
                 [33.1, 29.6, 18.4, 24.0, 27.8],
                 [20.2, 23.5, 31.9, 28.1, 22.6]])
```
## Task 1

Print the shape of data. Then compute and print the mean temperature per station (one value per row).

```python3
print("Shape:", data.shape)
mean_per_station = data.mean(axis=1)
print("Mean temperature per station:", mean_per_station)
```

**output:**
```terminal
Shape: (4, 5)
Mean temperature per station: [25.3  23.78 26.58 25.26]
```

## Task 2

Using a boolean mask, extract all temperature readings above 28.0°C and print them as a 1D array.

```python3
mask = data > 28.0
above_28 = data[mask]
print("Temperatures above 28.0°C:", above_28)
```

**output:**
```terminal
Temperatures above 28.0°C: [31.2 28.7 30.5 33.1 29.6 31.9 28.1]
```

## Task 3

Normalize the entire data array to the range [0, 1] using the formula below and print the result rounded to 2 decimal places:

>
>normalized = (data - data.min()) / (data.max() - data.min())
>

```python
normalized = (data - data.min()) / (data.max() - data.min())
print("Normalized data (rounded to 2 decimal places):")
print(np.round(normalized, 2))
```

**output:**
```terminal
Normalized data (rounded to 2 decimal places):
[[0.33 0.11 0.88 0.72 0.49]
 [0.   0.35 0.84 0.58 0.29]
 [1.   0.78 0.07 0.42 0.66]
 [0.18 0.39 0.92 0.68 0.34]]
```
