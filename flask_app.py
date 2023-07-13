from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tables')
def data():
    return render_template('tables.html')


@app.route('/network')
def network():
    return render_template('network.html')


if __name__ == '__main__':
	app.run()

