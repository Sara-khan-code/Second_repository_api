from flask import Flask, render_template

#create a flask instance
app = Flask(__name__)

#create a route decorator
@app.route("/")

def index():
    first_name = "Faiza"
    stuff = "This is our <strong>Bold</strong> text"
    favorite_pizza = ["cheese", "pepproni", "chicken", 23]
    bold_pizza = "<strong>Pizza list </strong>"
    return render_template("index.html", firstname = first_name, bold_stuff = stuff,
                           fav_piza = favorite_pizza, piza_bold = bold_pizza)


#create custom error pages
#Invalid URL
@app.errorhandler(404)

def page_not_found(e):
    return render_template("404.html"), 404

#Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
    
@app.route("/user/<name>")

def user(name):
    
    return render_template("user.html", user_name=name)
   # return "<h1>Hello {}!!!</h1>".format(name)

if __name__ == "__main__":
    app.run(debug=True)