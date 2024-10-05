def calculator():
    print("Welcome to the Addition and Subtraction Calculator!")

    while True:
        try:
            # Input numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Choose operation
            operation = input("Choose the operation (+ or -): ")

            if operation == "+":
                result = num1 + num2
                print(f"Result of addition: {result}")
            elif operation == "-":
                result = num1 - num2
                print(f"Result of subtraction: {result}")
            else:
                print("Invalid operation. Please choose + or -.")

        except ValueError:
            print("Please enter valid numbers.")

        # Ask if the user wants to continue
        continue_choice = input("Do you want to perform another operation? (yes/no): ")
        if continue_choice.lower() != "yes":
            break


calculator()
