from app import db, login
from flask import current_app
import sqlalchemy as sa
import sqlalchemy.orm as so
from datetime import datetime, timezone
from flask_login import UserMixin
from typing import Optional
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key = True)
    nome_completo: so.Mapped[str] = so.mapped_column(sa.String(64), index = True, unique = True)
    username: so.Mapped[str] = so.mapped_column(sa.String(32), index = True, unique = True)
    telefone: so.Mapped[str] = so.mapped_column(sa.String(14), index = True, unique = True)
    email: so.Mapped[str] = so.mapped_column(sa.String(64), index = True, unique = True)
    senha_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    reservas = db.relationship('Reserva', backref = '/templates/historico_reservas.html')

class Reserva(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key = True)
    user_id: so.Mapped[id] = so.mapped_column(sa.ForeignKey(User.id))
    user_telefone: so.Mapped[str] = so.mapped_column(sa.ForeignKey(User.telefone))
    qtd_pessoas: so.Mapped[int] = so.mapped_column(index = True)
    data: so.Mapped[Optional[datetime]] = so.mapped_column(index = True, default = lambda: datetime.now(timezone.utc))
    mensagem: so.Mapped[str] = so.mapped_column(sa.String(140))