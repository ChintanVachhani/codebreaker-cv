from flask import Flask

application = Flask(__name__)

from app import routes

if __name__ == '__main__':
    application.run(host='0.0.0.0')
