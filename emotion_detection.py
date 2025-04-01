'''
Create function to perform emotion detection on text.
Implementing Watson NLP Emotion Predict.
'''
import json
import requests

def emotion_detector(text_to_analyse):
    '''
    Emotion detection function. argument is text for analysis
    '''
    # URL for Watson NLP API
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # headers for API
    API_headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Input as json
    input_json = { "raw_document": { "text": text_to_analyse } }
    # POST request to the API 
    response = requests.post(URL, json = input_json, headers=API_headers)
    # return text attribute from response object as noted in step 3.
    return response.text