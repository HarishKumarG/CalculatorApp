print("Welcome to Calculator!")
def calculator():
    while True:
        #welcome message
        print("Select the operation you want to perform.")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        #input for operator
        operator = input("Enter your choice(1/2/3/4/5): ")

        operator_list = ['1','2','3','4','5']
        if operator in operator_list:
            #exit condition
            if operator == '5':
                print("Thank you for using calculator!")
                break
            #getting nums from user
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            #operation
            if operator == '1':
                print(f"The addition of {int(num1)} and {int(num2)} is:", int(num1 + num2))
            elif operator == '2':
                print(f"The Difference of {int(num1)} and {int(num2)} is:", int(num1 - num2))
            elif operator == '3':
                print(f"The Multiplication of {int(num1)} and {int(num2)} is:", int(num1 * num2))
            elif operator == '4':
                if num2 != 0:
                    print(f"The Division of {int(num1)} by {int(num2)} is:", int(num1 / num2))
                else:
                    print("ZeroDivisionError: Division by zero is not allowed")
        else:
            print("Invalid operator")

        print()
        print("---------------------------------------------------")
        print()

#calling function
calculator()

