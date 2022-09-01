from flask import Flask,request, jsonify

def create_app():
    app = Flask(__name__)

    from .models import user_similarity

    @app.route('/similarity', methods=['POST'])
    def index():
        return jsonify({'similarity': user_similarity(dict(request.json))})
    return app

#터미널 : set FALSK_APP=패키지 이름,  set FLASK_DEBUG=true
# ngrok config add-authtoken