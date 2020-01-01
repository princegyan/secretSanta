from flask import Flask, render_template, Response, request 
from queries.queries import *

app = Flask(__name__)


@app.route("/")
def index():
    
    return render_template(
        "index.html", numbers=getnumbers()
    )

@app.route("/fetch", methods=["GET","POST"])
def fetch():
    if request.method == 'GET':
        return('''
        <h2>Are you sure you are authorized</h2>
        ''')
    else:
        user_removed = False
        number = request.form['number']
        name=getnamebynumber(number)
        if name == None:
            user_removed =True
            return render_template("returnedname.html", name=name,user_removed=user_removed)

        else:
            removeuser(number)
            return render_template("returnedname.html", name=name[0],user_removed=user_removed)


if __name__ == "__main__":
    app.run(debug=True, port=8000)

