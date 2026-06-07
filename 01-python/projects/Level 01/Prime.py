# ==============================
# 4. Prime Number Checker
# ==============================

def prime_checker():
    print("\n--- Prime Number Checker ---")

    num = int(input("Enter number: "))

    if num <= 1:
        print("Not Prime")

    else:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print("Prime Number")

        else:
            print("Not Prime")