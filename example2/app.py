from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

@app.route("/")
def root():
    query = """
    SELECT p.id, p.title, u.name 
    FROM posts p
    INNER JOIN users u
    ON u.id = p.id_user
    """

    posts = db.engine.execute(query)

    return render_template("main.html", posts=posts)

@app.route("/post/<id>")
def show_post(id):
    query = """
    SELECT p.title, p.content, u.name 
    FROM posts p
    INNER JOIN users u
    ON u.id = p.id_user
    WHERE p.id = {}
    """

    post = db.engine.execute(query.format(id)).fetchone()

    return render_template("post.html", post=post)

@app.route("/new_post")
def new_post():
    return render_template("newpost.html")

@app.route("/insert_post", methods = ["POST"])
def insert_post():
    query = """
    INSERT INTO posts (title, content, id_user)
    VALUES ('{}', '{}', 1)
    """

    title = request.form["title"]
    form = request.form["content"]

    db.engine.execute(query.format(title, form))

    return "new post written"

db.init_app(app)
app.run()