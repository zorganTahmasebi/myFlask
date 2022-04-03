from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello World</h1>"

@app.route('/test/<name>')
def test(name):
    return f"My name is {name}"

@app.route('/homeAmin/<name>')
def home(name):
    name = "    Hello <strong> amin</strong>"
    fav_pizza = ["peperoni", "pasta", 'chese']
    return render_template('index.html', user_name=name, fav = fav_pizza)


# create custom erro pages 
# invalid url

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# internal server error 
@app.errorhandler(500)
def server_not_fount(e):
    return render_template("500.html"), 500