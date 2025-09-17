from flask import Flask, render_template
from flask_login import login_required
from flask_babel import _
from app.main.forms import Reserva
import sqlalchemy as sa
from app import db
from app.main import bp

@bp.route('/')
@bp.route('/homepage')
def homepage():
    return render_template('homepage.html', title = _('Homepage'))

@bp.route('/acomodacoes')
@login_required
def acomodacoes():
    return render_template('acomodacoes.html', title = _('Acomodações'))

@bp.route('/reservas') 
@login_required
def reservas():
    return render_template('reservas.html', title = _('Reservas'))
    
@bp.route('/servicos')
@login_required
def servicos():
    return render_template('servicos.html', title = _('Serviços'))

@bp.route('/perfil')
def perfil():
    return render_template('perfil.html', title = _('Perfil')) 