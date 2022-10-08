from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/activity1')
def activity1():
    return render_template('activity1.html')

@app.route('/activity2')
def activity2():
    return render_template('activity2.html')

@app.route('/activity3')
def activity3():
    return render_template('activity3.html')

app.run(host="localhost", debug=True)