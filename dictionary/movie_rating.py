from datetime import datetime
movies = {}

def add_movie(movies,name):
    if not name:
        return False
    if name in movies:
        return False
    movies[name] = {
    "ratings" : [],
    "time_added" : datetime.now()
    }
    return True


def rate_movie(movies,name, rating):
    if name not in movies:
        return "Movie not found"
    if rating < 1 or rating > 5:
        return "rating must be between 1 and 5"

    movies[name]["ratings"].append(rating)
    return f" Rating added successfully for {name}."
