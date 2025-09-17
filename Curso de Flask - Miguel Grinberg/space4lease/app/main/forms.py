import sqlalchemy as sa
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, FormField, SubmitField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Length
from flask_babel import _, lazy_gettext as _l
from app import db
from app.models import User

class Reserva(FlaskForm):
    nome_completo = StringField('Nome completo', validators = [DataRequired()])
    