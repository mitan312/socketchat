from flask import Flask, render_template
from flask_socketio import SocketIO, send
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print(f"📩 Nhận tin nhắn: {msg}")
    send(msg, broadcast=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"✅ Server đang chạy tại http://localhost:{port}")
    socketio.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)
    import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, host="0.0.0.0", port=port, debug=False)
