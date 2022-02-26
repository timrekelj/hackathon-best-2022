from flask import render_template, Flask, Response
from app_mod import functions
from tinydb import TinyDB, Query

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    db = TinyDB('db.json')
    functions.initialize()
    return render_template('index.html', title='Home', data=db.all(), fixed=False)


@app.route('/fixed', methods=['GET', 'POST'])
def fixed():
    db = TinyDB('db.json')
    for value in db.all():
        functions.fix(db, value['date'])
    return render_template('index.html', title='Home', data=db.all(), fixed=True)


@app.route('/export', methods=['GET', 'POST'])
def export():
    db = TinyDB('db.json')
    functions.export(db.all())
    with open("poraba-2021.csv") as fp:
        csv = fp.read()
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=poraba-2021.csv"}
    )

@app.route('/exportfixed', methods=['GET', 'POST'])
def exportfixed():
    data, fixedData = functions.initialize()
    functions.export(fixedData)
    with open("poraba-2021.csv") as fp:
        csv = fp.read()
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=poraba-2021.csv"}
    )


if __name__ == "__main__":
    app.run()
