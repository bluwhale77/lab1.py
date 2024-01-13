# lab1.py

# Starter code for lab 1 in ICS 32 Programming with Software Libraries in Python
# Please see the README in this repository for the requirements of this lab exercise

# Bryant Lu
# Lubg@uci.edu
# 83665984

print("Welcome to ICS 32 PyCalc!")

print()

operand1 = int(input("Enter your first operand: "))
operand2 = int(input("Enter your second operand: "))
operator = input("Enter your desired operator (+, -, or x): ")

print()

if operator == '+':
    answer = operand1 + operand2
elif operator == '-':
    answer = operand1 - operand2
elif operator == 'x':
    answer = operand1 * operand2
    
print(f'The result of your calculation is: {answer}')
