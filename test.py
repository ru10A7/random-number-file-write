import random


name = ["Nathan", "Cyntia", "John", "Dan", "Alice", "Nancy",
        "Camille", "Sacha", "Eden", "Charlie", "Lou", "Loan", "Jonathan", "Thaïs", "Maé", "Elie", "Yaël", "Cameron", "Maxence", "Morgan", "Wissem", "Claude", "Dominique", "Richard", "Tom", "Jerry", "Sam", "Clark"]


def view():
    with open("asoiu.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            student_Name, score = data.split("|")
            print("Name:", student_Name, ", Points:", score)


def add():
    for student_Name in name:
        score = random.randint(0, 20)

        with open("asoiu.txt", "a") as f:
            f.write(student_Name + "|" + str(score) + "\n")


while True:

    mode = input(
        "Would you like to add a new gradue or view existing ones (View, add), press q to quit  ? ").lower()
    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid mode.")
        continue
