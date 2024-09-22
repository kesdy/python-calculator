import math

while True:
    print("""
     For addition : 1
     For subtraction : 2
     For multiplication : 3
     For division : 4
     For factorial : 5
          EXIT : 0
     """)

    try:
        choice = int(input("Please choose a number : "))

        if choice == 1:
            try:
                num1 = int(input("Enter a number : "))
                num2 = int(input("Enter the 2nd number : "))
                result = num1 + num2
                print("Result : ", result)
            except ValueError:
                print("ERROR | Please enter a valid number.")

        elif choice == 2:
            try:
                num3 = int(input("Enter a number : "))
                num4 = int(input("Enter the 2nd number : "))
                result2 = num3 - num4
                print("Result : ", result2)
            except ValueError:
                print("ERROR | Please enter a valid number.")

        elif choice == 3:
            try:
                num5 = int(input("Enter a number : "))
                num6 = int(input("Enter the 2nd number : "))
                result3 = num5 * num6
                print("Result : ", result3)
            except ValueError:
                print("ERROR | Please enter a valid number.")

        elif choice == 4:
            try:
                num7 = int(input("Enter a number : "))
                num8 = int(input("Enter the 2nd number : "))

                if num8 == 0:
                    print("ERROR | Division by 0 is not allowed.")
                else:
                    result4 = num7 / num8
                    print("Result : ", result4)
            except ValueError:
                print("ERROR | Please enter a valid number.")

        elif choice == 5:
            try:
                num9 = int(input("Enter a number : "))

                if num9 < 0:
                    print("ERROR | Factorial cannot be negative.")
                else:
                    result5 = math.factorial(num9)
                    print("Result : ", result5)
            except ValueError:
                print("ERROR | Please enter a valid number.")

        elif choice == 0:
            print("Exiting the program...")
            break

        else:
            print("ERROR | Invalid choice. Please enter a valid option.")

    except ValueError:
        print("ERROR | Please select a valid number.")
