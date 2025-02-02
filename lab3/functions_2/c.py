from dictionary_of_movies import movies
import random

def filter_movies():
  categories = list((movie["category"] for movie in movies if "category" in movie))
  category = random.choice(categories)

  filtered_movies = [movie for movie in movies if movie.get("category") == category]

  return category, filtered_movies

selected_category, some_category_movies = filter_movies()

print(f"Movies under category: {selected_category}")
for movie in some_category_movies:
  print(movie['name'])

