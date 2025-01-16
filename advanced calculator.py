def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
def square(x):
    return x ** 2
def square_root(x):
    return x ** 0.5

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square")
print("6. Squire Root")

choice = input("Enter choice(1/2/3/4/5/6): ")

num1 = float(input("Enter first number: "))

if choice in ['1', '2', '3', '4']:
    num2 = float(input("Enter second number: "))

if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
elif choice =='5':
    print(f"{num1} squared = {square(num1)}")
elif choice == '6':
    print(f"Square root of {num1} = {square_root(num1)}")
else:
        print("Invalid input")

        


