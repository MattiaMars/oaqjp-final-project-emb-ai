
def emotion_detector(text_to_analyse):
    import requests
    # Define the inputs
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    input_json = {
        "raw_document": { "text": text_to_analyse}
        }
    # Send the POST request
    response = requests.post(url, json=input_json, headers=headers)
    if response.status_code != 200:
        print('INVALID server response')
        out =''
    else:
        text=response.json()
        import json
        #dic=json.load(text)
        emotions=text["emotionPredictions"][0]['emotion']
        anger_score=emotions["anger"]
        disgust_score=emotions["disgust"]
        fear_score=emotions["fear"]
        joy_score=emotions["joy"]
        sadness_score=emotions["sadness"]
        max_key = max(emotions, key=emotions.get)
        out =        {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': max_key  }
    return out
