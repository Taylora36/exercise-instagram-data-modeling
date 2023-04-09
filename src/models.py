import os
import sys
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    """
    User
    ----
    id int PK
    email unique string
    nickname string
    password string
    """
    __tablename__ = "user"
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(256), unique=True, nullable=False)
    nickname = Column(String(256))
    phone = Column(String(16), unique=True)
    password = Column(String(256), nullable=False)
    profilepic = Column(String(256))

class Follow(Base):
    """
    Follow
    ----
    follower_id int PK FK >- User.id
    following_id int PK FK >- User.id
    """
    __tablename__ = "follow"
    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, ForeignKey("user.id"))
    following_id = Column(Integer, ForeignKey("user.id"))

class Post(Base):
    """
    Post
    ----
    id int PK
    user_id int PK FK >- User.id
    media string
    description string
    """
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    description = Column(String(256))
    likes = Column(Integer)
    comments = Column(String(256))
    collection_id = Column(Integer, ForeignKey("collection.id"))
    created = Column(DateTime, default=datetime.now)
    edited = Column(DateTime, default=None, onupdate=datetime.now)

class Comment(Base):
    """
    Comment
    ---
    id int PK
    post_id int FK >- Post.id
    user_id int FK >- User.id
    content string
    created datetime
    """
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))
    description = Column(String(256))
    created = Column(DateTime, default=datetime.now)
    edited = Column(DateTime, default=None, onupdate=datetime.now)

class Collection(Base):
    """
    Collection
    ----
    id int PK
    user_id int PK FK >- User.id
    title string
    """
    __tablename__ = "collection"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))

class Media(Base):
     __tablename__ = "media"
     id = Column(Integer, primary_key=True)
     url = Column(String(256))
     post_id = Column(Integer, ForeignKey("post.id"))





## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
