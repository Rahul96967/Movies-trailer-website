"""Stores details of movies and displays them on a website."""
import fresh_tomatoes
import media


"""Creates Movie objects, initialising these objects with title, storyline,
    poster image url, video trailer url."""

toy_story = media.Movie("Toy Story", 
                        "A story of a boy and his toys that comes to life",
                        "https://bit.ly/2wkpqR5",
                        "https://www.youtube.com/watch?v=Bj4gS1JQzjk") 

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://bit.ly/2fWJXSq",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

insideout = media.Movie("Insideout",
                        "feelings of a girl are created as cartoon illusions",
                        "https://bit.ly/2JWIFqN",
                        "https://www.youtube.com/watch?v=BUrLN7Bh94c")

dj = media.Movie("DJ",
                 "Hero acts as a prist to enquire abot the villan deal",
                 "https://bit.ly/2LzR2u9",
                 "https://www.youtube.com/watch?v=fy-kooz9se4")

avengers = media.Movie("Avengers :Infinity War",
                       "Superhero film based on Marvel Comics The Avengers",
                       "https://bit.ly/2KjSEUq",
                       "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

# Storing the Movie objects in a list.
movies = [toy_story, avatar, insideout, dj, avengers]

# Opens the movie website in the default browser, featuring the movies above.
fresh_tomatoes.open_movies_page(movies)
