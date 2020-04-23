from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():

	return "Hello, World ! My master will rule the world for ever. Hahahaha"

if __name__ == '__main__':

	app.run(host='0.0.0.0', port=5000)
