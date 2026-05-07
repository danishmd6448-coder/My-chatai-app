from flask import Flask, request, jsonify
from g4f.client import Client

app = Flask(__name__)
client = Client()

@app.route('/')
def home():
    return "<h1>API is Running!</h1>"

@app.route('/v1/chat/completions', methods=['POST'])
def chat():
    try:
        data = request.json
        response = client.chat.completions.create(
            model=data.get("model", "gpt-3.5-turbo"),
            messages=data.get("messages")
        )
        return jsonify({
            "choices": [{"message": {"content": response.choices[0].message.content}}]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
  
