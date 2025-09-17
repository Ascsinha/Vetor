from flask import Flask, render_template
from flask_login import login_required
import sqlalchemy as sa
from app import db
from app.main import bp

@bp.route('/')
@bp.route('/homepage')
def homapage():
    return render_template('index.html', title = 'Home Page')

@bp.route('/reservas') 
def reservas():
    return render_template('reservas.html', title = 'Reservas')

@login_required
@bp.route('/servicos')
def servicos():
    return render_template('servicos.html', title = 'Serviços')