class Movie:

    total_movies = 0          # Class Variable

    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating
        self.watched = False

        Movie.total_movies += 1

    def watch(self):
        self.watched = True

    def display(self):
        print(f"{self.title} | {self.genre} | {self.rating}")

    def __str__(self):
        status = "Watched" if self.watched else "Not Watched"
        return f"{self.title} ({self.genre}) - {status}"

    @classmethod
    def show_total_movies(cls):
        print("Total Movies:", cls.total_movies)

    @staticmethod
    def cinema_rules():
        print("No recording allowed inside the cinema.")

    
class PremiumMovie(Movie):

    def __init__(self, title, genre, rating, subscription):
        super().__init__(title, genre, rating)
        self.subscription = subscription

    def display(self):
        print(
            f"{self.title} | {self.genre} | {self.rating} | Subscription: {self.subscription}"
        )


class Cinema:

    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def view_movies(self):

        if not self.movies:
            print("No Movies Found")
            return

        for movie in self.movies:
            print(movie)

    def search_movie(self, title):

        for movie in self.movies:

            if movie.title.lower() == title.lower():
                print(movie)
                return

        print("Movie not found")

    def remove_movie(self, title):

        for movie in self.movies:

            if movie.title.lower() == title.lower():

                self.movies.remove(movie)

                Movie.total_movies -= 1

                print("Movie Removed")

                return

        print("Movie not found")
cinema = Cinema()

m1 = Movie("Inception", "Sci-Fi", 9.2)
m2 = Movie("Interstellar", "Sci-Fi", 9.5)
m3 = PremiumMovie("Avengers Endgame", "Action", 9.0, "Yes")

cinema.add_movie(m1)
cinema.add_movie(m2)
cinema.add_movie(m3)

cinema.view_movies()

Movie.show_total_movies()

Movie.cinema_rules()

m1.watch()

print(m1)

cinema.search_movie("Inception")

cinema.remove_movie("Interstellar")

cinema.view_movies()
