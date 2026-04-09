# ML Workflow Assignment

## Task 1: Label and Data Leakage Identification

**Label (Target Variable):** `repeat_purchase_flag`

> This is the label because it is the answer we are trying to predict — did the customer come back and buy again within 30 days? Yes (1) or No (0).

**Column that introduces Data Leakage:** `discount_used_on_repeat_order`

> This column causes data leakage because it gives away information about the repeat order — but that order is exactly what we are trying to predict! We cannot know the discount on a repeat purchase before the purchase even happens. If we train the model using this column, it will look like the model is doing great, but in real life it will fail because this data won't be available at prediction time.

---

## Task 2: Two Important Steps Before Training a Model

### Step 1 — Explore the Data First (EDA)

Before jumping into any model, we should look at the data carefully — check for missing values, understand what the numbers look like, and see how many customers actually made a repeat purchase versus those who did not.

**Why it matters:** Imagine 90 out of 100 customers did NOT make a repeat purchase. If we skip this check and train a model, it might just predict "No" for everyone and still look 90% accurate — which is useless. Exploring the data first helps us catch these problems early.

### Step 2 — Clean and Prepare the Data

This means fixing missing values, removing the leaky column, and making sure all the data is in a format the model can actually use.

**Why it matters:** Even a powerful model like gradient boosting cannot make sense of messy or misleading data. If we feed it bad data, it will learn the wrong patterns. Cleaning the data first makes sure the model is learning something real and useful — not just noise or cheating on the answers.
