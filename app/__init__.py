from flask import Flask

app = Flask(__name__)

# the routes module needs to import the app variable defined in this script
from app import routes;