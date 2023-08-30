import requests

def emotion_detector(text_to_analyze):
    API_URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    params = { 
        "raw_document": { 
            "text": text_to_analyze 
        } 
    }

    print(f"Getting emotion analysis for input: {text_to_analyze}")
    response =  requests.get(API_URL, headers=headers, params=params)

    return response.text


print(emotion_detector("I was very happy with the service provided today."))
