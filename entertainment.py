import media
import fresh_tomatoes

slc_punk = media.Movie("SLC punk",
                       "Two anarchist punks deying the system while figuring out their lives",
                       "https://upload.wikimedia.org/wikipedia/en/a/a1/SLC_Punk.jpg",
                       "https://www.youtube.com/watch?v=DILdeHgWF-U")
#print(slc_punk.storyline)
kill_bill = media.Movie("Kill Bill: Volume 1",
                        "A former assasin looking for revenge on her ex-lover, and ex- squad",
                        "http://t1.gstatic.com/images?q=tbn:ANd9GcRZU0dTKm9Za0BhD7BiugB1UvByR615pavx4_0rnJHagCty7AcX",
                        "https://www.youtube.com/watch?v=ot6C1ZKyiME")
#print(kill_bill.storyline)
django_unchained = media.Movie("Django unchained",
                               "A freed slave with a bounty hunter on a journey to save his wife, while killing people along the way.",
                               "http://t3.gstatic.com/images?q=tbn:ANd9GcSnm2FczCxSnt69XUZqqI5-sfy66SvjiV0du9mfUKRRCGqVAurt",
                               "https://www.youtube.com/watch?v=eUdM9vrCbow")
#print(django_unchained.storyline)
#django.show_trailer()

movies = [slc_punk, kill_bill,django_unchained]
fresh_tomatoes.open_movies_page(movies)
