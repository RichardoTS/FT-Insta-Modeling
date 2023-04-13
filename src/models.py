import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

class Follower(Base):
    __tablename__ = 'followers'
    user_from_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    user_to_id = Column(Integer, ForeignKey('users.id'))

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    text = Column(String(250))
    likes = Column(Integer)

class File(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True)
    filetype = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'))

class Liked(Base):
    __tablename__ = 'liked_posts'
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'), primary_key=True)

class Comment(Base):
    __tablename__ = 'comments'
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'), primary_key=True)
    text = Column(String(250))

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
