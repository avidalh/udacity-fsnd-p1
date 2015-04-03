# add support for somespecial characters used in the text strings
# coding=utf-8

import media
import fresh_tomatoes
import operator

# movie class instances with some films
alien = media.Movie(
    "Alien",
    "In deep space, the crew of the commercial starship Nostromo is awakened "
    "from their cryo-sleep capsules halfway through their journey home to "
    "investigate a distress call from an alien vessel. The terror begins when "
    "the crew encounters a nest of eggs inside the alien ship. An organism "
    "from inside an egg leaps out and attaches itself to one of the crew, "
    "causing him to fall into a coma.",
    "http://www.justtopten.com/wp-content/uploads/2014/08/Alien.jpg",
    "https://www.youtube.com/watch?v=bEVY_lonKf4",
    "United States",
    "Ridley Scott",
    "1979")

casablanca = media.Movie(
    "Casablanca",
    "It is early December 1941. American expatriate Rick Blaine is the "
    "proprietor of an upscale nightclub and gambling den in Casablanca. "
    "Rick's Café Américain, attracts a varied clientele: Vichy French, "
    "Italian, and German officials; refugees desperate to reach the still "
    "neutral United States; and those who prey on them. Although Rick "
    "professes to be neutral in all matters, it is later revealed he ran guns "
    "to Ethiopia during its war with Italy and fought on the Loyalist side "
    "against the fascist Nationalists in the Spanish Civil War.",
    "http://www.impawards.com/1942/posters/casablanca.jpg",
    "https://www.youtube.com/watch?v=TLU41jUnWM4",
    "United States",
    "Michael Curtiz",
    "1942")

god_father = media.Movie(
    "The Godfather",
    "Epic tale of a 1940s New York Mafia family and their struggle to protect "
    "their empire from rival families as the leadership switches from the "
    "father (Marlon Brando) to his youngest son (Al Pacino)",
    "http://lunkiandsika.files.wordpress.com/2011/11/the-godfather-original"
    "-poster-1972.png",
    "https://www.youtube.com/watch?v=sY1S34973zA",
    "United States",
    "Francis Ford Coppola",
    "1972")

star_wars = media.Movie(
    "Star Wars",
    "A long time ago in a galaxy far, far away...",
    "http://1.bp.blogspot.com/-WusVAlhA_NM/UPvUR6u1BII/AAAAAAACR7Y"
    "/MlObkYWkZYc/s1600/Star+Wars+Theatrical+Posters "
    "+Around+The+World+in+1977+(12).jpg",
    "https://www.youtube.com/watch?v=i-vsILeJ8_8",
    "United States",
    "George Lucas",
    "1977")

the_sixth_sense = media.Movie(
    "The Sixth Sense",
    "8-year-old Cole Sear (Haley Joel Osment) is haunted by a dark secret: he "
    "is visited by ghosts. Cole is frightened by visitations from those "
    "with unresolved problems who appear from the shadows. He is too afraid "
    "to tell anyone about his anguish, except child psychologist Dr. "
    "Malcolm Crowe (Bruce Willis). As Dr. Crowe tries to uncover the truth "
    "about Coles supernatural abilities, the consequences for client and "
    "therapist are a jolt that awakens them both to something "
    "unexplainable.",
    "http://upload.wikimedia.org/wikipedia/en/6/66/The_sixth_sense.jpg",
    "https://www.youtube.com/watch?v=VG9AGf66tXM",
    "United States",
    "M. Night Shyamalan",
    "1999")

belle_epoque = media.Movie(
    "Belle Époque",
    "The year is 1931. Spain is politically divided between Republicans and "
    "Traditionalists and on the verge of the Spanish Second Republic. "
    "Fernando, a young soldier, deserts his duty.",
    "http://upload.wikimedia.org/wikipedia/en/a/ab/BelleEpoque.jpg",
    "www.youtube.com/watch?v=u_6NLtd_nYw",
    "Spain",
    "Fernando Trueba",
    "1992")

# create the movies list
movies = [casablanca, god_father, alien, belle_epoque, star_wars,
          the_sixth_sense]

# sort by ascending year
movies = sorted(movies, key=operator.attrgetter('year'))

#generate the html page
fresh_tomatoes.open_movies_page(movies)
