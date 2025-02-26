import requests, json

def emotion_detector(text_to_analyze):
    '''
    input  ---> text_to_analyze
    return ---> reponse of 'emotion detection' using Watson NLP. return output variable as a dictionary.
    '''

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json =  {"raw_document": {"text": text_to_analyze}}

    ### send post request 
    response = requests.post(url=url, headers=headers, json=input_json)
    
    ### response in json format
    response_json = json.loads(response.text)
    
    ### access value of 'emotion' in a response dictionary
    reponse_json = response_json['emotionPredictions'][0]['emotion']
    
    ### get scores for each emotion parameter
    anger_score = reponse_json['anger']
    disgust_score = reponse_json['disgust']
    fear_score = reponse_json['fear']
    joy_score = reponse_json['joy']
    sadness_score = reponse_json['sadness']
    
    ### create 'output' dictionary
    output = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    ### define dominant emotion category/name using max() 
    ### and add it to the final 'output' dictionary
    output['dominant_emotion'] = max(output, key=output.get)
    
    return output









# import requests

# def emotion_detector(text_to_analyze):
#     '''
#     input  ---> text_to_analyze
#     return ---> reponse of 'emotion detection' using Watson NLP.
#     '''

#     url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
#     headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
#     input_json =  {"raw_document": {"text": text_to_analyze}}

#     ### send post request 
#     response = requests.post(url=url, headers=headers, json=input_json)
    
#     ### return reponse as a text   
#     return response.text