import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Boolean, Numeric
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

t
class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    email = Column(String(250))
    yearsold = Column(Numeric)
    pasword = Column(String(8)) 
    bio= Column(String(250))
    follower = relationship('followers', secondary='userfollower')
    comment = relationship("Comments", uselist=False, back_populates="comments")

class Followers(Base):
    __tablename__ = 'followers'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    acepted = Column(Boolean)
    user = relationship('users', secondary='userfollower')
    
class UserFollower(Base): 
    __tablename__ = 'userfollower'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    user = relationship(Users)
    followers_id = Column(Integer, ForeignKey('followers.id'), primary_key=True)
    followers = relationship(Followers)


class Posts(Base):
    __tablename__ = 'posts'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users)
    photo = Column(String(250))
    description = Column(String(250))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users)
    comment = relationship("Comments", uselist=False, back_populates="comments")

class Likes(Base):
    __tablename__ = 'likes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post= relationship(Posts)
    

class Comments(Base):
    __tablename__ = 'comments'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment = Column(String(250))
    user_id = Column(Integer, ForeignKey('users.id'), back_populates="users")
    user = relationship(Users)
    post_id = Column(Integer, ForeignKey('posts.id'), back_populates="posts")
    post= relationship(Posts)

    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
