from app import db, login
from flask import current_app
import sqlalchemy as sa
import sqlalchemy.orm as so
from flask_login import UserMixin
from typing import Optional
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key = True)
    nome_completo: so.Mapped[str] = so.mapped_column(sa.String(64), index = True, unique = True)
    username: so.Mapped[str] = so.mapped_column(sa.String(32), index = True, unique = True)
    email: so.Mapped[str] = so.mapped_column(sa.String(64), index = True, unique = True)
    senha_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

class Reserva(db.Model):
    id: