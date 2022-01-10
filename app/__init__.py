from flask import Flask
from tasks import expenses

app = Flask(__name__)
app.register_blueprint(expenses)

from app import main_routes, crypto_routes