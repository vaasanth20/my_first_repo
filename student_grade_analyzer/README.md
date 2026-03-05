# Python: Functions & Modularity

You are building a mini student grade analyzer for a classroom system that processes student scores, evaluates performance, and generates a summary report.

## Task 1 
    Process the Scores Write a function process_scores(students) that accepts a dictionary where keys are student names and values are lists of integer scores. Calculate the average score for each student (rounded to 2 decimal places) and return a new dictionary in the format { name: average_score }.

## Task 2 
    Classify the Grades Write a function classify_grades(averages) that takes the output of Task 1 and assigns a letter grade to each student using the scale below. Return a dictionary in the format { name: (average, grade) }. Define the grading thresholds as variables inside the function — do not use global variables for them.

```
   **Average	Grade**
   90 and above	A
   75 – 89	B
   60 – 74	C
   Below 60	F
```

## Task 3 
    Generate the Report Write a function generate_report(classified, passing_avg=70) that takes the output of Task 2 and an optional passing threshold (default 70). Print a formatted report as shown below, then return the total number of students who passed. In your main block, call all three functions in sequence, each feeding its output into the next.

```
===== Student Grade Report =====
Alice     | Avg: 86.25 | Grade: B | Status: PASS
Bob       | Avg: 62.50 | Grade: C | Status: PASS
Clara     | Avg: 96.25 | Grade: A | Status: PASS
================================
Total Students : 3
Passed         : 3
Failed         : 0
```