# Udacity [Full-Stack Web Developer Nanodegree](https://www.udacity.com/course/nd004)
##Project 1: Movie Trailer Website with Fresh Tomatoes </h2>
by Angel Vidal
###About
The project has three python files:
* `media.py`: class movie declaration.
* `movies.py`: main program file with the instances to the movie class.
* `fresh_tomatoes.py`: helper python module for html generating.

To run the program type `python movies.py` from the command line and the web 
page 
`fresh_tomatoes.html` will be generated and loaded into the browser.

Once the html file is generated you can load it without run the program.

If you need to add more movies to the library insert them into the movies file 
and run the program again as described before.

The web page shows movies posters tiles with information about:
* movie title
* director
* country
* and year of production

The last three items were added to the `fresh_tomato.py` original file in order
 to be displayed in the web page. 

Background color, movie tiles hover color and 
shape were modified in the css part of `fresh_tomatoes.py`.

When a film tile is clicked it's youtube trailer link will be open and played 
on the page. 
