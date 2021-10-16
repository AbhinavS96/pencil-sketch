#import cv2

# read the image
#image = cv2.imread("images/image.jpg")

# creating the pencil sketch directly
#image_out = cv2.pencilSketch(image, sigma_s=60, sigma_r=0.07, shade_factor=0.05)

# save the images
#cv2.imwrite("images/sketch.jpg", image_out[0])
#cv2.imwrite("images/sketch-color.jpg", image_out[1])

from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def hello():
    return {'key': 'hello'}


if __name__ == '__main__':
    app.run(debug=True)