from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

# GET /sse 엔드포인트
@app.route('/sse', methods=['GET'])
def sse():
    session_id = request.args.get('sessionId', 'unknown')
    return jsonify({
        "jsonrpc": "2.0",
        "id": "1",
        "method": "sse",
        "params": {
            "sessionId": session_id
        },
        "result": {
            "message": "SSE Connected"
        },
        "error": None
    })

# POST /query 엔드포인트
@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    return jsonify({
        "jsonrpc": "2.0",
        "id": "2",
        "method": "query",
        "params": data,
        "result": {
            "message": "Query Received",
            "received": data
        },
        "error": None
    })

# POST /invoke 엔드포인트
@app.route('/invoke', methods=['POST'])
def invoke():
    data = request.get_json()
    return jsonify({
        "jsonrpc": "2.0",
        "id": "3",
        "method": "invoke",
        "params": data,
        "result": {
            "message": "Invoke Completed",
            "received": data
        },
        "error": None
    })
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
