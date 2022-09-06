from turtle import title
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db = SQLAlchemy(app)

basedir = os.path.abspath(os.path.dirname(__file__))

# configurations for DB
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'KHRISTOPHERPRACTICE'

class job(db.Model):
    __tablename__ = 'job'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    def __repr__(self) -> str:
        return '<Job %s>' % self.title

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, job=job)