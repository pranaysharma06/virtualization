Face Swap Web Application

This is a simple web application that allows you to perform face swapping between two images. It uses the Flask framework and runs in a Docker container.

Table of Contents
-----------------
- Prerequisites
- Getting Started
- Usage
- Troubleshooting
- License

Prerequisites
-------------
Before running the application, ensure that you have the following prerequisites installed:
- Docker (https://www.docker.com/get-started)
- Python (for development)

Getting Started
---------------
1. Clone this repository to your local machine:

git clone https://github.com/yourusername/face-swap-app.git
cd face-swap-app

2. Build the Docker image:
docker build -t frontal-face-image .



3. Run the Docker container:

docker run -d --name frontal-face-container -p 5000:5000 frontal-face-image


4. Access the web application in your browser at http://localhost:5000.

Usage
-----
1. Open the web application in your browser.

2. Click the "Upload" button to upload a source image and a target image for face swapping. Both images should be in JPG or PNG format.

3. After uploading the images, click the "Generate Deepfake" button.

4. The application will process the images and generate a new image with the faces swapped. You can view and download the result.

Troubleshooting
---------------
If you encounter any issues or errors while running the application, consider the following troubleshooting steps:

- Check the Docker container logs for error messages:

docker logs frontal-face-container


- Verify that the input images contain recognizable faces for the face swapping operation.

- Ensure that the Haar cascade XML file is correctly copied into the Docker container and used in the application.

- Review the application code for any errors or issues with image processing logic.

- Check the network configuration and firewall settings on your machine.

License
-------
This project is licensed under the MIT License - see the LICENSE file for details.

