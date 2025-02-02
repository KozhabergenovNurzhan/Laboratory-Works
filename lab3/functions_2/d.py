from dictionary_of_movies import movies

def average_imdb_score(movies):
  valid_movies = [(movie['name'], movie['imdb']) for movie in movies if 'imdb' in movie and isinstance(movie['imdb'], (int, float))]

  avg_score = sum(score for _, score in valid_movies) / len(valid_movies)
  movie_names = [title for title, _ in valid_movies]

  return avg_score, movie_names

avg_score, movie_names = average_imdb_score(movies)

print("Average IMDB score of:")
for name in movie_names:
  print(f"- {name}")
print(f"{avg_score:.2f}")  

