MOVIE_LIBRARY = []


class BasePlayable:

    def __init__(self, title: str, release_year: int, genre: str):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.watch_count = 0

    def play(self):
        self.watch_count += 1
        print(str(self))
        


class Movie(BasePlayable):

    def __str__(self):
        return f"{self.title} ({self.release_year})"


class Series(BasePlayable):
    def __init__(
            self, title: str, release_year: int,
            genre: str, season_number: int, series_number: int
    ):
        super(Series, self).__init__(title, release_year, genre)
        self.season_number = season_number
        self.series_number = series_number

    @property
    def season_number_two_digits(self) -> str:
        return str(self.season_number) if self.season_number > 9 else f"0{self.season_number}"

    @property
    def series_number_two_digits(self) -> str:
        return str(self.series_number) if self.series_number > 9 else f"0{self.series_number}"

    def __str__(self):
        return f"{self.title} S{self.season_number_two_digits}E{self.series_number_two_digits}"


class Add_Movie(BasePlayable):
    def __init__(
            self, title: str, release_year: int,
            genre: str, season_number: int, series_number: int
    ):
      movie = Movie(title, release_year, genre)
      MOVIE_LIBRARY.append(movie)


    def add_serial(title: str, release_year: int, genre: str, season_number: int, series_number: int):
       serial = Series(title, release_year, genre, season_number, series_number)
       MOVIE_LIBRARY.append(serial)


    def get_movies():
        return list(
        sorted(
            filter(
                lambda item: isinstance(item, Movie), MOVIE_LIBRARY
            ),
            key=lambda item: item.title
        )
    )

    def get_series():
         return list(
        sorted(
            filter(
                lambda item: isinstance(item, Series), MOVIE_LIBRARY
            ),
            key=lambda item: item.title
        )
    )

    def search(query):
        return list(filter(lambda item: item.title == query, MOVIE_LIBRARY))


    def general_views() :
        for _ in range(MOVIE_LIBRARY) :
            return f"{ play(self) for _ in (0 , 100)}"


    def ten() :
         return f"{(general_views)*10}"


    def top_titles() :
        return F"(self.title: int) if self.watch_count == max"


