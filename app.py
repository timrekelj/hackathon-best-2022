from flask import render_template, Flask, Response
from app_mod import functions
# from tinydb import Tinydb, Query

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    data = functions.initialize()
    return render_template('index.html', title='Home', data=data)


@app.route('/fixed', methods=['GET', 'POST'])
def fixed():
    data = functions.initialize()
    data = functions.fix(data)
    return render_template('index.html', title='Home', data=data)


@app.route('/export', methods=['GET', 'POST'])
def export():
    data = functions.initialize()
    functions.export(data)
    with open("poraba-2021.csv") as fp:
        csv = fp.read()
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=poraba-2021.csv"}
    )


if __name__ == "__main__":
    app.run()
