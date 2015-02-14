import webbrowser


#the single class for this project to allow movies to be created
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image_url, trailer_youtube_url, quote):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.quote = quote

        
#the single method inside this single class to run the trailers when activated
    def show_trailer(self):
        webbrowser.open(self.trailer)
