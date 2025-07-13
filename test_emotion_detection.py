import json
import unittest
import emotion_detection as EmotionDetection

test_cases = {
    "I am glad this happened": "joy",
    "I am really mad about this": "anger",
    "I feel disgusted just hearing about this": "disgust",
    "I am so sad about this": "sadness",
    "I am really afraid that this will happen": "fear",
}

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        for statement, expected in test_cases.items():
            
            output_str = EmotionDetection.emotion_detector(statement)
            output = json.loads(output_str)
            dominant_emotion = output.get("dominant_emotion")
            
            assert dominant_emotion == expected, \
                f"For statement: {statement}\\nExpected: {expected}, Got: {dominant_emotion}"

unittest.main()