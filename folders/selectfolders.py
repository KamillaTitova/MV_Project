from flask import *
import os


blueprint_folders = Blueprint('blueprint_folders', __name__, template_folder='templates')