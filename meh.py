def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b


print("Ugh. Welcome to the Meh-culator. I'm really tired so hurry up")

sure = input("Are you sure you need to solve something because i don't want to do anything(Y/N): ").upper()

if sure == "Y":
    done = "N"
    while done == "N":
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        operation = input("What do you want to do? (+, -, *, /): ")

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
                print("Oh brilliant. Divide by zero. That's impossible you stupid.")
            else:
                print(f"Here. The quotient is {result}.")
        else:
            print("Seriously? That's not even an option. Try reading next time.")

        done = input("Are we done now? (Y/N): ").upper()
    
    print("Finally! I can rest. Bye.")
elif sure == "N":
    print("Finally! Someone who doesn’t want math. Thank you for sparing me.")
else:
    print("Ugh. You can’t even type Y or N correctly. This is hopeless.")
