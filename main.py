from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import chatbot


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
@cross_origin()
def index():
    resp = {
        'status': 'success',
    }
    return jsonify(resp)

@app.route('/msg', methods=['POST'])
@cross_origin()
def msg():
    resp = chatbot.predict_msg(request.json['msg'])
    return jsonify(resp)

if __name__ == '__main__':
    app.run(debug=True)