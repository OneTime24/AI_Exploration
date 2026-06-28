


import json

games=[]




def addgame():
    gm=input("Enter Game Name: ")
    price=float(input("Enter Game price: "))
    year=int(input("Enter Release Year"))

    games.append({"name":gm,
           "price":price,
           "year":year}
    )


def viewgames():
    if not games:
        print("no games found")
        return 
    for game in games:
        print(f"Game: {game['name']} | Price: {game['price']} | Year: {game['year']}")

#might noy work lol
def tojson():

    with open("rev_json.json","w") as file:

        json.dump(games,file)



while True:
    print("\nOPTIONS")
    print("1. Add Game")
    print("2. View Games")
    print("3. Save Games")
    print("4. Exit")

    ch = int(input("Enter option: "))

    if ch == 1:
        addgame()

    elif ch == 2:
        viewgames()

    elif ch == 3:
        tojson()

    elif ch == 4:
        print("Exiting...")
        break

    else:
        print("Invalid option.")