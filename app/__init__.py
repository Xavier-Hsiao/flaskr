from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# the routes module needs to import the app variable defined in this script
from app import routes;