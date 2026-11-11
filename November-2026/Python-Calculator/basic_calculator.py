while True:
    print("=========PYTHON CALCULATOR=========")


    try:
        num1_input = input("Enter First Number or q to Quit : ")

        if num1_input.lower() == "q":
            print("Goodbye! Thanks for using Python Calculator😊")
            break
        
        num1 = float(num1_input)
        
    except ValueError:
        print("Please enter a valid number.")
        continue
        
    
    operator = input("(Select an operator : +,-,*,/,//,%,**) : ")

        
    try:
        num2_input = input("Enter Second Number or q to Quit : ")

        if num2_input.lower() == "q":
            print("Goodbye! Thanks for using Python Calculator😊")
            break

        num2 = float(num2_input)
        

    except ValueError:
        print("Please enter a valid number.")
        continue


    if operator == "+":
        print("Result : ", num1+num2)


    elif operator == "-":
        print("Result : ", num1-num2)


    elif operator == "*":
        print("Result : ", num1*num2)


    elif operator == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            print("Result : ", num1/num2)


    elif operator == "//":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            print("Result : ", num1//num2)


    elif operator == "%":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            print("Result : ", num1%num2)


    elif operator == "**":
        print("Result : ", num1**num2)

        
    else:
        print("Invalid Syntax.")


        
