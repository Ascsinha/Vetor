from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, FormField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_babel import _, lazy_gettext as _l
import sqlalchemy as sa
from app import db
from app.models import User

class Login(FlaskForm):
    username = StringField(_l('Nome completo'), validators = [DataRequired()])
    senha = PasswordField(_l('Senha'), validators = [DataRequired()])
    lembre_me = BooleanField(_l('Lembre-me'))
    enviar = SubmitField(_l('Enviar'))

class Telefone(FlaskForm):
    pais_codigo = IntegerField(_l('Código do país'), validators = [DataRequired()])
    area_codigo = IntegerField(_l('Código de área'), validators = [DataRequired()])
    numero = StringField(_l('Número'))

class Cadastro(FlaskForm):
    nome_completo = StringField(_l('Nome completo'), validators = [DataRequired()])
    username = StringField(_l('Username'), validators = [DataRequired()])
    email = StringField(_l('E-mail'), validators = [DataRequired(), Email()])
    telefone = FormField(Telefone)
    senha = PasswordField(_l('Senha'), validators = [DataRequired()])
    senha2 = PasswordField(_l('Repita sua senha'), validators = [DataRequired(), EqualTo('senha')])
    enviar = SubmitField(_l('Enviar'))

    def validar_usuario(self, username):
        user = db.session.scalar(sa.select(User).where(User.username == username.data))
        if user is not None:
            return ValidationError(_l('Esse nome já está sendo usado.'))
        
    def validar_email(self, email):
        email = db.session.scalar(sa.select(User).where(User.email == email.data))
        if email is not None:
             return ValidationError(_l('Esse email já está sendo usado.'))