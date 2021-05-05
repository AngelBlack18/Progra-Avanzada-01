from flask import Flask, redirect, url_for,render_template


app = Flask(__name__)
app.config['DEBUG']= True

@app.route('/')
def home():
    return render_template("Nopuedes.html")


if __name__ == '__main__': 
    app.run()