import os
from flask import Flask, render_template, send_from_directory


app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/vt2018')
def vt2018():
    return render_template('vt2018.html')


if __name__ == '__main__': app.run(debug=True)