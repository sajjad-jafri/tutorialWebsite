from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/courses")
def courses():
    return render_template("courses.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/courses/python")
def python():
    return render_template("python/python.html")

@app.route("/courses/python/Introduction")
def pythonIntro():
    return render_template("python/python_intro.html")

@app.route("/courses/python/Input-Output")
def pythonInputOutput():
    return render_template("python/inpOut.html")

@app.route("/courses/Python/Data-Types")
def dataTypes():
    return render_template("python/dataTypes.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
