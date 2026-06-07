# ==============================
# 5. Pattern Printing Program
# ==============================

def pattern_printing():
    print("\n--- Pattern Printing ---")

    rows = int(input("Enter number of rows: "))

# Normal pattern

    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    print("\n")

# Inverted pattern

    for i in range(rows - 1, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    print("\n")