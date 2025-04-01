''' Create function to perform emotion detection on text. Implementing Watson NLP Emotion Predict. '''
import json
import requests

def emotion_detector(text_to_analyse):
    ''' Emotion detection function. argument is text for analysis'''
    # URL for Watson NLP API
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # headers for API
    API_headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Input as json
    input_json = { "raw_document": { "text": text_to_analyse } }
    # POST request to the API 
    response = requests.post(URL, json = input_json, headers=API_headers)
    # return text attribute from response as json 
    response_json = json.loads(response.text)
    if response.status_code == 400:
        task3_output = {} 
        task3_output['anger'] = 'None' 
        task3_output['disgust'] = 'None' 
        task3_output['fear'] = 'None' 
        task3_output['joy'] = 'None' 
        task3_output['sadness'] = 'None' 
        task3_output['dominant_emotion'] = 'None' 
        return task3_output        
    else:
        emotions = response_json['emotionPredictions'][0]['emotion']
        # retrieve dominant emotion
        dominant_emotion = max(emotions, key=emotions.get) 
        # create ouput
        task3_output = {} 
        task3_output['anger'] = emotions['anger'] 
        task3_output['disgust'] = emotions['disgust']
        task3_output['fear'] = emotions['fear']
        task3_output['joy'] = emotions['joy']
        task3_output['sadness'] = emotions['sadness']
        task3_output['dominant_emotion'] = dominant_emotion
        return task3_output