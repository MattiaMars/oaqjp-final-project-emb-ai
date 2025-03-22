from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detect():
    text_to_analyze = request.args.get('textToAnalyze')
    if text_to_analyze:
        emotion=emotion_detector(text_to_analyze)  # Replace with your function
        output='For the given statement, the system response is: /n' + '"anger": ' + str(emotion["anger"]) + ' "disgust": '  + str(emotion["disgust"]) + '" fear": ' + str(emotion["fear"]) + '" joy": ' + str(emotion["joy"]) + ' "sadness": ' + str(emotion["sadness"]) + '\n\t' + '. The dominant emotion is: ' + emotion["dominant_emotion"]
         
        return output
        #return jsonify({'For the given statement, the system response is ': emotion})
    else:
        return jsonify({'error': 'No text provided'}), 400
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
