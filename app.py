from flask import Flask, render_template, url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, email, equal_to
#from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime 

# create a Flask Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "My supersecret key"
app.url_map.strict_slashes = False
users = ( 'Maryann', 'Anthony', 'Darren', 'Emma')

# create a class form
class SignUpForm(FlaskForm):
    fname = StringField("First Name", validators=[DataRequired()])
    lname = StringField("Last Name", validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    passwd = PasswordField('password', validators=[DataRequired()])
    compasswd = PasswordField('comfirm password', validators=[DataRequired()])
    submit = SubmitField('submit')


#add database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

#db = SQLAlchemy(app)


"""class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=dateTime.utcnow)

    def __repr__(self):
        return '<Name %r>' %self.name"""

# create a route decorator

#Sign in page
@app.route('/sign in', methods=['GET', 'POST'])
def signin():
    fname = None
    lname = None
    email = None
    passwd = None
    compasswd = None
    form = SignUpForm()
    
    
    #validate Form
    if form.validate_on_submit():
        #fname
        fname = form.fname.data
        form.fname.data = ''
        #lname
        lname = form.lname.data
        form.lname.data = ''
        #email
        email = form.email.data
        form.email.data = ''
        #passwd
        passwd= form.passwd.data
        form.passwd.data = ''
        #compasswd
        compasswd= form.compasswd.data
        form.compasswd.data = ''
        flash("Account Created!")

    return render_template('signup.html', fname = fname, lname = lname, email = email, passwd = passwd, compasswd = compasswd, form = form)

#landing page
@app.route('/')
def home():
    return render_template('landing_page.html')

#about page
@app.route('/about')
def about():
    return render_template('about.html')


#Index page
@app.route('/<myurs>')
def index(myurs):
    if myurs in users:
        return render_template('index.html',urs1=myurs)
    else:
        return redirect(url_for('signin'))

#add task page
@app.route('/task/<Turs>')
def task(Turs):
    return render_template('add_task.html', urs=Turs)


#Invalid error
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#Internal Server Error
@app.errorhandler(500)
def internal_server(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
