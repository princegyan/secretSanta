from flask import Flask, render_template, Response, request 
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

@app.route("/fetch", methods=["GET","POST"])
def fetch():
    if request.method == 'GET':
        returned_number="Dennis"
        if returned_number =="" or None:
            return render_template("returnedname.html", name="No name")
        else:
            return render_template("returnedname.html", name="returned_number")

    else:
        number = request.form['number']
        return render_template("returnedname.html", name=number)


if __name__ == "__main__":
    app.run(debug=True, port=8000)

