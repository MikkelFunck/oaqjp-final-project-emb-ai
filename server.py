''' Executing this function initiates the application of emotion detection analysis 
    to be executed over the Flask channel and deployed on localhost:5000. '''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def em_detector():
    ''' Receives text from the HTML interface and runs 
    emotion detection analysis using emotion_detector(). '''
    text_to_analyze = request.args.get('textToAnalyze') # retrieve

    response = emotion_detector(text_to_analyze) # pass on to function
    if response['dominant_emotion'] == 'None':
        return 'Invalid text! Please try again'

    # extract and create output
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dom_emo = response['dominant_emotion']
    output = f"For the given statement, the system response is " \
             f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} " \
             f"and 'sadness': {sadness}. The dominant emotion is {dom_emo}."

    return output

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
