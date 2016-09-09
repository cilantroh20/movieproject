#this file is structure of the class, which you will import this file
#to your instances file
#it is creating a class that will hold all you movie information
#the self is an instance method, it represents the instance that is calling it
#example: self(the method or convention) is being called by the instance .title
#the init being defined is intializing the data for the class movie
class Movie():
    def __init__(self,movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
