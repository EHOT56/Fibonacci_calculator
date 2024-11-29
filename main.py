import json
import os

HISTORY_FILE = "history.json"

def fibonacci_n(n):
    if n < 0:
        raise ValueError("Index can't be lower than 0")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def check_fibonacci(num):
    if num < 0:
        raise ValueError("Value can't be lower than 0")
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return num == b, a, b

def generate_fibonacci_up_to(limit):
    if limit < 0:
        raise ValueError("Limit must be non-negative")
    a, b = 0, 1
    sequence = [a]
    while b <= limit:
        sequence.append(b)
        a, b = b, a + b
    return sequence

def sum_of_fibonacci(n):
    if n < 0:
        raise ValueError("Index can't be lower than 0")
    a, b = 0, 1
    total = a
    for _ in range(n):
        a, b = b, a + b
        total += a
    return total

def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as file:
                history = json.load(file)
                print("History loaded successfully.")
                return history
        except (json.JSONDecodeError, IOError):
            print("Error loading history. Starting with an empty history.")
    return []

def save_history(history):
    try:
        with open(HISTORY_FILE, "w") as file:
            json.dump(history, file, indent=4)
            print("History saved successfully.")
    except IOError as e:
        print(f"Error saving history: {e}")

def menu():
    print("\n--- Fibonacci Calculator ---")
    print("1. Find the N-th Fibonacci number")
    print("2. Check if a number is a Fibonacci number")
    print("3. Generate Fibonacci sequence up to a limit")
    print("4. Sum of the first N Fibonacci numbers")
    print("5. View history")
    print("6. Clear history")
    print("7. Exit")

def main():
    history = load_history()  # Загружаем историю при старте программы
    while True:
        menu()
        choice = input("Choose an option (1-7): ")
        
        if choice == "1":
            try:
                n = int(input("Enter the index (N): "))
                result = fibonacci_n(n)
                print(f"The {n}-th Fibonacci number is {result}")
                history.append(f"Find N-th Fibonacci (N={n}): {result}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "2":
            try:
                num = int(input("Enter a number to check: "))
                is_fib, prev, next_ = check_fibonacci(num)
                if is_fib:
                    print(f"{num} is a Fibonacci number.")
                else:
                    print(f"{num} is NOT a Fibonacci number. Closest: {prev}, {next_}")
                history.append(f"Check Fibonacci ({num}): {'Yes' if is_fib else 'No'}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "3":
            try:
                limit = int(input("Enter the limit: "))
                sequence = generate_fibonacci_up_to(limit)
                print(f"Fibonacci sequence up to {limit}: {sequence}")
                history.append(f"Generate sequence up to {limit}: {sequence}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "4":
            try:
                n = int(input("Enter the range (N): "))
                total = sum_of_fibonacci(n)
                print(f"Sum of the first {n} Fibonacci numbers is {total}")
                history.append(f"Sum of first N Fibonacci (N={n}): {total}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "5":
            if history:
                print("\n--- History ---")
                for i, entry in enumerate(history, 1):
                    print(f"{i}. {entry}")
            else:
                print("\nNo history available.")
        
        elif choice == "6":
            confirm = input("Are you sure you want to clear history? (yes/no): ")
            if confirm.lower() == "yes":
                history.clear()
                save_history(history)  # Сохраняем пустую историю
                print("History cleared.")
            else:
                print("Operation cancelled.")
        
        elif choice == "7":
            save_history(history)  # Сохраняем историю перед выходом
            print("Exiting. Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
