from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1> Hello World! </h1>"

@app.route("/info")
def info():
    return "<h1> Hello Universe! </h1>"

#Dynamic Routing
@app.route("/profile/<name>")
def main_profile(name):
    return "<h1> This is a page for {} </h1>".format(name.title())

if __name__ == "__main__":
    app.run(debug=True)