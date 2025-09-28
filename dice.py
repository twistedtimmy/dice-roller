import random

print("🎲 Dice Roller 🎲")
sides = int(input("How many sides does the die have? "))
rolls = int(input("How many times do you want to roll? "))

for i in range(rolls):
    result = random.randint(1, sides)
    print(f"Roll {i+1}: {result}")
