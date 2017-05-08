from sqlalchemy.schema import Table
from . import db

# 映射类
class Role(db.Model):
    __tablename__ = 'roles'
    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')
    def __repr__(self):
        return '<Role %r>' % self.user_name
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'))
    def __repr__(self):
        return '<User %r>' % self.username
'''
roles = db.Table('roles',
             db.Column('role_id', db.Integer, primary_key=True),
             db.Column('role_name', db.String(64))
             )

users=db.Table('users',
               db.Column('id', db.Integer, primary_key=True),
               db.Column('username', db.String(64)),
               db.Column('role_id', db.Integer, db.ForeignKey('roles.role_id'))
              )
'''
