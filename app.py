from flask import Flask, render_template, Response

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found_function(e):

	return "<h1 style='color: red;'>Error 404: Page not found, sorry...</h1>", 404

@app.errorhandler(500)
def internal_problem_function(e):

	return "<h1 style='color: red;'>Error 500: Internal problem, sorry...</h1>", 500

@app.route('/', methods=['GET'])
def home():

	phrase_comme_string = "Hello, World ! My master will rule the world for ever. Hahahaha"

	phrase_comme_tableau = ["Hello", "World", "My", "master", "will", "rule", "you", "for", "ever", "Hahahaha"]

	return render_template('main.html', titre="Bienvenue !", phrase_comme_tableau=phrase_comme_tableau, phrase_comme_string=phrase_comme_string), 200

if __name__ == '__main__':

	app.run(host='0.0.0.0', port=5000)
