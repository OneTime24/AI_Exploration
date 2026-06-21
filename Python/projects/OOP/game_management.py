# 🎮 Game Collection Manager
# Each game has:
# title
# genre
# price
# Menu:
# 1 Add Game
# 2 View Games
# 3 Search Game
# 4 Save
# 5 Load
# 6 Exit
# Use:
# Game class
# GameCollection class


import json

class Game:
    def __init__(self,title,genre,price):

        self.title=title
        self.genre=genre
        self.price=price

    
    
    def display(self):
        print(f"{self.title} : {self.genre} : {self.price}")

    
    def todict(self):

        return {
            "title":self.title,
            "genre":self.genre,
            "price":self.price
        }
    

class manage:

    def __init__(self):
        self.games=[]

    
    #1. add games

    def addgame(self):

        name=input("Enter Game Name: ")

        gen=input("Enter Genre of the Game: ")

        pr=float(input("Enter PRice of the game: "))

        gm=Game(name,gen,pr)

        self.games.append(gm)

    
    #2. View Games:

    def viewgame(self):

        
        if not self.games:
            print("No Games Found: ")

            return
        
        for gm in self.games:

            gm.display()

        
        #3. search

    def searchgame(self):

        target=input("Enter Game TItle: ")

        found=False

        for gm in self.games:

            if gm.title.lower()==target.lower():

                gm.display()

                found=True

        
        if not found:

            print("Game Not found: ")





    #4. Save to json
    
    def saveto(self):

        data=[]

        for gm in self.games:
            data.append(gm.todict())

        with open("games.json","w") as file:

            json.dump(data,file)
        
        print("Data saved to Json")


    #5. Load from json:

    
    def loadto(self):

        try:
            with open("games.json","r") as file:
                data=json.load(file)

            
            self.games.clear()


            for itm in data:
                gm=Game(itm["title"],itm["genre"],itm["price"])

            
            self.games.append(gm)


            print("Loaded from json")


        except FileNotFoundError:
            print("File Not FOund;")




g_manage=manage()


while True:

    print("""
1. Add Games
2. View Gamess
3. Search Games
4. Save
5. Load
6. Exit
""")
    

    ch=int(input("Select Option: "))


    if ch==1:
        g_manage.addgame()

    elif ch==2:
        g_manage.viewgame()

    elif ch==3:
        g_manage.searchgame()
    elif ch==4:
        g_manage.saveto()

    elif ch==5:
        g_manage.loadto()

    elif ch==6:
        
        print("Exiting the program: ")
        break
    else:
        print("Enter a valid option: ")