from flask import Flask

app = Flask(__name__)

from app import main_routes, crypto_routes