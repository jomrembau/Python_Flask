from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check")
def check():
    username = request.args.get("username")

    lower_case = False
    upper_case = False
    missing_end_number = False

    if username:
        if not username[-1].isnumeric():
            missing_end_number = True

        for char in username:
            if char.isupper():
                upper_case = True
                break

        for char in username:
            if char.islower():
                lower_case = True
                break


    return render_template("check.html", username=username, lower_case=lower_case, upper_case=upper_case, missing_end_number=missing_end_number)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(debug=True)