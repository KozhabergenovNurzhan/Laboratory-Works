from dictionary_of_movies import movies

def filter_movies(movies):
  return [movie for movie in movies if movie['imdb'] > 5.5]

filtered_movies = filter_movies(movies) 

for movie in filtered_movies:
  print(movie['name'])