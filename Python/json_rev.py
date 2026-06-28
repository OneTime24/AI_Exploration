


import json

games=[]




def addgame():
    gm=input("Enter Game Name: ")
    price=float(input("Enter Game price: "))
    year=int(input("Enter Release Year"))

    games={"name":gm,
           "price":price,
           "year":year}
    

def tojson():

    with open("rev_json.json","w") as file:

        json.dump(games,file)


print("OPTIONS:\n1. addGame:\n2. SaveGames")

ch=int(input("Enter option: "))




