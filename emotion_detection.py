import requests
import json

def emotion_detector(text_to_analyze):
    resp = requests.post('https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict',
        data=json.dumps({ "raw_document": { "text": text_to_analyze }}),
        headers= {"Content-Type": "application/json","grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"})
    result = json.loads(resp.text)
    emotions = result['emotionPredictions'][0]['emotion']

    dominant_emotion = ''
    dominant_emotion_score = 0
    for key, val in emotions.items():
        if val > dominant_emotion_score:
            dominant_emotion_score = val
            dominant_emotion = key
    emotions['dominant_emotion'] = dominant_emotion
    return json.dumps(emotions, indent=2)
print(emotion_detector("I love this new technology."))
