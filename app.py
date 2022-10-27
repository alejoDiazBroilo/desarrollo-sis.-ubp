from flask import Flask


from routes.home import Home


app = Flask(__name__)
app.secret_key = 'mysecretkey'





app.register_blueprint(Home)


