from flask import Flask, render_template

app = Flask(__name__)


# Home Page
@app.route("/home/")
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

# Dynamic route for courses and chapters
@app.route("/courses/<course_name>/")
def display_course(course_name):
    return render_template(f"courses/{course_name}.html")

# Dynamic route for chapters within a course
@app.route("/courses/<course_name>/<chapter_name>/")
def display_chapter(course_name, chapter_name):
    active_chapter = chapter_name
    return render_template(f"courses/{course_name}/{chapter_name}.html", active_chapter = active_chapter)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
