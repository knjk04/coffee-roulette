# TODO: fix imports with venv
from flask import Flask, send_from_directory
from flask_cors import CORS

from pair_people import display_pairings, pair

from excel.writer import create_workbook, workbook_name, workbook_parent_dir
from excel.reader import read_first_column

app = Flask(__name__)
cors = CORS(app, origins=['http://localhost:4200'])


people = {''}


# TODO: export as spreadsheet
def main():
    global people
    people = read_first_column('sample_people.xlsx')

    pairings = pair(people)
    display_pairings(pairings)


@app.route("/api/pair", methods=["POST"])
def test_route():
    try:
        global people
        people = read_first_column('sample_people.xlsx')
        print(people)
    except FileNotFoundError:
        return "File not found", 400

    create_workbook()
    return send_from_directory(directory=workbook_parent_dir(), path=workbook_name(), as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
