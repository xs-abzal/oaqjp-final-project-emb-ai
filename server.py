''' Running server.py initiates the application of emotion detection
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
### import libraries
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def sent_to_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection analysis over it using emotion_detector()
        function. The output returned as a text.
    '''
    ### get user input
    text_to_analyze = request.args.get('textToAnalyze')
    ### apply emotion_detector() to get dictionary reponse
    response_dict = emotion_detector(text_to_analyze)
    anger_score = response_dict['anger']
    disgust_score = response_dict['disgust']
    fear_score = response_dict['fear']
    joy_score = response_dict['joy']
    sadness_score = response_dict['sadness']
    dominant_emotion_name = response_dict['dominant_emotion']

    ### Task7, when input is empty & 'None' is received as a response,
    ### replace response with 'special' response_text value
    if dominant_emotion_name == 'None':
        response_text = 'Invalid text! Please try again!'

    else:
        response_text = f"For the given statement, the system response is \
                        'anger': {anger_score}, 'disgust': {disgust_score}, \
                        'fear': {fear_score}, 'joy': {joy_score} and \
                        'sadness': {sadness_score}. \
                        The dominant emotion is {dominant_emotion_name}."

    return response_text

@app.route('/')
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000)
