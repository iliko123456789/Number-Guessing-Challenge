def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "error"
    else:
        return x / y
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")
    num_1 = float(input("enter first number: "))
    num_2 = float(input("enter second number: "))
    
    if choice == "1":
        print("Result:", add(num_1, num_2))
    elif choice == "2":
        print("Result:", subtract(num_1, num_2))
    elif choice == "3":
        print("Result:", multiply(num_1, num_2))
    elif choice == "4":
        print("Result:", divide(num_1, num_2))
    else:
        print("invalid input")
calculator()