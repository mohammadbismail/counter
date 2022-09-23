from crypt import methods
from pydoc import render_doc
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"


@app.route("/")
def index():
    return render_template("index.html")


app.route("/count", methods=["POST"])

def count():
    return redirect()


@app.route("/destroy_session")
def destroy():
    return render_template("")


if __name__ == "__main__":
    app.run(debug=True)
