from dictionary_of_movies import movies
import random

def pick_a_movie(movie):
  return movie['imdb'] > 5.5

movie = random.choice(movies)

print(pick_a_movie(movie))

