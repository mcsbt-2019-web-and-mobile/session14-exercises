---
title: session 14
---

#

## Software development for web and mobile. Session 14

#

## Plan for today

* Using databases in Python

#

## sqlite

Today we'll be usign SQLite database engine.  SQLite is cool because
we don't need to have a database service running, it's just a file in
our commputer that contains all the data.

https://sqlite.org/index.html

## flask-sqlalchemy

The library that we'll be using to communicate with sqlalchemy from
python is called sqlalchemy and, although it comes installed with
Anaconda, we will use the flask bindings.  You can install them with:

`pip install flask-sqlalchemy` or `conda install flask-sqlalchemy`

#

## DB structure

Today we'll use a blog as the application for all our examples. We
will have three tables in the blog:

## Users

``` sql
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL
);
```

## posts

``` sql
CREATE TABLE IF NOT EXISTS posts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(255) NOT NULL,
  content VARCHAR(512) NOT NULL,
  id_USER INTEGER NOT NULL,
  FOREIGN KEY(id_user) REFERENCES users(id)
);
```

## comments

``` sql
CREATE TABLE IF NOT EXISTS comments (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  content VARCHAR(255) NOT NULL,
  user VARCHAR(100) NOT NULL,
  id_post INTEGER,
  FOREIGN KEY(id_post) REFERENCES posts(id)
);
```

#

## Connecting to the database

Using SQLAlchemy, connecting to the database is fairly easy.  We just
need to provide the database uri like this:

``` python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
```

## 

if we were not using sqlite but postgres, for example, we could
connect with:

``` python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:secret@localhost'
```

#

## Reading data from the database

Using the `db` object, we can make queries to the database:

``` python
result = db.engine.execute(query)
```

## Example 1

See `example1` folder.

## Exercise time

Let's modify the example 1 to make it possible to see detailed blog
posts.  In the detailed view, one should be able to see the post
title, who wrote it, and the contents.

# 

## Security: SQL Injection

#

## Configuring the database with Flask
