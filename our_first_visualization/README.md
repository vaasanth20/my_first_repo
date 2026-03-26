# Our First Visualization - Exploring Restaurant Tips

```pyhton3
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
tips = sns.load_dataset("tips")
print(tips.head())
```

```terminal
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
```

## Task 1 — Your First Matplotlib Chart

Using Matplotlib, create a bar chart that shows the total tip amount collected on each day of the week.

- x-axis: day, y-axis: total sum of tip

- Add a title, x-label, and y-label

- Set the figure size to (8, 5) using plt.figure(figsize=(8, 5))

- Call plt.show() to display the chart

Hint: Use tips.groupby("day")["tip"].sum() to get the total tips per day before plotting.

**This chart aggregates the data to show which day of the week brings in the most tips in total.**

```python3
# Aggregate the data
daily_tips = tips.groupby("day", observed=True)["tip"].sum()

# Create the plot
plt.figure(figsize=(8, 5))
plt.bar(daily_tips.index, daily_tips.values, color='skyblue', edgecolor='navy')

# Customization
plt.title("Total Tips Collected by Day of the Week")
plt.xlabel("Day of the Week")
plt.ylabel("Total Tip Amount ($)")

plt.show()
```
<img width="640" height="433" alt="image" src="https://github.com/user-attachments/assets/2576388d-bf68-421b-856b-e2d734bc16fd" />

## Task 2 - Seaborn Histogram

Using Seaborn, create a histogram of the tip column to see how tip amounts are distributed across all customers.

- Set bins=20
- Overlay a KDE curve on the histogram
- Add the title: "Distribution of Tip Amounts"
- Call plt.show() to display the chart

In a markdown cell below your chart, write 2–3 sentences describing what the chart tells you — for example: where most tips fall, whether the distribution is skewed, and what the KDE line adds to the histogram.

**Histograms help us understand the "shape" of our data—in this case, how much people typically tip.**

```python3
plt.figure(figsize=(8, 5))
sns.histplot(tips['tip'], bins=20, kde=True, color='teal')

# Customization
plt.title("Distribution of Tip Amounts")
plt.xlabel("Tip Amount ($)")
plt.ylabel("Frequency")

plt.show()
```

<img width="640" height="433" alt="image" src="https://github.com/user-attachments/assets/bee1bc66-03c2-403d-b035-5228f9feb993" />

**Analysis:**


The histogram shows that the distribution of tip amounts is right-skewed, meaning most tips fall into a lower range (typically between $2 and $4), while a few exceptionally high tips pull the "tail" to the right. The KDE (Kernel Density Estimate) line adds a smooth curve that helps visualize the underlying probability density, making it easier to see the peaks and the overall shape of the distribution without being distracted by the individual bins.

## Task 3 — Seaborn Scatter Plot

Using Seaborn, create a scatter plot to explore the relationship between the total bill and the tip amount.

- x-axis: total_bill, y-axis: tip
- Color the points by day using the hue parameter
- Add the title: "Total Bill vs Tip Amount"
- Call plt.show() to display the chart

In a markdown cell below, write 1–2 sentences describing any pattern you notice — for example, does a higher bill generally lead to a higher tip?

**Scatter plots are the best way to see if two continuous variables (like bill size and tip amount) move together.**

```python3
plt.figure(figsize=(8, 5))
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day")

# Customization
plt.title("Total Bill vs Tip Amount")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip Amount ($)")

plt.show()
```
<img width="640" height="433" alt="image" src="https://github.com/user-attachments/assets/6a20da9c-ae63-4b1b-903b-3b234cec7894" />

**Analysis:**

There is a clear positive correlation between the total bill and the tip amount; as the bill increases, the tip generally increases as well. However, the "spread" of the points increases for larger bills, suggesting that while big spenders often tip more, their tipping percentages are more variable than those with smaller bills.


