from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Testcase for emotion 'joy',
        # input statement 'I am glad this happened'
        result1 = emotion_detector('I am glad this happened')
        self.assertEqual(result1['dominant_emotion'], 'joy')

        # Testcase for emotion 'anger',
        # input statement 'I am really mad about this'
        result2 = emotion_detector('I am really mad about this')
        self.assertEqual(result2['dominant_emotion'], 'anger')

        # Testcase for emotion 'disgust',
        # input statement 'I feel disgusted just hearing about this'
        result3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result3['dominant_emotion'], 'disgust')

        # Testcase for emotion 'sadness',
        # input statement 'I am so sad about this'
        result4 = emotion_detector('I am so sad about this')
        self.assertEqual(result4['dominant_emotion'], 'sadness')

        # Testcase for emotion 'fear',
        # input statement 'I am really afraid that this will happen'
        result5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result5['dominant_emotion'], 'fear')

if __name__ == "__main__":
    unittest.main()