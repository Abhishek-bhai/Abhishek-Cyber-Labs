# ==============================
# 2. Factorial Program
# ==============================

def factorial_program():
    print("\n--- Factorial Program ---")

    num = int(input("Enter a number: "))
    fact = 1

    if num < 0:
        print("Factorial does not exist for negative numbers")

    else:
        for i in range(1, num + 1):
            fact *= i

        print("Factorial =", fact)