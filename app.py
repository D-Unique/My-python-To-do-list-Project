from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime 

# create a Flask Instance
app = Flask(__name__)
app.url_map.strict_slashes = False
users = ( 'Maryann', 'Anthony', 'Darren', 'Emma')
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
@app.route('/sign in')
def signin():
    return 'PLEASE SIGN IN'

@app.route('/')
def home():
    return 'HOME PAGE'

@app.route('/<myurs>')
def index(myurs):
    if myurs in users:
        return render_template('index.html',urs1=myurs)
    else:
        return redirect(url_for('signin'))

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
