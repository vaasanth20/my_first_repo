# Stage 1: Basic Calculator
# -------------------------
# This program takes two numbers and an operator
# from the user and displays the calculated result.
# It handles invalid operators and division by zero.

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

# Display the result only if calculation was successful
if result is not None:
    print(f"Result = {result}")
