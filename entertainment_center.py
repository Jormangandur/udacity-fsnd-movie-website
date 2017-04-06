import fresh_tomatoes
import media

# Create Movie instances
two_towers = media.Movie("The Lord of the Rings: The Two Towers",
                         "While Frodo and Sam edge closer to Mordor with the "
                         "help of the shifty Gollum, the divided fellowship "
                         "makes a stand against Sauron's new ally, Saruman, "
                         "and his hordes of Isengard.",
                         "http://www.gstatic.com/tv/thumb/movieposters/30793/p30793_p_v8_am.jpg",
                         "https://www.youtube.com/watch?v=LbfMDwc4azU",
                         "12")

oldboy = media.Movie("Oldboy",
                     "After being kidnapped and imprisoned for fifteen years, "
                     "Oh Dae-Su is released, only to find that he must find "
                     "his captor in five days.",
                     "http://www.gstatic.com/tv/thumb/movieposters/35948/p35948_p_v8_aa.jpg",
                     "https://www.youtube.com/watch?v=D89OHw0VsYM",
                     "18")

rogue_one = media.Movie("Rogue One",
                        "The Rebel Alliance makes a risky move to steal the"
                        "plans for the Death Star, setting up the epic saga"
                        "to follow.",
                        "http://a.dilcdn.com/bl/wp-content/uploads/sites/6/2016/10/rogueone_onesheetA.jpg",
                        "https://www.youtube.com/watch?v=frdj1zb9sMY",
                        "12A")

return_of_the_king = media.Movie("The Lord of the Rings: The Return of the King",
                                 "Gandalf and Aragorn lead the World of Men "
                                 "against Sauron's army to draw his gaze from "
                                 "Frodo and Sam as they approach Mount Doom "
                                 "with the One Ring.",
                                 "http://www.impawards.com/2003/posters/lord_of_the_rings_the_return_of_the_king.jpg",
                                 "https://www.youtube.com/watch?v=r5X-hFf6Bwo",
                                 "12")

tropic_thunder = media.Movie("Tropic Thunder",
                             "Through a series of freak occurrences, a group of"
                             "actors shooting a big-budget war movie are forced"
                             " to become the soldiers they are portraying.",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BNDE5NjQzMDkzOF5BMl5BanBnXkFtZTcwODI3ODI3MQ@@._V1_UY1200_CR112,0,630,1200_AL_.jpg",
                             "https://www.youtube.com/watch?v=T-6YhRZowgc",
                             "15")

deadpool = media.Movie("Deadpool",
                       "A fast-talking mercenary with a morbid sense of humor "
                       "is subjected to a rogue experiment that leaves him"
                       "with accelerated healing powers and a quest for revenge.",
                       "http://www.impawards.com/2016/posters/deadpool_ver9_xxlg.jpg",
                       "https://www.youtube.com/watch?v=FyKWUTwSYAs",
                       "15")

# Create movies array for instance use in fresh_tomatoes.py
movies = [two_towers, oldboy, rogue_one,
          return_of_the_king, tropic_thunder, deadpool]

# Pass movies to fresh_tomatoes.py and call generate webpage method
fresh_tomatoes.open_movies_page(movies)
