from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY']='hard to guess string'
bootstrap=Bootstrap(app)

class NameForm(FlaskForm):
    name=StringField('What is your name?', validators=[DataRequired()])
    submit=SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():  #홈페이지
    name = None
    form= NameForm()
    if form.validate_on_submit():
        name=form.name.data
        form.name.data=' '
    return render_template('index.html', form=form, name=name)
@app.route('/user/<name>')
def user(name):  #네임페이지
    return render_template('user.html', name=name)
@app.errorhandler(404)#페이지 못 찾을때
def page_not_found(e):
    return render_template('404.html'),404
@app.errorhandler(500)#서버 고장
def internal_server_error(e):
    return render_template('500.html'),500

if __name__ == '__main__':
    app.run()
