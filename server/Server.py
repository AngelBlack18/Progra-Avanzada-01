from flask import Flask, redirect, url_for,render_template


app = Flask(__name__)


@app.route('/')
def test2():
    return render_template("Nopuedes.html")


if __name__ == '__main__': 
    app.run()