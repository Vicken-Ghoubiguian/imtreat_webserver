import cv2

class Camera:

	def __init__(self):

		self.cap = cv2.VideoCapture(-1)

	def get_frame(self):

		_, self.frame = self.cap.read()

		_, jpeg = cv2.imencode('.jpg', self.frame)

		return jpeg.tobytes()

if __name__ == '__main__':

	camera = Camera()
