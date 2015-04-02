import webbrowser


class Movie():
    """
    Class movie constructor...
    """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, country, director, year):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.country = country
        self.director = director
        self.year = year

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def show_poster(self):
        webbrowser.open(self.poster_image_url)

