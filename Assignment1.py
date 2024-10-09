''''
Task 1: Create functions for each arithmetic operation.
'''

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1a, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


'''
Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.
'''

user_operation = input("Which operation would you like to perform? (add, subtract, multiply, or divide): ")


num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))

'''
Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling set up to prevent an error from showing in the console.

'''

user_operation = input("Which operation would you like to perform? (add, subtract, multiply, or divide): ")

options = ["add", "subtract", "multiply", "divide"]

while user_operation not in options:
    print("please enter a valid option\n")
    user_operation = input("Which operation would you like to perform? (add, subtract, multiply, or divide): ")
    
    
num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))
    
while user_operation == "divide" and num2 == 0:
    print("You cannot divide a nunmber by 0, please enter another number to divide by: ")
    num2 = int(input("Please enter your second number: "))
    

if user_operation == "add":
    print(add(num1, num2))
elif user_operation == "subtract":
    print(subtract(num1, num2))
elif user_operation == "multiply":
   print(multiply(num1, num2))
elif user_operation == "divide":
    print(divide(num1, num2))


