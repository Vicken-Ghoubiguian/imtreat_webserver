from flask import Flask, render_template, Response

import cv2
import sys

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found_function(e):

	return render_template('errors.html', error_label="Error 404", error_description="Page not found, sorry..."), 404

@app.errorhandler(500)
def internal_problem_function(e):

	return render_template('errors.html', error_label="Error 500", error_description="Internal problem, sorry..."), 500

@app.route('/', methods=['GET'])
def home():

	phrase_comme_string = "Hello, World ! My master will rule the world for ever. Hahahaha"

	phrase_comme_tableau = ["Hello", "World", "My", "master", "will", "rule", "you", "for", "ever", "Hahahaha"]

	opencv_version = cv2.__version__

	python_version = sys.version

	python_version_info = sys.version_info

	return render_template('main.html', titre="Bienvenue !", phrase_comme_tableau=phrase_comme_tableau, phrase_comme_string=phrase_comme_string,opencv_version=opencv_version, python_version=python_version, python_version_info=python_version_info), 200

if __name__ == '__main__':

	app.run(host='0.0.0.0', port=5000)
