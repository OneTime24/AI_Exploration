

#calculator:





while True:

    a=float(input("Enter First Operand: "))
    ch=str(input("Operation? + - * / % "))
    b=float(input("Enter Second Operand: "))
    match ch:

        case '+':
            print(a+b)
                  
        case '-':
            print(a-b)
            
        case '*':
            print(a*b)
            
        case '/':
            print(a/b)
            
        case '%':
            print(a%b)
            


    x=str(input("Do you want to continue: y/n"))

    if x=='y':
        continue
    else:
        break;

