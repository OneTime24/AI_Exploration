


while True:

    

    try:
        n=int(input("Enter a number: "))
        result=10/n
        print(result)
        break
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
