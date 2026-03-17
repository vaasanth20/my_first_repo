# Question: Data Merging and Lookup Operations with Pandas

You are a data analyst at an e-learning platform. You have been given multiple datasets containing student information, course enrollments, and exam scores. Your task is to merge these datasets, handle missing values, perform lookup operations, and generate insights using different join types.

## Task 1: Data Preparation and Missing Value Handling (30 points)
Create the following three DataFrames:

```python3
import pandas as pd
import time as time

students_data = {
    'student_id': [101, 102, 103, 104, 105, 106, 107],
    'name': ['Alice', 'Bob', None, 'David', 'Emma', 'Frank', 'Grace'],
    'email': ['alice@email.com', 'bob@email.com', 'charlie@email.com', None, 'emma@email.com', 'frank@email.com', 'grace@email.com'],
    'city': ['Mumbai', 'Delhi', 'Bangalore', 'Mumbai', None, 'Chennai', 'Delhi']
}

enrollments_data = {
    'student_id': [101, 102, 103, 105, 108, 109],
    'course_name': ['Python', 'Data Science', 'Python','Machine Learning', 'AI', 'Python'],
    'enrollment_date': ['2024-01-15', '2024-01-20', '2024-02-01','2024-02-10', '2024-02-15', '2024-03-01']
}

scores_data = {
    'student_id': [101, 102, 104, 105, 106],
    'exam_score': [85, 92, 78, 88, 95]
}
```
Tasks:

  - Create all three DataFrames
    **Code :**
    ```python3
    students = pd.DataFrame(students_data)
    enrollments = pd.DataFrame(enrollments_data)
    scores = pd.DataFrame(scores_data)
    print(students)
    print("-"*60)
    print(enrollments)
    print("-"*60)
    print(scores)
    ```
    **Output :**
    ```terminal
    student_id   name              email       city
    0         101  Alice    alice@email.com     Mumbai
    1         102    Bob      bob@email.com      Delhi
    2         103   None  charlie@email.com  Bangalore
    3         104  David               None     Mumbai
    4         105   Emma     emma@email.com       None
    5         106  Frank    frank@email.com    Chennai
    6         107  Grace    grace@email.com      Delhi
    ------------------------------------------------------------
    student_id       course_name enrollment_date
    0         101            Python      2024-01-15
    1         102      Data Science      2024-01-20
    2         103            Python      2024-02-01
    3         105  Machine Learning      2024-02-10
    4         108                AI      2024-02-15
    5         109            Python      2024-03-01
    ------------------------------------------------------------
    student_id  exam_score
    0         101          85
    1         102          92
    2         104          78
    3         105          88
    4         106          95
    ```
  
  - For the students DataFrame:
  
    - Display null value count and percentage for each column
        **Code :**
        ```python3
        null_count = students.isnull().sum()
        null_pct   = (null_count / len(students) * 100).round(2)
        
        null_report = pd.DataFrame({
            'Null Count':      null_count,
            'Null Percentage': null_pct.astype(str) + '%'
        })
        print(null_report)
        ```
        
        **Output :**
        ```terminal
        Null Count Null Percentage
        student_id           0            0.0%
        name                 1          14.29%
        email                1          14.29%
        city                 1          14.29%
        ```
    - Fill missing 'city' values with 'Unknown'
        **Code :**
        ```python3
        students['city'] = students['city'].fillna('Unknown')   # Emma → 'Unknown'
        ```
    
    - Drop rows where 'name' is missing
        **Code :**
        ```python3
        students = students.dropna(subset=['name'])              # drop Charlie (103)
        ```
    
  - Display the cleaned students DataFrame
        **Code :**
        ```python3
        print(students.to_string(index=False))
        ```
    
        **Output :**
        ```terminal
        student_id  name           email    city
        101     Alice alice@email.com  Mumbai
        102     Bob   bob@email.com   Delhi
        104     David            None  Mumbai
        105     Emma  emma@email.com Unknown
        106     Frank frank@email.com Chennai
        107     Grace grace@email.com   Delhi
        ```

## Task 2: Multiple Join Operations (40 points)
Perform the following join operations and answer questions:

- Inner Join: Merge students and enrollments on student_id
    **Code :**
    ```python3
    pd.merge(students, enrollments, on='student_id', how='inner')
    ```
    
    **Output :**
    ```terminal    
        student_id	name	email	city	course_name	enrollment_date
    0	101	Alice	alice@email.com	Mumbai	Python	2024-01-15
    1	102	Bob	bob@email.com	Delhi	Data Science	2024-01-20
    2	105	Emma	emma@email.com	Unknown	Machine Learning	2024-02-10

    ```

  - How many students appear in the result?
    >
    > Rows in result: 3
    >
    
  - Which students from the students table are excluded and why?
    >
    > Excluded students :-    David (104), Frank (106), Grace (107)
    > Why excluded :-   Their student_ids have no matching record in the enrollments table — inner join keeps only the intersection.
    > 

- Left Join: Merge students and enrollments on student_id
    **Code :**
    ```python3
    pd.merge(students, enrollments, on='student_id', how='left')
    ```
    
    **Output :**
    ```terminal
        student_id	name	email	city	course_name	enrollment_date
    0	101	Alice	alice@email.com	Mumbai	Python	2024-01-15
    1	102	Bob	bob@email.com	Delhi	Data Science	2024-01-20
    2	104	David	None	Mumbai	NaN	NaN
    3	105	Emma	emma@email.com	Unknown	Machine Learning	2024-02-10
    4	106	Frank	frank@email.com	Chennai	NaN	NaN
    5	107	Grace	grace@email.com	Delhi	NaN	NaN
    ```

  - How many total rows are in the result?
    >
    > Total rows: 6 (all students are preserved
    >
    
  - Which students have null values in course_name and why?
    >
    > Null course_name :-    David (104), Frank (106), Grace (107)
    > Why null :-    These students exist in students but have no enrollment record. Left join keeps all left-table rows and fills unmatched right-side columns with NaN.
    >

- Right Join: Merge students and enrollments on student_id
    **Code :**
    ```python3
    pd.merge(students, enrollments, on='student_id', how='right')
    ```
    
    **Output :**
    ```terminal
    
        student_id	name	email	city	course_name	enrollment_date
    0	101	Alice	alice@email.com	Mumbai	Python	2024-01-15
    1	102	Bob	bob@email.com	Delhi	Data Science	2024-01-20
    2	103	NaN	NaN	NaN	Python	2024-02-01
    3	105	Emma	emma@email.com	Unknown	Machine Learning	2024-02-10
    4	108	NaN	NaN	NaN	AI	2024-02-15
    5	109	NaN	NaN	NaN	Python	2024-03-01

    ```

  - How many total rows are in the result?
    >
    > Total rows :-   6 (all enrollment records are preserved)
    >
    
  - Which student_ids appear in the result but don't have student names?
    >
    > student_ids with null name :-   103, 108, 109
    > Why null :-   These IDs exist only in enrollments.  student_id 103 was dropped during cleaning (null name), and
    > 108/109 were never in the students table at all. The right join preserves them, but student info is NaN.
    >

- Full Outer Join: Merge students and enrollments on student_id
    **Code :**
    ```python3
    outer = pd.merge(students, enrollments, on='student_id', how='outer')
    outer
    ```
    
    **Output :**
    ```terminal
    
        student_id	name	email	city	course_name	enrollment_date
    0	101	Alice	alice@email.com	Mumbai	Python	2024-01-15
    1	102	Bob	bob@email.com	Delhi	Data Science	2024-01-20
    2	103	NaN	NaN	NaN	Python	2024-02-01
    3	104	David	None	Mumbai	NaN	NaN
    4	105	Emma	emma@email.com	Unknown	Machine Learning	2024-02-10
    5	106	Frank	frank@email.com	Chennai	NaN	NaN
    6	107	Grace	grace@email.com	Delhi	NaN	NaN
    7	108	NaN	NaN	NaN	AI	2024-02-15
    8	109	NaN	NaN	NaN	Python	2024-03-01

    ```

  - How many total rows are in the result?
    >
    > Total rows: 9 (union of both tables)
    >
    
  - Display rows where either student name is null OR course_name is null
    **Code :**
    ```python3
    mask = outer['name'].isnull() | outer['course_name'].isnull()
    outer[mask].reset_index(drop=True)
    ```
    
    **Output :**
    ```terminal
    
        student_id	name	email	city	course_name	enrollment_date
    0	103	NaN	NaN	NaN	Python	2024-02-01
    1	104	David	None	Mumbai	NaN	NaN
    2	106	Frank	frank@email.com	Chennai	NaN	NaN
    3	107	Grace	grace@email.com	Delhi	NaN	NaN
    4	108	NaN	NaN	NaN	AI	2024-02-15
    5	109	NaN	NaN	NaN	Python	2024-03-01

    ```

- Add indicator=True parameter to the outer join and show the distribution of merge sources (_merge column)
  
    **Code :**
    ```python3
    outer_int = pd.merge(students, enrollments, on='student_id', how='outer', indicator=True)
    print(outer_int.to_string(index=True))
    ```
    
    **Output :**
    ```terminal
       student_id   name            email     city       course_name enrollment_date      _merge
    0         101  Alice  alice@email.com   Mumbai            Python      2024-01-15        both
    1         102    Bob    bob@email.com    Delhi      Data Science      2024-01-20        both
    2         103    NaN              NaN      NaN            Python      2024-02-01  right_only
    3         104  David             None   Mumbai               NaN             NaN   left_only
    4         105   Emma   emma@email.com  Unknown  Machine Learning      2024-02-10        both
    5         106  Frank  frank@email.com  Chennai               NaN             NaN   left_only
    6         107  Grace  grace@email.com    Delhi               NaN             NaN   left_only
    7         108    NaN              NaN      NaN                AI      2024-02-15  right_only
    8         109    NaN              NaN      NaN            Python      2024-03-01  right_only
    ```
    
      
    **Code :**
    ```python3
    dist   = outer_int['_merge'].value_counts()
    legend = {
        'both':       'student_id present in BOTH tables',
        'left_only':  'student_id ONLY in students (not enrolled)',
        'right_only': 'student_id ONLY in enrollments (unknown student)'
    }
    for label, count in dist.items():
        print(f"  {str(label):<14}: {count}  --- {legend[str(label)]}")
    ```
    
    **Output :**
    ```terminal
      left_only     : 3  --- student_id ONLY in students (not enrolled)
      right_only    : 3  --- student_id ONLY in enrollments (unknown student)
      both          : 3  --- student_id present in BOTH tables
    ```


## Task 3: Lookup Operation and Automation (30 points)
- Lookup Operation:

  - Create a dictionary mapping student_id to exam_score from the scores DataFrame
    **Code :**
    ```python3
    score_dict = dict(zip(scores['student_id'], scores['exam_score']))
    ```    
  - Use the .map() function to add exam scores to the students DataFrame
      
    **Code :**
    ```python3
    students['exam_score'] = students['student_id'].map(score_dict)
    students
    ```
    
    **Output :**
    ```terminal
        	student_id	name	email	city	exam_score
    0	101	Alice	alice@email.com	Mumbai	85.0
    1	102	Bob	bob@email.com	Delhi	92.0
    2	103	None	charlie@email.com	Bangalore	NaN
    3	104	David	None	Mumbai	78.0
    4	105	Emma	emma@email.com	None	88.0
    5	106	Frank	frank@email.com	Chennai	95.0
    6	107	Grace	grace@email.com	Delhi	NaN

    ```
  - Display students with their scores (showing NaN for students without scores)
    **Code :**
    ```python3
    print(students[['student_id', 'name', 'city', 'exam_score']].to_string(index=False))
    print(f"\nStudents WITH scores    : {students['exam_score'].notna().sum()} "
          f"→ {students[students['exam_score'].notna()]['name'].tolist()}")
    print(f"Students WITHOUT scores : {students['exam_score'].isna().sum()} "
          f"→ {students[students['exam_score'].isna()]['name'].tolist()}")
    ```
    
    **Output :**
    ```terminal
     student_id  name      city  exam_score
        101 Alice    Mumbai        85.0
        102   Bob     Delhi        92.0
        103  None Bangalore         NaN
        104 David    Mumbai        78.0
        105  Emma      None        88.0
        106 Frank   Chennai        95.0
        107 Grace     Delhi         NaN
    
    Students WITH scores    : 5 → ['Alice', 'Bob', 'David', 'Emma', 'Frank']
    Students WITHOUT scores : 2 → [None, 'Grace']
    ```

- Performance Comparison:

  - Implement the same score addition using pd.merge() with a left join
    **Code :**
    ```python3
    students_map = students.copy()
    start = time.perf_counter()
    score_dict = dict(zip(scores['student_id'], scores['exam_score']))
    students_map['exam_score'] = students_map['student_id'].map(score_dict)
    map_time = (time.perf_counter() - start) * 1000
    
    print(students_map.to_string(index=False))
    print(map_time)
    ```
    
    **Output :**
    ```terminal
     student_id  name             email      city  exam_score
        101 Alice   alice@email.com    Mumbai        85.0
        102   Bob     bob@email.com     Delhi        92.0
        103  None charlie@email.com Bangalore         NaN
        104 David              None    Mumbai        78.0
        105  Emma    emma@email.com      None        88.0
        106 Frank   frank@email.com   Chennai        95.0
        107 Grace   grace@email.com     Delhi         NaN
    4.821411000193621
    ```
  - Explain why lookup (map) is more efficient than merge for this scenario
    **Code :**
    ```python3
    start = time.perf_counter()
    students_merge = pd.merge(students, scores, on='student_id', how='left')
    merge_time = (time.perf_counter() - start) * 1000
    
    print(students_merge.to_string(index=False))
    print(map_time)
    ```
    
    **Output :**
    ```terminal
     student_id  name             email      city  exam_score
        101 Alice   alice@email.com    Mumbai        85.0
        102   Bob     bob@email.com     Delhi        92.0
        103  None charlie@email.com Bangalore         NaN
        104 David              None    Mumbai        78.0
        105  Emma    emma@email.com      None        88.0
        106 Frank   frank@email.com   Chennai        95.0
        107 Grace   grace@email.com     Delhi         NaN
    4.821411000193621
    ```

- Simple Automation:

  - Create a function auto_merge(df1, df2, join_type, key_column) that:
    - Takes two DataFrames, join type, and key column as input
    - Performs the specified merge
    - Returns a dictionary with: {'result_df': merged_df, 'row_count': count, 'join_type': type}
  - Test your function with at least 2 different join types
  - 
    **Code :**
    ```python3
      def auto_merge(df1, df2, join_type, key_column):
        valid_joins = {'inner', 'left', 'right', 'outer'}
        if join_type not in valid_joins:
            raise ValueError(f"join_type must be one of {valid_joins}, got '{join_type}'")
        if key_column not in df1.columns or key_column not in df2.columns:
            raise KeyError(f"key_column '{key_column}' must exist in both DataFrames")
    
        merged_df = pd.merge(df1, df2, on=key_column, how=join_type)
        return {
            'result_df' : merged_df,
            'row_count' : len(merged_df),
            'join_type' : join_type
        }
        
        print("Automation Function Test:")
        print("-"*50)
        # Test 1: inner — only students who have an exam score
        r1 = auto_merge(students, scores, 'inner', 'student_id')
        print(f"Join Type: : '{r1['join_type']}' \n Rows in Result : {r1['row_count']} \n Result Preview:")
        print(r1['result_df'][['student_id','name','exam_score']].to_string(index=False))
        print("-"*50)
        # Test 2: left — all students, NaN for those without a score
        r2 = auto_merge(students, scores, 'left', 'student_id')
        print(f"Join Type: : '{r2['join_type']}' \n Rows in Result : {r2['row_count']} \n Result Preview:")
        print(r2['result_df'][['student_id','name','exam_score']].to_string(index=False))
        print("-"*50)
        # Test 3: outer — all students + all enrollment records
        r3 = auto_merge(students, enrollments, 'outer', 'student_id')
        print(f"Join Type: : '{r3['join_type']}' \n Rows in Result : {r3['row_count']} \n Result Preview:")
        print(r3['result_df'][['student_id','name','course_name']].to_string(index=False))
    ```

    **Output :**
    ```terminal
    Automation Function Test:
    --------------------------------------------------
    Join Type: : 'inner' 
     Rows in Result : 5 
     Result Preview:
     student_id  name  exam_score
            101 Alice          85
            102   Bob          92
            104 David          78
            105  Emma          88
            106 Frank          95
    --------------------------------------------------
    Join Type: : 'left' 
     Rows in Result : 7 
     Result Preview:
     student_id  name  exam_score
            101 Alice        85.0
            102   Bob        92.0
            103  None         NaN
            104 David        78.0
            105  Emma        88.0
            106 Frank        95.0
            107 Grace         NaN
    --------------------------------------------------
    Join Type: : 'outer' 
     Rows in Result : 9 
     Result Preview:
     student_id  name      course_name
            101 Alice           Python
            102   Bob     Data Science
            103  None           Python
            104 David              NaN
            105  Emma Machine Learning
            106 Frank              NaN
            107 Grace              NaN
            108   NaN               AI
            109   NaN           Python
    ```
