from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = "Shea"
    letters = list(name)
    pup_dict = {"puppy_name" : "Z" }
    my_list = [1,2,3,4,5]
    return render_template("index.html", name = name, letters=letters, pup_dict = pup_dict, my_list=my_list)

if __name__ == "__main__":
    app.run(debug=True)