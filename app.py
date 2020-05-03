from flask import Flask, render_template, Response
from camera import Camera

app = Flask(__name__)
camera = Camera()

def display_camera():

	while True:

		frame = camera.get_frame()

		yield (b'--frame\r\n'
		       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/', methods=['GET'])
def home():

	phrase_comme_string = "Hello, World ! My master will rule the world for ever. Hahahaha"

	phrase_comme_tableau = ["Hello", "World", "My", "master", "will", "rule", "you", "for", "ever", "Hahahaha"]

	return render_template('main.html', titre="Bienvenue !", phrase_comme_tableau=phrase_comme_tableau, phrase_comme_string=phrase_comme_string)

@app.route('/video_displaying', methods=['GET'])
def video_display():

	return Response(display_camera(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':

	app.run(host='0.0.0.0', port=5000)
