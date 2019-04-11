from app.extensions import db, ma
from sqlalchemy.sql.expression import func

def BasicExamModel(name):
    class Model(db.Model):
            __tablename__ = 'exam_{}'.format(name)
        
            __table_args__ = {'extend_existing': True}

            id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
            question = db.Column(db.Text, nullable=False)
            A = db.Column(db.Text, nullable=False)
            B = db.Column(db.Text, nullable=False)
            C = db.Column(db.Text, nullable=False)
            D = db.Column(db.Text, nullable=False)
            answer = db.Column(db.Text, nullable=False)
            img = db.Column(db.Text, nullable=True)

            @classmethod
            def oneQuestion(cls, nr):
                return cls.query.filter_by(id=nr).limit(1)

            @classmethod
            def questions(cls, quantity=40):
                return cls.query.order_by(func.random()).limit(quantity)
    
    return Model


class ExamsList(db.Model):
    __tablename__ = 'exams_list'

    id = db.Column(db.Integer, primary_key=True)
    exam_name = db.Column(db.Text)


class BasicExamSchema(ma.Schema):
    class Meta:
        fields = (
            'id',
            'question',
            'A',
            'B',
            'C',
            'D',
            'answer',
            'img')


class ExamsListSchema(ma.Schema):
    class Meta:
        fields = ('id', 'exam_name')