import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } } 
    response = requests.post(url, json = myobj, headers=header)
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        list_emotion  = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(list_emotion, key = list_emotion.get)
    elif response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        list_emotion  = None
        dominant_emotion = None
    else:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        list_emotion  = None
        dominant_emotion = None
    return {'anger': anger, 'disgust': disgust,'fear' : fear, 'joy' : joy, 'sadness' : sadness, 'dominant_emotion' : dominant_emotion}