import random

x = "y"

while x == "y":

    no = random.randint(1, 6)

    if no == 1:
        print(
            " ┌─────────┐\n",
            "│         │\n",
            "│    ●    │\n",
            "│         │\n",
            "└─────────┘",
        )
        print("\nYou rolled 1!")
    if no == 2:
        print(
            " ┌─────────┐\n",
            "│  ●      │\n",
            "│         │\n",
            "│      ●  │\n",
            "└─────────┘\n",
        )
        print("\nYou rolled 2!")
    if no == 3:
        print(
            " ┌─────────┐\n",
            "│  ●      │\n",
            "│    ●    │\n",
            "│      ●  │\n",
            "└─────────┘",
        )
        print("\nYou rolled 3!")
    if no == 4:
       print(
           " ┌─────────┐\n",
           "│  ●   ●  │\n",
           "│         │\n",
           "│  ●   ●  │\n",
           "└─────────┘",
       )
       print("\nYou rolled 4!")
    if no == 5:
       print(
           " ┌─────────┐\n",
           "│  ●   ●  │\n",
           "│    ●    │\n",
           "│  ●   ●  │\n",
           "└─────────┘",
       )
       print("\nYou rolled 5!")
    if no == 6:
        print(
            " ┌─────────┐\n",
            "│  ●   ●  │\n",
            "│  ●   ●  │\n",
            "│  ●   ●  │\n",
            "└─────────┘",
        )
        print("\nYou rolled 6!")

    x = input("\nPress y to roll again and n to exit: ")
    print("\n")
