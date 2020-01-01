from flask import Flask, render_template, Response
import csv
import sqlite3 as sql


app = Flask(__name__)

list_of_numbers=[1,2,3]
list_of_names=["Dennis", "Ming", "Bernice"]

@app.route("/")
def index():
    return render_template(
        "index.html", numbers=list_of_numbers, names=list_of_names
    )


if __name__ == "__main__":
    app.run(debug=True, port=8000)

