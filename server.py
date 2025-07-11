from flask import Flask, request, render_template
from emotion_detection import emotion_detector
import json

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/emotionDetector")
def emotionDetector():
    textToAnalyze = request.args.get("textToAnalyze")
    result = emotion_detector(textToAnalyze)
    data = json.loads(result)
    response_text = 'For the given statement, the system response is '
    for key, val in data.items():
        if key != 'dominant_emotion':
            response_text += f"'{key}':{val},"
    response_text = response_text[:-1]
    response_text += f' The dominant emotion is <b>{data["dominant_emotion"]}</b>'
    return response_text
if __name__ == "__main__":
    app.run(debug=True)