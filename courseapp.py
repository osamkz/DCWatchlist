import flask
import datetime

app = flask.Flask("courseapp")

#Defining the get page

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
        value = value + "<p>" + "<a class="+"menulink"+" href="+"/onemovie/"+movie+"> " + movie +  "</a> </p>"
    return movie_page.replace("&&LIST&&",value)


    
# Adding a  route with optional URL parameter in order to get into each movie as a subpage
# Source: https://sentry.io/answers/create-a-route-with-optional-url-parameters-in-flask/

@app.route("/onemovie", defaults = {"movie_name": None })
@app.route("/onemovie/<movie_name>")
def get_onemovie(movie_name):
    onemovie_page = get_html("onemovie")
    if movie_name:
        return onemovie_page.replace("&&DETAIL&&",movie_name)
