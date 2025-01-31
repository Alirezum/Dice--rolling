import random


def roll_dice():
    dice_drawing = {
        1: (
            "-----",
            "| 1 |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "| 2 |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o3 |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "| 4 |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o5o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o6o|",
            "|o o|",
            "-----",
        ),
    }
    roll = input("Roll dice (yes/no)?:")

    while roll.lower() == "yes":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print(f"dice roll {dice1} and dice roll {dice2}")
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))

        roll = input("roll again(yas/no)")


roll_dice()
