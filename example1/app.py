from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

@app.route("/")
def root():
    query = """
    SELECT p.title, u.name 
    FROM posts p
    INNER JOIN users u
    ON u.id = p.id_user
    """

    posts = db.engine.execute(query)

    return render_template("main.html", posts=posts)

db.init_app(app)
app.run()