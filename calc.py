class Calculator:
    # Constructor of the class, initializing with used variables.
    def __init__(self):
        self.last_result = 0

    # Method to add two numbers.
    def add(self, x, y):
        self.last_result = x + y
        return self.last_result

    # Method to subtract two numbers.
    def subtract(self, x, y):
        self.last_result = x - y
        return self.last_result

    # Method to multiply two numbers.
    def multiply(self, x, y):
        self.last_result = x * y
        return self.last_result

    # Method to divide two numbers.
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        self.last_result = x / y
        return self.last_result

    # Method to display calculator options.
    @staticmethod
    def display_options():
        print("\nOptions:")
        print("Enter '+' to add two numbers")
        print("Enter '-' to subtract two numbers")
        print("Enter '*' to multiply two numbers")
        print("Enter '/' to divide two numbers")
        print("Enter 'quit' to end the program")


# Function for console-based interaction with the user.
def main():
    calculator = Calculator()
    while True:
        # Display the menu options.
        Calculator.display_options()
        user_input = input(": ")

        if user_input == "quit":
            # Quit the program if the user inputs 'quit'.
            print("Thank you for using the calculator.")
            break
        elif user_input in ("+", "-", "*", "/"):
            # Ask the user for input if a valid operation is selected.
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Unknown input")
                continue

            # Perform the operation and display the result.
            try:
                if user_input == "+":
                    print(f"The result is: {calculator.add(num1, num2)}")
                elif user_input == "-":
                    print(f"The result is: {calculator.subtract(num1, num2)}")
                elif user_input == "*":
                    print(f"The result is: {calculator.multiply(num1, num2)}")
                elif user_input == "/":
                    print(f"The result is: {calculator.divide(num1, num2)}")
            except ValueError as e:
                print(e)
        else:
            # Inform the user of unknown input.
            print("Unknown input")


if __name__ == "__main__":
    main()
