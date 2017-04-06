import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

rogue_one = media.Movie("Rogue One",
                    "The Rebel Alliance makes a risky move to steal the plans for the Death Star, setting up the epic saga to follow.",
                    "http://a.dilcdn.com/bl/wp-content/uploads/sites/6/2016/10/rogueone_onesheetA.jpg",
                    "https://www.youtube.com/watch?v=frdj1zb9sMY")

return_of_the_king = media.Movie("The Lord of the Rings: The Return of the King",
                    "The Rebel Alliance makes a risky move to steal the plans for the Death Star, setting up the epic saga to follow.",
                    "http://www.impawards.com/2003/posters/lord_of_the_rings_the_return_of_the_king.jpg",
                    "https://www.youtube.com/watch?v=r5X-hFf6Bwo")

tropic_thunder = media.Movie("Tropic Thunder",
                    "Through a series of freak occurrences, a group of actors shooting a big-budget war movie are forced to become the soldiers they are portraying.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BNDE5NjQzMDkzOF5BMl5BanBnXkFtZTcwODI3ODI3MQ@@._V1_UY1200_CR112,0,630,1200_AL_.jpg",
                    "https://www.youtube.com/watch?v=T-6YhRZowgc")

deadpool = media.Movie("Deadpool",
                    "A fast-talking mercenary with a morbid sense of humor is subjected to a rogue experiment that leaves him with accelerated healing powers and a quest for revenge.",
                    "http://www.impawards.com/2016/posters/deadpool_ver9_xxlg.jpg",
                    "https://www.youtube.com/watch?v=FyKWUTwSYAs")

movies = [toy_story, avatar, rogue_one, return_of_the_king, tropic_thunder, deadpool]
#fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
