# ==============================
# 3. Palindrome Checker Program
# ==============================

def palindrome_checker():
    print("\n--- Palindrome Checker ---")

    text = input("Enter text or number: ")

    if text == text[::-1]:
        print("Palindrome")

    else:
        print("Not Palindrome")
