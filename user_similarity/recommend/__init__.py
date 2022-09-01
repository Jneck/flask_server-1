from flask import Flask
from flask import render_template

#pip install flask-migrate
#pip install pymysql
#flask db init
#flask run --port=5001
#flask db migrate
#flask db upgrade



def create_app():
    app = Flask(__name__)

    from .models import user_similarity

    @app.route('/')
    def index():

        return user_similarity()

    return app

#터미널 : set FALSK_APP=패키지 이름,  set FLASK_DEBUG=true
# ngrok config add-authtoken