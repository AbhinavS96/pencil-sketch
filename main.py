#import cv2

# read the image
#image = cv2.imread("images/image.jpg")

# creating the pencil sketch directly
#image_out = cv2.pencilSketch(image, sigma_s=60, sigma_r=0.07, shade_factor=0.05)

# save the images
#cv2.imwrite("images/sketch.jpg", image_out[0])
#cv2.imwrite("images/sketch-color.jpg", image_out[1])

from flask import Flask, url_for
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

localhost = '127.0.0.2'
my_port = '5000'


@app.route('/image')
@cross_origin()
def host():
    return {'path': url_for('static', filename='image.jpg')}


if __name__ == '__main__':
    app.run(host=localhost, port=my_port, debug=True)