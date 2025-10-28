# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Netlify에서 오는 요청 허용

@app.route('/')
def home():
    return jsonify({"message": "Backend API is running."})

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")
    
    # 여기서 이메일 전송 또는 DB 저장 로직 수행 가능
    print(f"New contact from {name} ({email}): {message}")
    
    return jsonify({"status": "success", "message": "Form submitted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
