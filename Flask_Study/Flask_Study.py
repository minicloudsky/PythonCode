from flask import Flask
from flask import redirect
from flask import make_response
from flask import abort
from flask import render_template
app = Flask(__name__)
user = 'jiayawu'

@app.route('/')
def index():
    return render_template('index.html',name=user)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)




if __name__ == '__main__':
    app.run(debug=True)
