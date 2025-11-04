# Simple Calculator

print("Simple Calculator")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Operations: +  -  *  /")
op = input("Enter operation: ")

if op == '+':
    print(f"Result = {a + b}")
elif op == '-':
    print(f"Result = {a - b}")
elif op == '*':
    print(f"Result = {a * b}")
elif op == '/':
    if b != 0:
        print(f"Result = {a / b}")
    else:
        print("Division by zero not allowed!")
else:
    print("Invalid operation!")
