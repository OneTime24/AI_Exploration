# Expense Tracker

# Menu:

# 1. Add Expense
# 2. View Expenses
# 3. Search Expense
# 4. Total Expense
# 5. Save Expenses
# 6. Load Expenses
# 7. Exit


expdic=[]

def addexpense():

    try:
        itm=str(input("Enter Item Name: "))
        amt=int(input("Enter Item Amount: "))
        categ=str(input("Enter Item Category: "))

        std={"item":itm,
                "amount":amt,
                "category":categ}

        expdic.append(std)
    except ValueError:
        print("Invalid Input: ")

while True:

    
    try:
        n=int(input("Enter Choice: "))
    except ValueError:
        print("Invalid Choice")
        continue

    if(n==1):
        addexpense()
        continue
    elif(n==2):
        if len(expdic)==0:
            print("No Expenses Yet: ")
            continue

        for itm in expdic:
            print(itm["item"]," ", itm["amount"]," ",itm["category"])
        
        continue
    
    elif(n==3):
        name=str(input("Enter Item Name: " ))
        found=False
        for itm in expdic:
            if(name.lower()==itm["item"].lower()):
                 print("Item: ",itm["item"],"\nAmount: ",itm["amount"],"\nCategory: ",itm["category"])
                 found=True

        if found == False:
            print("item Not Found")
        
       
        continue

    elif(n==4):
        total=0
        for itm in expdic:
            total+=itm["amount"]
        print("Total Expense:", total)
    

    elif(n==5):
        #to save file
        try:
            with open("data.txt","w") as file:
                for itm in expdic:
                    line=itm["item"]+","+str(itm["amount"])+","+itm["category"]+"\n"

                    file.write(line)
                    continue
        except Exception:
            print("Error Saving File: ")
            continue

    elif(n==6):
        try:

            with open("data.txt","r") as file:

                expdic.clear()
                
                for line in file:

                    data=line.strip().split(",")

                    det={
                        "item":data[0],
                        "amount":int(data[1]),
                        "category":data[2]
                    }

                    expdic.append(det)

                print("data loaded succesfully:" )

        except FileNotFoundError:
            print("File Not Found: ")


    elif(n==7):
        print("Exiting the program: ")
        break