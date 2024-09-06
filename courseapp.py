import flask
import datetime
from flask import request
from datetime import date
from datetime import datetime


app = flask.Flask("courseapp")

#Defining the get page, get list, and the class init of the movies

def get_html(page_name):
    html_file = open(page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

def get_html_sub(page_name, movie_noun = None):
    html_file = open(page_name + ".html")
    content = html_file.read()
    if movie_noun:
        content = content.replace('{{ movie_name }}', movie_noun)
    html_file.close()
    return content

def get_list():
    list_file = open("listmovies.txt")
    content = list_file.read()
    list_file.close()
    movie_list = content.split(";")
    movie_list = [movie.replace("\n","") for movie in movie_list]
    return movie_list 

#functions to add comment in the txt file
def save_movie(movie_name, movie_info):
    file_path = "movie_cmt/"+movie_name
    file = open(file_path, "a")
    file.write("<ul><li> <i>Written on</i> " + str(datetime.today().strftime("%d-%m-%Y")) + ":<br> " + movie_info+" \n <br></li></ul>")
    file.close


def get_comment(movie_name):
    file_path = "movie_cmt/"+movie_name
    file = open (file_path, "r+")
    content = file.read().strip()
    file.close()
    return content



#Defining the class Moviz for the movie details

class Moviz:
    def __init__(self, title, release, summary, comment):
        self.title = title
        self.release = release
        self.summary = summary
        self.comment = comment
    

    #Properties to measure the content of the Object and the timeline of the movie (Nolan or Snyder).
    def movie_len(self):
        return len(self.title)+len(self.release)+len(self.summary)+len(self.comment)

    def movie_Timeline(self):
        movie_year = int(self.release)
        timeline = ""
        if movie_year < 2015:
            timeline = "Nolan Universe"
        else:
            timeline = "Snyder Universe"
        return timeline

    

    
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
                comment = lines[3].split(":")[1]
                movies.append(Moviz(title, release, summary, comment))
            return movies
    #Method to return the identified elements of each movie information 
    #Use of f string to preserve html format. This is not my code 
    # source :https://docs.python.org/3/reference/lexical_analysis.html#f-strings
    #Use of the span so that the Movie element can stay next to the information with no break of line 
    def movie_info(self):
        a = f"<p> <span class = 'listStyle'> Title:</span> <span>{self.title} </span></p>"
        b = f"<p> <span class = 'listStyle'> Release:</span> <span>{self.release} </span> <span>({Moviz.movie_Timeline(self)}) </span></p>"
        c = f"<p> <span class = 'listStyle'> Summary:</span> <span>{self.summary} </span></p>"
        d = f"<p> <span class = 'listStyle'> Comments:</span> <span>{self.comment} </span></p>"
        return str(a + b + c + d)
    

    



#Defining the routes

@app.route("/")
def home():
    return get_html("index")

@app.route("/allmovies")
def get_movies():
    movie_page = get_html("allmovies")
    movies_list = get_list()
    movies_list = sorted(movies_list)
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
    onemovie_page = get_html_sub("onemovie",movie_noun = movie_name)
    movie_info = Moviz.populate_moviz("moviesdetails.txt")
    #Using the print(movie_info) to check the format of the movie info
    #Using the movie_found for the loop.
    movie_found = False
    #Replace the _ in order to compare with the movie title in the movie_info
    movie_param = movie_name.replace("_"," ")
    
#use the class movie to complete each page
    for movie in movie_info:
        if movie.title == movie_param:
            movie_found = True
            movie_path = movie_name + ".txt"
            movie_content = get_comment(movie_path)
            update_page = onemovie_page.replace("&&DETAIL&&",Moviz.movie_info(movie))
            update_page = update_page.replace("&&COMM&&",movie_content)
            return update_page
    if not movie_found:
        return onemovie_page.replace("&&DETAIL&&","404 No Page found")

@app.route("/onemovie/<movie_name>", methods=["POST"])
def watched_movie(movie_name):
    onemovie_page = get_html_sub("onemovie", movie_noun = movie_name)
    movie_info = Moviz.populate_moviz("moviesdetails.txt")
    # #movie_choice = request.form.get("MovieDecision")
    comment = request.form.get("MyComment")
    movie_link = movie_name.replace("_"," ")

    if "SaveComment" in request.form:
        for movie in movie_info: 
            if movie.title == movie_link:
                if comment != "":
                    movie_comment = ""
                    movie_comment = movie_comment + str(comment)
                    movie_path = movie_name + ".txt"
                    save_movie(movie_path,movie_comment)
                    movie_content = get_comment(movie_path)

                    #update_page = onemovie_page.replace("{{ movie_name }}",movie_name)
                    update_page = onemovie_page.replace("&&DETAIL&&",Moviz.movie_info(movie))
                    update_page = update_page.replace("NO", "YES")
                    update_page = update_page.replace("&&COMM&&",movie_content)
                    return update_page
                else: 
                    return "Movie not found"
    else: 
        return "Movie not found"
    

@app.route("/result")
def search_notes():
    resultp = get_html("result")
    movies_list = get_list()
    note = flask.request.args.get("mySearch")
    value = ""
    found_match = False
    for movie in movies_list:
        if str(note).lower() in str(movie).lower():
            movie = movie.strip()
            movie_param = movie.replace(" ","_")
            value = value + "<p>" + "<a class="+"menulink"+" href="+"/onemovie/"+movie_param+"> " + movie +  "</a> </p>"
            found_match = True
    if not found_match :
        value =  "<p> No Result found ! Surely a move from The Riddler... </p>"
    return resultp.replace("&&RESULT&&",value)
