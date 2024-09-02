#1
number = 10
if number > 0:
    print("The number is postive.")
else:
    print("The number is non-positive.")

#2
number = 0
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#3
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "c"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Your grade is: {grade}")

#4
number = 7
result = "even" if number % 2 == 0 else "odd"
print(f"The number is {result}")

#5
num1 = 10
num2 = 5
operator = "+"

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result - num1 * num2
elif operator == "/":
    result = num1 / num2 if num2 != 0 else "Error: Division by zero."
else:
    result = "Error: Invalid operator."

print(f"Result: {result}")


