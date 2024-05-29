iteration = 0

while iteration <= 5:
    iteration += 1

    answer = input("Choose Wisely: (yes/no): ")

    if answer == "yes":
        print("Iteration", iteration,":", "nice, let's go again.")

    elif answer == "no":
        print("Have a Good Day!")
        break

    else:
        print("Invalid Input, Try Again")

