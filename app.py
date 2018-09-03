from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/vt2018')
def vt2018():
    return render_template('vt2018.html')


if __name__ == '__main__': app.run(debug=True)