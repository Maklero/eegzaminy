from app import db
from sqlalchemy.sql.expression import func


class UsersModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(85), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)


def BasicExamModel(name):
    class Model(db.Model):
        __tablename__ = 'exam_{name}'.format(name=name)

        def __init__(self, examName):
            self.__tablename__ = 'exam_{}'.format(examName)

        id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True, nullable=False)
        question = db.Column(db.Text, nullable=False)
        A = db.Column(db.Text, nullable=False)
        B = db.Column(db.Text, nullable=False)
        C = db.Column(db.Text, nullable=False)
        D = db.Column(db.Text, nullable=False)
        answer = db.Column(db.Text, nullable=False)
        img = db.Column(db.Text, nullable=True)

        @classmethod
        def questions(cls, quantity=40):
            return cls.query.order_by(func.random()).limit(quantity)

        @classmethod
        def oneQuestion(cls, nr):
            return cls.query.filter_by(id=nr).first()

    return Model
