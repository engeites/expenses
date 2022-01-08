from flask import Flask
from tasks import tasks

app = Flask(__name__)
app.register_blueprint(tasks)

from app import main_routes, crypto_routes