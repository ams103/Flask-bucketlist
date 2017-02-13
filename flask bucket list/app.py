from flask import Flask, render_template

app = Flask(__name__)


@app.route('/showSignup')
def showSignup():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run()
