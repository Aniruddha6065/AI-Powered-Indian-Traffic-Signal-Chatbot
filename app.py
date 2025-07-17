from flask import Flask, render_template, request, jsonify
from ai_logic import get_bot_response

app = Flask(__name__)
app.secret_key = 'trafficbot_secret_key'  # Needed for session

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/chat')
def chat():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_api():
    user_message = request.json.get('message', '')
    bot_response = get_bot_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True) 