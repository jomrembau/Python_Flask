from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = "Shea"
    letters = list(name)
    pup_dict = {"puppy_name" : "Z" }
    return render_template("index.html", name = name, letters=letters, pup_dict = pup_dict)

if __name__ == "__main__":
    app.run(debug=True)