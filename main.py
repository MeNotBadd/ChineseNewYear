import random
chinese_new_year_tasks = ["Give a red envelope with money to and elder!", "Help your parent's prepare dinner.", "Go shopping, you deserve it!", "Clean your house to rid it of bad omens!", "Decorate your house!", "Visit your relatives!", "Light some firecrackers!", "Eat dumplings idk...", "Stay up late to celebrate!"]

while True:
    enter = input("\nPress enter to reveal your Chinese New Year task.")
    print(random.choice(chinese_new_year_tasks))
    enter = input("\nDo you want to go again? (yes/no, default is no) ")
    if enter.lower() != "yes":
        break