# Question: Data Merging and Lookup Operations with Pandas

You are a data analyst at an e-learning platform. You have been given multiple datasets containing student information, course enrollments, and exam scores. Your task is to merge these datasets, handle missing values, perform lookup operations, and generate insights using different join types.

## Task 1: Data Preparation and Missing Value Handling (30 points)
Create the following three DataFrames:

```pyhon3
Students DataFrame:

students_data = {
    'student_id': [101, 102, 103, 104, 105, 106, 107],
    'name': ['Alice', 'Bob', None, 'David', 'Emma', 'Frank', 'Grace'],
    'email': ['alice@email.com', 'bob@email.com', 'charlie@email.com', None, 'emma@email.com', 'frank@email.com', 'grace@email.com'],
    'city': ['Mumbai', 'Delhi', 'Bangalore', 'Mumbai', None, 'Chennai', 'Delhi']
}
Enrollments DataFrame:

enrollments_data = {
    'student_id': [101, 102, 103, 105, 108, 109],
    'course_name': ['Python', 'Data Science', 'Python', 'Machine Learning', 'AI', 'Python'],
    'enrollment_date': ['2024-01-15', '2024-01-20', '2024-02-01', '2024-02-10', '2024-02-15', '2024-03-01']
}
Scores DataFrame:

scores_data = {
    'student_id': [101, 102, 104, 105, 106],
    'exam_score': [85, 92, 78, 88, 95]
}
```
Tasks:

  - Create all three DataFrames
  
  - For the students DataFrame:
  
    - Display null value count and percentage for each column
    
    - Fill missing 'city' values with 'Unknown'
    
    - Drop rows where 'name' is missing
    
  - Display the cleaned students DataFrame

## Task 2: Multiple Join Operations (40 points)
Perform the following join operations and answer questions:

- Inner Join: Merge students and enrollments on student_id

  - How many students appear in the result?
  - Which students from the students table are excluded and why?

- Left Join: Merge students and enrollments on student_id

  - How many total rows are in the result?
  - Which students have null values in course_name and why?

- Right Join: Merge students and enrollments on student_id

  - How many total rows are in the result?
  - Which student_ids appear in the result but don't have student names?

- Full Outer Join: Merge students and enrollments on student_id

  - How many total rows are in the result?
  - Display rows where either student name is null OR course_name is null

- Add indicator=True parameter to the outer join and show the distribution of merge sources (_merge column)

## Task 3: Lookup Operation and Automation (30 points)
- Lookup Operation:

  - Create a dictionary mapping student_id to exam_score from the scores DataFrame
  - Use the .map() function to add exam scores to the students DataFrame
  - Display students with their scores (showing NaN for students without scores)

- Performance Comparison:

  - Implement the same score addition using pd.merge() with a left join
  - Explain why lookup (map) is more efficient than merge for this scenario

- Simple Automation:

  - Create a function auto_merge(df1, df2, join_type, key_column) that:
    - Takes two DataFrames, join type, and key column as input
    - Performs the specified merge
    - Returns a dictionary with: {'result_df': merged_df, 'row_count': count, 'join_type': type}
  - Test your function with at least 2 different join types
