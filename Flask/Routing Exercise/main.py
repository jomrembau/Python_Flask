from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome! Go to/puppy_latin/name to see your name in puppy latin.</h1>"

@app.route("/puppy_latin/<name>")
def latin_page(name):
    if name[-1] == "y":
        latin_name = name[0:-1]
        return "<h1> Hi,{}! Your puppy latin name is {}iful! </h1>".format(name.title(), latin_name.title())

    else:
        return "<h1> Hi,{}! Your puppy latin name is {}y! </h1>".format(name.title(), name.title())


if __name__ == "__main__":
    app.run(debug=True)