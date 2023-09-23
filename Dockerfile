# Use the official Python image from Docker Hub with Python 3.9
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the Flask app files and dependencies to the container
COPY FrontalFace.py .
COPY templates/ templates/
COPY static/ static/

COPY haarcascade_frontalface_default.xml .


# Install Flask and other required Python packages
RUN pip install Flask opencv-python-headless

# Expose port 5000 (the default Flask port)
EXPOSE 5000

# Define the command to run your Flask app
CMD ["python", "FrontalFace.py"]
