from flask import Flask, render_template

app = Flask(__name__)


# Home Page
@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")

# Courses Page
@app.route("/courses/")
def courses():
    return render_template("courses.html")

# About Page
@app.route("/about/")
def about():
    return render_template("about.html")

# Contact Page
@app.route("/contact/")
def contact():
    return render_template("contact.html")


@app.route("/courses/python/")
def python():
    return render_template("courses/python/python.html")

@app.route("/courses/python/Introduction/")
def pythonIntro():
    return render_template("courses/python/python_intro.html")

@app.route("/courses/python/Input-Output/")
def pythonInputOutput():
    return render_template("courses/python/inpOut.html")

@app.route("/courses/python/Data-Types/")
def pythonDataTypes():
    return render_template("courses/python/dataTypes.html")

@app.route("/courses/python/Control-Flow-If-Statements/")
def pythonIfStatements():
    return render_template("courses/python/ifStatements.html")

@app.route("/courses/python/For-Loop/")
def pythonForLoop():
    return render_template("courses/python/forLoop.html")

@app.route("/courses/python/While-Loop/")
def pythonWhileLoop():
    return render_template("courses/python/whileLoop.html")

@app.route("/courses/python/Transfer-Statements/")
def pythonTransferStatements():
    return render_template("courses/python/transferStatements.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
