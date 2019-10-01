# sorted beta

taskn = 0
task1 = ""
task2 = ""
task3 = ""
due1 = ""
due2 = ""
due3 = ""

stage = 1

print("Welcome!")
print("Sorted: The simple text-base task manager.")

if stage == 1:
    mode = input("Press [v] tp view tasks, or [a] to add tasks: ")
    if mode == "v":
        stage = 2
    elif mode == "a":
        stage = 3

if stage == 2:
    print("Your current tasks are: ")
    if taskn == 0:
        print("You don't have any tasks. Please add them first: ")
        stage = 3
    elif taskn == 1:
        print(task1,due1)
    elif taskn == 2:
        print(task2,due2)
    elif taskn == 3:
        print(task3,due3)
    else:
        print("Max number of tasks reached!")

if stage == 3:
    if taskn == 0:
        task1 = input("What is your task? ")
        print("Task added!")
        taskn = 1
        stage = 1
    elif taskn == 2:
        task2 = input("What is your task? ")
    elif taskn == 3:
        task3 = input("What is your task? ")
    else:
        print("Max number of tasks reached!")
        print("Would you like to view them? ")
        view = input("[y/n]")
        if view == "y":
            stage = 2