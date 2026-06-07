# # ==============================
# 6. Guessing Game
# ==============================

import random

def guessing_game():
    print("\n--- Guessing Game ---")

    secret = random.randint(1, 10)

    while True:
        guess = int(input("Guess number (1-10): "))

        if guess == secret:
            print("Correct Guess!")
            break

        elif guess > secret:
            print("Too High")

        else:
            print("Too Low")