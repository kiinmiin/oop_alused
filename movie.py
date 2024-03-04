"""Movie."""


class Movie:
    """Movie object, do not change."""

    def __init__(self, name: str, year: int, genres: list):
        """Movie constructor."""
        self.name = name
        self.year = year
        self.genres = genres


def create_movie(name_with_year: str, genre1: str, genre2: str):
    """
    Create a new movie from name and 2 genres.

    Name is in format "name some thing (2019)".
    Year is inside parenthesis and always 4 digits.
    Everything before parenthesis is a name.
    Return None, if:
    - year is below 1900 and above 2020 ("blah (1200)", "blah (3000)")
    - name is empty ("(1933)")
    Otherwise create a new movie and return it.

    Year has to be int.
    Remove trailing space from name.
    "film (1999)" => should give "film" 1999
    """
    #for year in name_with_year:
        #if int(year) > 2020 or int(year) < 1900:
            #return None
        #if name not in name_with_year:
            #return None
        #else:
            #new_movie = Movie(name, int(year), genres)
            #print(new_movie)
    name, year = name_with_year.split("(")
    year = year.strip(")")
    
    if not name or not year.isdigit() or int(year) < 1900 or int(year) > 2020:
        return None

    return Movie(name.strip(), int(year), [genre1, genre2])
    pass


def get_ordered_movies(movies: list) -> list:
    """
    Return sorted movies by year (desc, newer first) and count of genres (asc).

    If both year and count of genres are the same, keep the original order.
    """
    sorted_movies = sorted(movies, key=lambda movie: (-movie.year, len(movie.genres)))
    return sorted_movies
    pass


def add_genres(movies: list, genres: list) -> None:
    """
    Modify the movies in the list by adding genres.

    A genre is added if it does not already exist.
    """
    for movie in movies:
        for genre in genres:
            if genre not in movie.genres:
                movie.genres.append(genre)
    return None
    
    pass


def remove_movies_by_genre(movies: list, genre: str) -> list:
    """
    Return a new list where all the movies with the given genre are removed.

    The order of movies should remain the same.
    The original movies list should remain unchanged.
    """
    certain_movies = []
    for movie in movies:
        if genre in movie.genres:
            movie.genres.remove(genre)
            certain_movies.append(movie)
    return certain_movies
    pass


if __name__ == "__main__":
    m1 = Movie("t1", 1991, ["thriller", "action"])
    print(m1)
    m2 = create_movie("t2 (1992)", "drama", "action")
    print(m2)
    movies1 = [m1, m2]
    print(movies1)
    print(remove_movies_by_genre(movies1, "action"))