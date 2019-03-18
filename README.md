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

Today we'll be usign SQLite database engine.  SQLite comes handy
because we don't need to have a database service running, it's just a
file in our computer that contains all the data.

[https://sqlite.org/index.html](https://sqlite.org/index.html)

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

## Modifying data in the Database

So far we've only read data from the DB.  Let's see how we would
modify data in the database.

## Example 2

see `example2` folder.

## exercise

make it possible to add comments to the posts in the blog.  Comments
will require your name and some content.

#

## Security: SQL Injection

Does anybody know what's SQL injection?

## The problem

If we dont _sanitize_ user input, it may go directly to our database,
meaning that we may be giving direct access to our data through our
forms.

## Example problem

in the example of adding a post, we could add the following as *post content*:
 
```
',1) union select * from users; --
```

## Explaination

in the beginning of the previous example we're finishing the current
SQL statement, and then adding more parts to the query.

``` sql
INSERT INTO posts (title, content, id_user)
VALUES ('a', '', 1) union select user, password from users; --
```

## the solution, prepared statements

prepared statements, the db library detects when the query is being
hijacked and stops it from being run in the database directly.
They're really simple to use, we just need to parametrise our queries
with `:keywords`, that we can substitute later.

##

``` sql
query = """
    SELECT p.title, p.content, u.name 
    FROM posts p
    INNER JOIN users u
    ON u.id = p.id_user
    WHERE p.id = :id
    """
	
db.engine.execute(query, id=post_id)
```

#

