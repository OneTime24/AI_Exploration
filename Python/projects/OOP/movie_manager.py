# 🎬 Project: Movie Collection Manager

# Imagine you're making a personal movie tracker.

# Features:

# Add movies
# View all movies
# Search movies
# Save to file
# Load from file



import json

class Movie:

    def __init__(self,name,year,rating):
        self.title=name
        self.year=year
        self.rating=rating
    

    def display(self):
        
        print(f"{self.title} ({self.year}) ({self.rating})")

    
    def todict(self):
        return {
            "title":self.title,
            "year":self.year,
            "rating":self.rating
        }
    

class movie_manage:

    def __init__(self):
        self.movies=[]

    
    #1. add

    def addmov(self):
        title=input("Enter Title: ")
        year=int(input("Enter Movie Year: "))
        rating=float(input("Enter Rating: "))

        movie=Movie(title,year,rating)

        self.movies.append(movie)

        print("Movie Added: ")


    #2. view all movies:


    def viewmov(self):

        if not self.movies:
            print("No Movies found: ")

            return
        
        for mov in self.movies:

            mov.display()

    
    def searchmov(self):

        target=input("Enter Title: ")

        found=False

        for mov in self.movies:

            if mov.title.lower() == target.lower():

                mov.display()

                found=True

    
        if not found:

            print("Movie Not found: ")


    #3. save to json

    def saveto(self):

        data=[]


        for mov in self.movies:
            data.append(mov.todict())

        
        with open("movies.json","w") as file:
            json.dump(data,file)

        
        print("Saved to JSON")



    #4. load to json

    def load(self):

        try:
            with open("movies.json","r") as file:
                data=json.load(file)
            
            self.movies.clear()


            for itm in data:
                movie=Movie(itm["title"]
                            ,itm["year"]
                            ,itm["rating"])
                
                self.movies.append(movie)

            print("loaded json")

        except FileNotFoundError:
            print("Failed to load from the json file: ")

    





manage=movie_manage()

while True:

    print("""
1. Add Movie
2. View Movies
3. Search Movie
4. Save
5. Load
6. Exit
""")
    

    ch=int(input("ENter Option Number: "))


    if ch==1:

        manage.addmov()


    elif ch==2:
        manage.viewmov()

    elif ch==3:
        manage.searchmov()

    elif ch==4:
        manage.saveto()

    elif ch==5:
        manage.load()

    elif ch==6:
        print("Exiting the program:")
        break








