#Flask1
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/reverse', methods=['POST'])
def reverse():
    req_data = request.get_json()
    word = req_data['message']
    output = word[::-1]
    return jsonify({ "message" : output })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)



