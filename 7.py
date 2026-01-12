import math
import uuid
import random
import string
from datetime import datetime

# --- 1. Datetime and Time Operations ---
def datetime_operations():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Displays current system date and time
            print(f"Current Date and Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        elif choice == '2':
            d1 = input("Enter the first date (YYYY-MM-DD): ")
            d2 = input("Enter the second date (YYYY-MM-DD): ")
            try:
                date1 = datetime.strptime(d1, "%Y-%m-%d")
                date2 = datetime.strptime(d2, "%Y-%m-%d")
                # Calculates absolute difference in days
                print(f"Difference: {abs((date2 - date1).days)} days")
            except ValueError:
                print("Invalid format! Use YYYY-MM-DD.")
        elif choice == '3':
            fmt = input("Enter format (e.g., %A, %B %d, %Y): ")
            try:
                print(f"Formatted Date: {datetime.now().strftime(fmt)}")
            except Exception as e:
                print(f"Error in format: {e}")
        elif choice == '4':
            break

# --- 2. Mathematical Operations ---
def math_operations():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            n = int(input("Enter a number: "))
            print(f"Factorial: {math.factorial(n)}")
        elif choice == '2':
            p = float(input("Enter principal amount: "))
            r = float(input("Enter rate of interest (in %): "))
            t = float(input("Enter time (in years): "))
            # Formula: A = P(1 + r/100)^t
            amount = p * (pow((1 + r / 100), t))
            print(f"Total Amount: {amount:.2f}")
            print(f"Compound Interest: {(amount - p):.2f}")
        elif choice == '3':
            angle = float(input("Enter angle in degrees: "))
            rad = math.radians(angle)
            print(f"Sin: {math.sin(rad):.4f}, Cos: {math.cos(rad):.4f}, Tan: {math.tan(rad):.4f}")
        elif choice == '4':
            print("1. Circle  2. Rectangle")
            shape = input("Select shape: ")
            if shape == '1':
                rad = float(input("Enter radius: "))
                print(f"Area of Circle: {math.pi * rad**2:.2f}")
            elif shape == '2':
                l = float(input("Length: "))
                w = float(input("Width: "))
                print(f"Area of Rectangle: {l * w:.2f}")
        elif choice == '5':
            break

# --- 3. Random Data Generation ---
def random_data_generation():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            start = int(input("Enter start range: "))
            end = int(input("Enter end range: "))
            print(f"Random Number: {random.randint(start, end)}")
        elif choice == '2':
            size = int(input("Enter list size: "))
            r_list = [random.randint(1, 100) for _ in range(size)]
            print(f"Random List: {r_list}")
        elif choice == '3':
            length = int(input("Enter password length: "))
            chars = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(chars) for _ in range(length))
            print(f"Generated Password: {password}")
        elif choice == '4':
            otp = random.randint(100000, 999999)
            print(f"Your 6-digit OTP: {otp}")
        elif choice == '5':
            break

# --- 5. File Operations ---
def file_operations():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter file name: ")
            # Simply creates an empty file
            open(name, 'w').close()
            print("File created successfully!")
        elif choice == '2':
            name = input("Enter file name: ")
            data = input("Enter data to write: ")
            with open(name, 'w') as f:
                f.write(data)
            print("Data written successfully!")
        elif choice == '3':
            name = input("Enter file name: ")
            try:
                with open(name, 'r') as f:
                    print(f"File Content:\n{f.read()}")
            except FileNotFoundError:
                print("File not found!")
        elif choice == '4':
            name = input("Enter file name: ")
            data = input("Enter data to append: ")
            with open(name, 'a') as f:
                f.write("\n" + data)
            print("Data appended successfully!")
        elif choice == '5':
            break

# --- MAIN MENU ---
def main_menu():
    while True:
        print("\n------------------------------")
        print("Welcome to Multi-Utility Toolkit")
        print("------------------------------")
        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            datetime_operations()
        elif choice == '2':
            math_operations()
        elif choice == '3':
            random_data_generation()
        elif choice == '4':
            # Generates a random version-4 UUID
            print(f"Generated UUID: {uuid.uuid4()}")
        elif choice == '5':
            file_operations()
        elif choice == '6':
            mod_name = input("Enter module name to explore: ")
            try:
                module = __import__(mod_name)
                print(f"Available Attributes in {mod_name} module:")
                print(dir(module))
            except ModuleNotFoundError:
                print("Module not found!")
        elif choice == '7':
            print("Thank you for using the multi utility toolkit!")
            break
        else:
            print("Invalid input, please choose 1-7.")

if __name__ == "__main__":
    main_menu()
