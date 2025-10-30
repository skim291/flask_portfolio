from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Vercel 프론트엔드만 허용
CORS(app, origins=["https://your-portfolio.vercel.app"])

@app.route('/')
def home():
    return jsonify({"message": "Backend API is running."})

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")
    
    print(f"New contact from {name} ({email}): {message}")
    
    return jsonify({"status": "success", "message": "Form submitted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
