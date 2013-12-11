from confirmerator import app
from helpers import *
import os

@app.route("/", methods=["GET"])
def create(): return render("create.html")

@app.route("/c/<id>", methods=["GET"])
def confirm(id):
	return "confirm..."
	pass

@app.route("/templated/<path:filename>", methods=["GET"])
def templated(filename):
	staticfile = os.sep.join(["wedding/static",filename])
	if not os.path.exists(staticfile):
		return ""

	content = file(staticfile).read()

	return content

@app.route("/robots.txt", methods=["GET"])
def robots():
	return templated("robots.txt")
