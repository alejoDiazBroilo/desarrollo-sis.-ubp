from flask import Blueprint,render_template,redirect,url_for,g
from models.databases import partidos


Home = Blueprint("Home",__name__)

@Home.route("/")
def getHome():
    g.partidos = partidos
    g.len_partidos = len(partidos)
    return render_template("home/home.html")





