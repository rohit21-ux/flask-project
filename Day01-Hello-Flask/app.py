from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Welcome Rohit !</h1>"

@app.route("/about")
def about():
    return "<h1> About page!</h1>"

@app.route("/contact")
def contact():
    return "<h1> Contact Page</h1>"

@app.route("/feedback")
def feedback():
    return "<h2> Feedback</h2>"

@app.route("/skills")
def skills():
    return "<h1> Python,SQL,Git,Flask</h1>"

@app.route("/projects")
def projects():
    return "<h1>Flask Journey Project</h1>"

@app.route("/github")
def github():
    return "<h1>rohit21-ux</h1> "

@app.route("/user/<name>")
def user(name):
    return f"<h1> Welcome {name}!</h1>"


if __name__ == "__main__":
    app.run(debug=True)

