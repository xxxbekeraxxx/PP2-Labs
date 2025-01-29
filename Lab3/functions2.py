# Dictionary of movies
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

# Function to filter movies by category
def filter_by_category(movies, category):
    """Filters the movies by their category."""
    return [movie for movie in movies if movie["category"] == category]

# Function to calculate the average IMDB score for a list of movies
def average_imdb_score(movies):
    """Calculates the average IMDB score for the given movies."""
    if not movies:
        return 0.0
    total_score = sum(movie["imdb"] for movie in movies)
    return total_score / len(movies)

# Function to calculate the average IMDB score for movies in a specific category
def average_imdb_score_by_category(movies, category):
    """Calculates the average IMDB score for movies in a given category."""
    category_movies = filter_by_category(movies, category)
    return average_imdb_score(category_movies)

# Calculate average IMDB score for 'Romance' category
avg_score_category = average_imdb_score_by_category(movies, "Romance")
print("Average IMDB score for Romance category:", avg_score_category)
