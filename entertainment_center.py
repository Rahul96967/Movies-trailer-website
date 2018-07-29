"""Stores details of movies and displays them on a website."""
import fresh_tomatoes
import media


"""Creates Movie objects, initialising these objects with title, storyline,
    poster image url, video trailer url."""
 
toy_story = media.Movie("Toy Story",
                          "A story of a boy and his toys that comes to life", 
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=Bj4gS1JQzjk") 

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

insideout = media.Movie("Insideout",
                        "feelings of a girl are created as cartoon illusions",
                        "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
                        "https://www.youtube.com/watch?v=BUrLN7Bh94c")


dj = media.Movie("DJ",
                 "Hero acts as a prist to enquire abot the villan deal",
                 "https://upload.wikimedia.org/wikipedia/en/7/72/DJ_film_poster.jpg",
                 "https://www.youtube.com/watch?v=fy-kooz9se4")

avengers = media.Movie("Avengers :Infinity War",
                       "American superhero film based on the Marvel Comics superhero team the Avengers",
                       "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",
                       "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

# Storing the Movie objects in a list.
movies = [toy_story, avatar, insideout, dj, avengers]

# Opens the movie website in the default browser, featuring the movies above.
fresh_tomatoes.open_movies_page(movies)
