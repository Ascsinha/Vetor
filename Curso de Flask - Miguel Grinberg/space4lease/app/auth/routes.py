from app import db
from app.auth import bp
import sqlalchemy as sa 
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from flask_babel import _
from urllib.parse import urlsplit
from app.auth.forms import Login, Cadastro
from app.models import User

@bp.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        redirect(url_for('main.homepage'))
    form = Login()
    if form.validate_on_submit():
        user = db.session.scalar(sa.select(User).where(User.username == form.senha.data))
        if user is None or not user.checar_senha(form.senha.data):
            flash(_('Nome ou senha inválido.'))
            return redirect(url_for('auth.login'))
        login_user(user, remember = form.lembre_me.data)
        prox_pag = request.args.get('next')
        if not prox_pag or urlsplit(prox_pag).netloc != '':
            prox_pag = url_for('main.homepage')
        return redirect(prox_pag)
    render_template('auth/login.html', title = _('Entrar'), form = form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.homepage'))

@bp.route('/cadastro', methods = ['GET', 'POST'])
def cadastro():
    if current_user.is_authenticated:
        return redirect(url_for('main.homepage'))
    form = Cadastro()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data)
        user.set_password(form.senha.data)
        db.session.add(user)
        db.session.commit()
        flash(_('Parabéns, agora você está cadastrado!'))
        return redirect(url_for('auth.login'))
    render_template('auth/cadastro.html', title = _('Cadastrar'), form = form)