# from code import multiplication

from addition import add_2_numbers
from multiplication import multiplication 
from subtraction import subtraction 

choice = int(input("Choices of Operation:\n1. Addition\n2. Subtraction\n3. Multiplication\nEnter Choice: "))

a = int(input("\nEnter Number 1: "))
b = int(input("\nEnter Number 2: "))

print(choice)
if choice == 1: 
    result = add_2_numbers(a, b)
    print(f"Result is {result}")
if choice == 2: 
    result = subtraction(a, b)
    print(f"Result is {result}")
if choice == 3: 
    result = multiplication(a, b)
    print(f"Result is {result}")


