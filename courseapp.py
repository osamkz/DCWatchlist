import flask
import datetime

app = flask.Flask("courseapp")

#Defining the get page, get list, and the class init of the movies

def get_html(page_name):
    html_file = open(page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

def get_list():
    list_file = open("listmovies.txt")
    content = list_file.read()
    list_file.close()
    movie_list = content.split(";")
    return movie_list 


#Defining the class Moviz for the movie details

class Moviz:
    def __init__(self, title, release, summary):
        self.title = title
        self.release = release
        self.summary = summary

    
    #Method to retrieve and adapt the form of the txt file with the movies informations
    def populate_moviz(file_path):
            movies = []
            file = open(file_path, "r")
            content = file.read().strip().split("\n")
            file.close()
            #print(content)
            for element in content:
                lines = element.split(";")
                title = lines[0].split(': ')[1]
                release = lines[1].split(': ')[1]
                summary = lines[2].split(': ')[1]
                movies.append(Moviz(title, release, summary))
            return movies
    #Method to return the identified elements of each movie information 
    #Use of f string to preserve html format. This is not my code 
    # source :https://docs.python.org/3/reference/lexical_analysis.html#f-strings
    def movie_info(self):
        a = f"<p> Title: {self.title} </p>"
        b = f"<p> Release: {self.release} </p>"
        c = f"<p> Summary: {self.summary} </p>"
        return str(a + b + c)
    



#Defining the routes

@app.route("/")
def home():
    return get_html("index")


@app.route("/allmovies")
def get_movies():
    movie_page = get_html("allmovies")
    movies_list = get_list()
    value = ""
    for movie in movies_list:
        movie = movie.strip()
        movie_param = movie.replace(" ","_")
        value = value + "<p>" + "<a class="+"menulink"+" href="+"/onemovie/"+movie_param+"> " + movie +  "</a> </p>"
    return movie_page.replace("&&LIST&&",value)


    
# Adding a  route with optional URL parameter in order to get into each movie as a subpage
# Source: https://sentry.io/answers/create-a-route-with-optional-url-parameters-in-flask/

@app.route("/onemovie", defaults = {"movie_name": None })
@app.route("/onemovie/<movie_name>")
def get_onemovie(movie_name):
    onemovie_page = get_html("onemovie")
    movie_info = Moviz.populate_moviz("moviesdetails.txt")
    #Using the print(movie_info) to check the format of the movie info
    #Using the movie_found for the loop.
    movie_found = False
    #Replace the _ in order to compare with the movie title in the movie_info
    movie_param = movie_name.replace("_"," ")
    

#use the class movie to complete each page
    for movie in movie_info:
        print(movie)
        if movie.title == movie_param:
            movie_found = True
            return onemovie_page.replace("&&DETAIL&&",Moviz.movie_info(movie))
    if not movie_found:
        return onemovie_page.replace("&&DETAIL&&","404 No Page found")