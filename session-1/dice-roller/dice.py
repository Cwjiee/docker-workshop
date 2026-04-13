import random

def roll_dice(num_dice=1, sides=6):
    """Roll one or more dice and return the results."""
    results = []
    for _ in range(num_dice):
        results.append(random.randint(1, sides))
    return results

def main():
    print("Welcome to the Dice Roller!")
    print("-" * 30)

    while True:
        try:
            num_dice = input("\nHow many dice to roll? (or 'q' to quit): ").strip()
            if num_dice.lower() == "q":
                print("Thanks for playing!")
                break

            num_dice = int(num_dice)
            if num_dice < 1:
                print("Please enter at least 1.")
                continue

            results = roll_dice(num_dice)
            print(f"\nRolling {num_dice} dice...")
            print(f"Results: {results}")
            print(f"Total:   {sum(results)}")

        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
