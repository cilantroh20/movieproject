#this file is structure of the class, which you will import this file
#to your instances file

class Movie():
    def __init__(self,movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
