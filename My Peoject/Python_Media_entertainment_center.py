import fresh_tomatoes
import Python_Media

braveheart = Python_Media.Movie("Braveheart", "a 13th-century Scottish warrior who led the Scots in the First War of Scottish Independence against King Edward I of England.", "http://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg", "https://www.youtube.com/watch?v=j53_WxqPZ7c")
#print (toy_story.storyline)
the_bible = Python_Media.Movie("The Bible", "The Bible is a television miniseries based on the Bible.", "http://upload.wikimedia.org/wikipedia/commons/9/99/The_Bible_-_Title_Card.jpg", "https://www.youtube.com/watch?v=1hThfoBzWxw")
#print (avatar.storyline)
#avatar.show_trailer()
the_passion = Python_Media.Movie("The Passion of the Christ", "The film covers primarily the final 12 hours of Jesus' life", "http://upload.wikimedia.org/wikipedia/en/6/61/Thepassionposterface-1-.jpg", "https://www.youtube.com/watch?v=MhdDIz3y9zo")
#the_passion.show_trailer()
movies = [braveheart, the_bible, the_passion]
#fresh_tomatoes.open_movies_page(movies)
#print (Python_Media.Movie.VALID_RATINGS)
print (Python_Media.Movie.__doc__)
print (Python_Media.Movie.__name__)
print (Python_Media.Movie.__module__)
