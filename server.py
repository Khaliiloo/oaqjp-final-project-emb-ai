"""
The flask main server
"""
import json
from flask import Flask, request, render_template
import emotion_detection
app = Flask(__name__)

@app.get("/")
def index():
    """
        home route
    """
    return render_template("index.html")

@app.get("/emotion_detector_api")
def emotion_detector_api():
    """
        Route of call emotion_detector and get text analysis
    """
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detection.emotion_detector(text_to_analyze)
    data = json.loads(result)
    
    if data['dominant_emotion'] is None:
        return '<b>Invalid text! Please try again!</b>'

    response_text = 'For the given statement, the system response is '
    for key, val in data.items():
        if key != 'dominant_emotion':
            response_text += f"'{key}':{val},"
    response_text = response_text[:-1]
    response_text += f' The dominant emotion is <b>{data["dominant_emotion"]}</b>'
    return response_text
if __name__ == "__main__":
    app.run(debug=True)
