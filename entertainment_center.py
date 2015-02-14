import fresh_tomatoes
import movie

# the next few lines are the movies entered in. i added an extra variable which was favorite quotes.
#the quotes along with a few other tidbits were eventually going to be added to a popup
#on the screen like a netflix but i needed to moveon
#todo: add a popup and put on nifty tidbits about the movie

back_to_the_future = movie.Movie("Back to the Future",
                                 "A young man is accidentally sent 30 years into the past in a time-traveling DeLorean invented by his friend, Dr. Emmett Brown, and must make sure his high-school-age parents unite in order to save his own existence.",
                                 "http://upload.wikimedia.org/wikipedia/en/thumb/d/d2/Back_to_the_Future.jpg/220px-Back_to_the_Future.jpg",
                                 "https://www.youtube.com/watch?feature=player_detailpage&v=qvsgGtivCgs",
                                 "Marty McFly: Wait a minute. Wait a minute, Doc. Ah... Are you telling me that you built a time machine... out of a DeLorean?Dr. Emmett Brown: The way I see it, if you're gonna build a time machine into a car, why not do it with some *style?* "
                                 )
                                    
monty_python = movie.Movie("The Holy Grail",
                                 "King Arthur and his knights embark on a low-budget search for the Grail, encountering many very silly obstacles.",
                                 "http://upload.wikimedia.org/wikipedia/en/thumb/4/49/Monty_python_and_the_holy_grail_2001_release_movie_poster.jpg/220px-Monty_python_and_the_holy_grail_2001_release_movie_poster.jpg",
                                 "https://www.youtube.com/watch?feature=player_detailpage&v=urRkGvhXc8w",
                                 " King Arthur: The Lady of the Lake, her arm clad in the purest shimmering samite held aloft Excalibur from the bosom of the water, signifying by divine providence that I, Arthur, was to carry Excalibur. THAT is why I am your king. Dennis: [interrupting] Listen, strange women lyin' in ponds distributin' swords is no basis for a system of government. Supreme executive power derives from a mandate from the masses, not from some farcical aquatic ceremony."
                                )

wedding_crashers = movie.Movie("Wedding Crashers",
                                 "John Beckwith and Jeremy Grey, a pair of committed womanizers who sneak into weddings to take advantage of the romantic tinge in the air, find themselves at odds with one another when John meets and falls for Claire Cleary.",
                                 "http://upload.wikimedia.org/wikipedia/en/thumb/3/3e/Wedding_crashers_poster.jpg/215px-Wedding_crashers_poster.jpg",
                                 "https://www.youtube.com/watch?v=FF-XbOJlbeU&feature=player_detailpage#t=5",
                                 "Gloria Cleary: Don't ever leave me!  Jeremy Grey: Never.  Gloria Cleary: Good.[girlish voice]  Gloria Cleary: 'Cause I'd find you!"
                               )

army_of_darkness = movie.Movie("Army of Darkness",
                                 "A man is accidentally transported to 1300 A.D., where he must battle an army of the dead and retrieve the Necronomicon so he can return home.",
                                 "http://upload.wikimedia.org/wikipedia/en/4/46/Army_of_Darkness_poster.jpg",
                                 "https://www.youtube.com/watch?feature=player_detailpage&v=CZ-wU5RXw2o#t=10",
                                 "Ash: First you wanna kill me, now you wanna kiss me. Blow."
                               )

the_matrix = movie.Movie("The Matrix",
                                 "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                                 "http://upload.wikimedia.org/wikipedia/en/thumb/c/c1/The_Matrix_Poster.jpg/220px-The_Matrix_Poster.jpg",
                                 "https://www.youtube.com/watch?feature=player_detailpage&v=m8e-FF8MsqU",
                                 "Neo: What are you trying to tell me? That I can dodge bullets?  Morpheus: No, Neo. I'm trying to tell you that when you're ready, you won't have to."
                              )

christmas_vacation = movie.Movie("Christmas Vacation",
                                 "The Griswold family's plans for a big family Christmas predictably turn into a big disaster.",
                                 "http://upload.wikimedia.org/wikipedia/en/thumb/5/53/NationalLampoonsChristmasVacationPoster.JPG/220px-NationalLampoonsChristmasVacationPoster.JPG",
                                 "https://www.youtube.com/watch?feature=player_detailpage&v=NBTTipJX-h4",
                                 "Eddie: Don't go puttin' none of that stuff on my sled, Clark. You know that metal plate in my head? I had to have it replaced, cause every time Catherine revved up the microwave I'd piss my pants and forget who I was for a half hour or so. So over at the VA they had to replace it with plastic. It ain't as strong so I don't know if I should go sailin down no hill with nothing between the ground and my brains but a piece of government plastic.  Clark: You really think it matters, Eddie?"
                               )


#this line adds the movies into an array called movies
movies = [back_to_the_future, monty_python, wedding_crashers, army_of_darkness, the_matrix, christmas_vacation]

#this line of code calls up the website when the run is used (in java this is called the MAIN
fresh_tomatoes.open_movies_page(movies)
