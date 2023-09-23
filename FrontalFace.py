from flask import Flask, request, render_template
import cv2


import cv2


app = Flask(__name__)


# Load the Haar cascade file
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Check if file was uploaded
    if 'source_image' not in request.files or 'target_image' not in request.files:
        return render_template('index.html', error='Please upload both source and target images.')

    source_file = request.files['source_image']
    target_file = request.files['target_image']

    # Check if file has allowed extension
    allowed_extensions = {'jpg', 'jpeg', 'png'}
    if source_file.filename.split('.')[-1].lower() not in allowed_extensions or \
       target_file.filename.split('.')[-1].lower() not in allowed_extensions:
        return render_template('index.html', error='Invalid file format. Please upload images in JPG or PNG format.')

    # Save the uploaded files
    source_file.save('static/source.jpg')
    target_file.save('static/target.jpg')

    # Load the image files
    source_img = cv2.imread('static/source.jpg')
    target_img = cv2.imread('static/target.jpg')

    # Convert the source image to grayscale
    gray = cv2.cvtColor(source_img, cv2.COLOR_BGR2GRAY)

    # Detect the faces in the source image
    source_faces = face_detector.detectMultiScale(gray, 1.3, 5)

    if len(source_faces) == 0:
        return render_template('index.html', error='No face detected in source image.')

    # Extract the first face detected
    (x, y, w, h) = source_faces[0]

    # Extract the face ROI
    source_face_roi = source_img[y:y+h, x:x+w]

    # Convert the target image to grayscale
    gray = cv2.cvtColor(target_img, cv2.COLOR_BGR2GRAY)

    # Detect the faces in the target image
    target_faces = face_detector.detectMultiScale(gray, 1.3, 5)

    if len(target_faces) == 0:
        return render_template('index.html', error='No face detected in target image.')

    # Extract the first face detected
    (x, y, w, h) = target_faces[0]

    # Extract the face ROI
    target_face_roi = target_img[y:y+h, x:x+w]

    # Resize the source face ROI to the size of the target face ROI
    source_face_roi_resized = cv2.resize(source_face_roi, (w, h))

    # Swap the faces
    target_img[y:y+h, x:x+w] = source_face_roi_resized

    # Save the generated deepfake image
    deepfake_filename = 'static/deepfake.jpg'
    cv2.imwrite(deepfake_filename, target_img)

    return render_template('result.html', deepfake_filename=deepfake_filename)



if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)
