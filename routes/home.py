from flask import Blueprint,render_template,redirect,url_for,g
from models.databases import partidos,equipos,equipos_nombre


Home = Blueprint("Home",__name__)

@Home.route("/")
def getHome():
    g.equipos = equipos
    return render_template("home/home.html")





