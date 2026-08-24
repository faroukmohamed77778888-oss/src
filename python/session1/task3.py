def calculator():

    while True:

        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("choose: ")

        if choice == "5":
            print("thank you")
            break

        if choice == "1":
            print("Add")

        elif choice == "2":
            print("Subtract")

        elif choice == "3":
            print("Multiply")

        elif choice == "4":
            print("Divide")

        else:
            print("wrong choice")
            continue

        num1 = float(input("enter first number: "))
        num2 = float(input("enter second number: "))

        if choice == "1":
            result = num1 + num2

        elif choice == "2":
            result = num1 - num2

        elif choice == "3":
            result = num1 * num2

        elif choice == "4":
            if num2 == 0:
                print("cant divide by zero")
                continue

            result = num1 / num2

        print("result is:", result)

        again = input("do you want again yes/no: ")

        if again == "no":
            print("thank you")
            break


calculator()