# Name: Vasanth Dhandapani
# Roll Number: IITP_AIMLTN_2602559
# Assignment: Python Logic & Flow - Subjective Question

# Stage 3: Student Grade Calculator
# ----------------------------------
# This program takes a student's name and marks
# in 3 subjects, then calculates the total,
# percentage, and final grade based on the
# grade logic below:
#   A : percentage >= 75%
#   B : percentage >= 60%
#   C : percentage >= 40%
#   F : percentage <  40%

# --- Take student details as input ---
name = input("Enter student name: ")  # Student's name (string)

# Marks for each subject (converted to float to allow decimal values)
mark1 = float(input("Enter marks for Subject 1 (0-100): "))
mark2 = float(input("Enter marks for Subject 2 (0-100): "))
mark3 = float(input("Enter marks for Subject 3 (0-100): "))

# --- Calculate total marks ---
# Sum of all three subject marks; maximum possible is 300
total = mark1 + mark2 + mark3

# --- Calculate percentage ---
# Formula: (total marks / maximum marks) * 100
percentage = (total / 300) * 100

# --- Determine grade based on percentage ---
if percentage >= 75:
    grade = "A"       # Distinction / excellent performance
elif percentage >= 60:
    grade = "B"       # Good performance
elif percentage >= 40:
    grade = "C"       # Average / passing performance
else:
    grade = "F"       # Fail — below minimum passing percentage

# --- Display the results ---
print(name)                              # Print student name
print(f"Total: {total}/300")            # Total marks out of 300
print(f"Percentage: {round(percentage,1)}%")     # Calculated percentage
print(f"Grade: {grade}")                # Final grade