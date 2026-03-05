# ------------------------------------------------------------
# Name: Vasanth Dhandapani
# Roll Number: IITP_AIMLTN_2602559
# Assignment: Python Loops & Automation - Subjective Question

#  grade_analyzer.py
#  Mini Student Grade Analyzer
#  Demonstrates: functions, dictionaries, f-strings, defaults
# ------------------------------------------------------------
# Task 1 — Process the Scores
# ------------------------------------------------------------
def process_scores(students):
    """
    Calculate the average score for each student.

    Parameters:
        students (dict): { name: [score1, score2, ...] }

    Returns:
        dict: { name: average_score }   (average rounded to 2 d.p.)
    """
    averages = {}  # Will hold {student name: average_score }

    for name, scores in students.items():
        # average score = all scores and divide by the number of scores
        avg = sum(scores) / len(scores)

        # Round to 2 decimal places before storing
        averages[name] = round(avg, 2)

    return averages

# ------------------------------------------------------------
# Task 2 — Classify the Grades
# ------------------------------------------------------------
def classify_grades(averages):
    """
    Assign grade to each student based on their average.

    Grading scale (Grades are LOCAL variables, not globals):
        A : 90 and above
        B : b/w 75 to 89
        C : b/w 60 to 74
        D : Below 60

    Parameters:
        averages (dict): { name: average_score }

    Returns:
        dict: { name: (average_score, letter_grade) }
    """

    # --- Grading thresholds defined locally inside the function ---
    Grade_A = 90   # 90 and above --> A
    Grade_B = 75   # 75 – 89      --> B
    Grade_C = 60   # 60 – 74      --> C
    # Below Grade_D --> F

    classified = {}  # Will hold { name: (avg, grade) }

    for name, avg in averages.items():
        # Determine grade by checking the score from highest to lowest
        if avg >= Grade_A:
            grade = "A"
        elif avg >= Grade_B:
            grade = "B"
        elif avg >= Grade_C:
            grade = "C"
        else:
            grade = "F"

        # Store as a tuple (average, grade)
        classified[name] = (avg, grade)

    return classified


# ------------------------------------------------------------
# Task 3 — Generate the Report
# ------------------------------------------------------------
def generate_report(classified, passing_avg=70):
    """
    Print a formatted student's grade report.

    Parameters:
        classified  (dict):  { name: (average_score, grade) }
        passing_avg (float): Minimum average to be considered passing (default 70)

    Returns:
        int: Number of students whose average >= passing_avg
    """
    passed = 0  # Counter for students who meet the passing grade

    print("===== Student Grade Report =====")
    for name, (avg, grade) in classified.items():
        # Determine pass/fail status based on the passing grade
        status = "PASS" if avg >= passing_avg else "FAIL"

        # Increment pass counter when the student passes
        if status == "PASS":
            passed += 1

        # Print student's scores with grade :the value of name is left-aligned, in a field that is 20 characters wide.
        print(f"{name:<20}| Avg: {avg:.2f} | Grade: {grade} | Status: {status}")

    total  = len(classified)   # Total number of students
    failed = total - passed    # Students who did not meet the passing grade

    print("================================")
    print(f"Total Students : {total}")
    print(f"Passed         : {passed}")
    print(f"Failed         : {failed}")
    print()  # Blank line after the report

    # Return the number of students who passed
    return passed


# Sample student data: each key is a name, value is a list of scores
students = {
    "Alice": [85, 92, 78, 90],    # Expected avg: 86.25 : B
    "Bob":   [70, 55, 68, 57],    # Expected avg: 62.50 : C
    "Clara": [98, 95, 92, 100],   # Expected avg: 96.25 : A
}

# Task 1: Compute averages from raw scores
averages = process_scores(students)

# Task 2: Classify each average into a letter grade
classified = classify_grades(averages)

# Task 3: Print the report and capture how many students passed
total_passed = generate_report(classified, 60)