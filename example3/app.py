from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import app, db
from models import Post

@app.route("/")
def root():
    posts = Post.query.all()

    return render_template("main.html", posts=posts)

@app.route("/post/<id>")
def show_post(id):
    post = Post.query.get(id)

    return render_template("post.html", post=post)

@app.route("/new_post")
def new_post():
    return render_template("newpost.html")

@app.route("/insert_post", methods = ["POST"])
def insert_post():
    title = request.form["title"]
    content = request.form["content"]

    post = Post(title=title, content=content, id_user=1)

    db.session.add(post)
    db.session.commit()

    return "new post written"

db.init_app(app)
app.run()