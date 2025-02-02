from dictionary_of_movies import movies
import random

def average_imdb_score_by_category(movies, category):
  valid_movies = [
  movie['imdb'] for movie in movies 
    
  if 'imdb' in movie 
    and isinstance(movie['imdb'], (int, float)) 
    and 'category' in movie 
    and movie['category'] == category
  ]

  avg_score = sum(valid_movies) / len(valid_movies)
  
  return avg_score


category = random.choice(movies)['category']
avg_score = average_imdb_score_by_category(movies, category)

print(f"Average IMDb score for '{category}' movies: {avg_score:.2f}")