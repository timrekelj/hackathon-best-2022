from flask import render_template, Flask
from app_mod import functions

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    data = functions.initialize()
    return render_template('index.html', title='Home', data=data)


@app.route('/fixed', methods=['GET', 'POST'])
def fixed():
    data = functions.initialize()
    data = functions.fix()
    return render_template('index.html', title='Home', data=data)


@app.route('/export', methods=['GET', 'POST'])
def export():
    data = functions.initialize()
    data = functions.export()
    return render_template('index.html', title='Home', data=data)


if __name__ == "__main__":
    app.run()
