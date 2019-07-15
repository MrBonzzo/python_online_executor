from wtforms import TextAreaField
from flask_wtf import FlaskForm


class CodeForm(FlaskForm):
    code = TextAreaField('code')
    stdin = TextAreaField('stdin')
