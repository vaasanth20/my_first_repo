# Name: Vasanth Dhandapani
# Roll Number: IITP_AIMLTN_2602559
# Assignment: Python Logic & Flow - Subjective Question

# Stage 2: Basic Calculator with Result Check
# -------------------------------------------
# Extends Stage 1 by checking whether the result
# is Positive, Negative, or Zero after calculation.

# Take input from the user
num1 = float(input("Enter first number: "))   # Convert input to float to support decimals
num2 = float(input("Enter second number: "))  # Convert input to float to support decimals
operator = input("Enter operator (+, -, *, /): ")  # Get the arithmetic operator

# Perform calculation based on the operator
if operator == "+":
    result = num1 + num2          # Addition

elif operator == "-":
    result = num1 - num2          # Subtraction

elif operator == "*":
    result = num1 * num2          # Multiplication

elif operator == "/":
    # Check for division by zero before dividing
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        result = None             # Set result to None to skip output
    else:
        result = num1 / num2      # Division

else:
    # If the operator is not one of the four valid ones
    print("Error: Invalid operator. Please use +, -, *, /")
    result = None                 # Set result to None to skip output

# Display result and check whether the result is greater than 0 or not
if result is not None:
    print(f"Result = {result}")   # Print the calculated result

    # Check whether the result is positive, negative, or zero
    if result > 0:
        print("Positive")         # Result is greater than zero
    elif result < 0:
        print("Negative")         # Result is less than zero
    else:
        print("Zero")             # Result is exactly zero