from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing text input'}), 400
    
    text_to_analyze = data['text']
    result = emotion_detector(text_to_analyze)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
