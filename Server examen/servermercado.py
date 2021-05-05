
from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG']= True

@app.route('/', methods=['GET'])
def home():
	return render_template("Html.html")
@app.route('/integrantes', methods=['GET'])
def integrantes():
	return render_template("integrantes.html")
app.run()