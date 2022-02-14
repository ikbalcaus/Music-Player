from flask import *
import os, waitress


app = Flask(__name__)


@app.route("/")
def indexRoute():
	songs = os.listdir("static/music")
	if "desktop.ini" in songs:
		songs.remove("desktop.ini")
	number_of_songs = len(os.listdir("static/music")) - 1
	return render_template("index.html",
		songs = songs,
		number_of_songs = number_of_songs
	)


@app.errorhandler(404)
def error(error):
	return redirect("/")


@app.errorhandler(500)
def error(error):
	return redirect("/")


if __name__ == "__main__":
	waitress.serve(app, host="0.0.0.0", port=80)