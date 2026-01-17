from src.calculation import add, subtract, multiply, divide

while True:
    print("\nChoose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    userChoice = input("Choose (1-5): ")

    if userChoice == "5":
        print("\nThank you for using our product.")
        break

    try:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("\nInvalid input, please enter a valid number.")

    if userChoice == "1":
        print(add(num1, num2))
    
    if userChoice == "2":
        print(subtract(num1, num2))

    if userChoice == "3":
        print(multiply(num1, num2)) 
    
    if userChoice == "4":
        print(divide(num1, num2))