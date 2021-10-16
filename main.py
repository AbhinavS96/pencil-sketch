from flask import Flask, url_for
from flask_cors import CORS, cross_origin
import cv2

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#setting custom values for sanity
localhost = '127.0.0.2'
my_port = '5000'


#pencil sketch API
@app.route('/pencilsketch')
@cross_origin()
def pencil():
    #read the image. Currently using a local file. Will have to receive this from frontend
    image = cv2.imread("static/image.jpg")

    # creating the pencil sketch directly
    image_out = cv2.pencilSketch(image,
                                 sigma_s=60,
                                 sigma_r=0.07,
                                 shade_factor=0.05)

    #save the images
    cv2.imwrite("static/pencil_sketch.jpg", image_out[0])

    return {'path': url_for('static', filename='pencil_sketch.jpg')}


#color pencil sketch API
@app.route('/colorpencilsketch')
@cross_origin()
def colorpencil():
    #read the image. Currently using a local file. Will have to receive this from frontend
    image = cv2.imread("static/image.jpg")

    # creating the pencil sketch directly
    image_out = cv2.pencilSketch(image,
                                 sigma_s=60,
                                 sigma_r=0.07,
                                 shade_factor=0.05)

    #save the images
    cv2.imwrite("static/color_pencil_sketch.jpg", image_out[1])

    return {'path': url_for('static', filename='color_pencil_sketch.jpg')}


if __name__ == '__main__':
    app.run(host=localhost, port=my_port, debug=True)