# Define a function that adds two numbers
def add(a, b):
    return a + b

# Define a function that subtracts the second number from the first
def subtract(a, b):
    return a - b

# Define a function that multiplies two numbers
def multiply(a, b):
    return a * b

# Define a function that divides two numbers
def divide(a, b):
    # Prevent division by zero (which causes an error)
    if b == 0:
        return None  # Return None if division by zero happens
    return a / b  # Otherwise return the result of the division


# Print a lazy greeting message to the user
print("Ugh. Welcome to the Meh-culator. I'm really tired so hurry up")

# Ask the user if they want to do any calculations
sure = input("Are you sure you need to solve something because I don't want to do anything (Y/N): ").upper()

# If the user says "Y", they want to do math
if sure == "Y":
    done = "N"  # Initialize loop control variable

    # Keep looping until the user says they're done
    while done == "N":
        # Get two numbers from the user
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        # Ask what operation they want to perform
        operation = input("What do you want to do? (+, -, *, /): ")

        # Perform the chosen operation and display the result
        if operation == "+":
            result = add(a, b)
            print(f"Fine. The sum is {result}.")
        elif operation == "-":
            result = subtract(a, b)
            print(f"Whatever. The difference is {result}.")
        elif operation == "*":
            result = multiply(a, b)
            print(f"Wow, multiplying. The product is {result}.")
        elif operation == "/":
            result = divide(a, b)
            if result is None:
                # Handle division by zero with a sarcastic message
                print("Oh brilliant. Divide by zero. That's impossible, you stupid.")
            else:
                print(f"Here. The quotient is {result}.")
        else:
            # Handle invalid operation input
            print("Seriously? That's not even an option. Try reading next time.")

        # Ask if the user wants to continue or stop
        done = input("Are we done now? (Y/N): ").upper()
    
    # When done, print goodbye message
    print("Finally! I can rest. Bye.")

# If the user says "N", skip doing math
elif sure == "N":
    print("Finally! Someone who doesn’t want math. Thank you for sparing me.")

# If the user enters something other than Y or N
else:
    print("Ugh. You can’t even type Y or N correctly. This is hopeless.")
