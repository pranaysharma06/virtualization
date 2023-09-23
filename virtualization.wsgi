import sys
import os
from flask import Flask

# Add the directory containing your Flask application to the sys.path list
sys.path.insert(0, "/home/pranay0406/dlopsproject")

# Initialize the Flask application
app = Flask(__name__)

# Import your Flask application from the dlops.py file
from dlops import app as application
