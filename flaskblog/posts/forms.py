from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('Judul', validators=[DataRequired()])
    content = TextAreaField('Isi', validators=[DataRequired()])
    submit = SubmitField('Post')