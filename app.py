from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():

	phrase_comme_string = "Hello, World ! My master will rule the world for ever. Hahahaha"

	phrase_comme_tableau = ["Hello", "World", "My", "master", "will", "rule", "you", "for", "ever", "Hahahaha"]

	return render_template('main.html', titre="Bienvenue !", phrase_comme_tableau=phrase_comme_tableau, phrase_comme_string=phrase_comme_string)

if __name__ == '__main__':

	app.run(host='0.0.0.0', port=5000)
