import webbrowser


class Movie():
    """This class provides storage for key movie information"""

    VALID_RATINGS = ["U", "PG", "12", "12A", "15", "18", "R18"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        if rating in self.VALID_RATINGS:
            self.rating = rating
        else:
            raise ValueError("Rating not valid for {movie_title}")

    def show_trailer(self):  # Class method for showing movie trailer
        webbrowser.open(self.trailer_youtube_url)
