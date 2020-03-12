from flask_wtf import FlaskForm
from sqlalchemy_serializer import SerializerMixin
from wtforms import StringField, TextAreaField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class AddJobForm(FlaskForm):
    job = StringField('Название работы', validators=[DataRequired()])
    team_leader = IntegerField('ID Тим-лида', validators=[DataRequired()])
    work_size = StringField('Размер работы', validators=[DataRequired()])
    collaborators = StringField('Рабочие', validators=[DataRequired()])
    is_finished = BooleanField('Закончна работа?')

    submit = SubmitField('Submit')
