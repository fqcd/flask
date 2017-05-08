# 程序路由
from flask import render_template, session, redirect, url_for
from datetime import datetime
from . import main
from .forms import NameForm
from .. import db
from ..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
          # if app.config['FLASK_ADMIN']:
             #  send_email(app.config['FLASK_ADMIN'], 'New user', 'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        #  old_name = session.get('name')
        #  if old_name is not None and old_name != form.name.data:
        #    flash ('Look like you have changed your name!')
        return redirect(url_for('main.index'))
    return render_template('index.html', form=form, name=session.get('name'),
                           current_time=datetime.utcnow(), known=session.get('known', False))  # 本地化时间和日期
@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)  # 模版渲染