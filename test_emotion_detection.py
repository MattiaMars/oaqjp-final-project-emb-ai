from EmotionDetection import emotion_detector
import unittest

class TestEmoDetector(unittest.TestCase):

    def test_emotion_1(self):
        result=emotion_detector("I am glad this happened")
        expected_result = 'joy'
        self.assertEqual(result['dominant_emotion'], expected_result)

    def test_emotion_2(self):
        result=emotion_detector("I am really mad at this")
        expected_result = 'anger'
        self.assertEqual(result['dominant_emotion'], expected_result)

    def test_emotion_3(self):
        result=emotion_detector("I am so sad about this")
        expected_result = 'sadness'
        self.assertEqual(result['dominant_emotion'], expected_result)

    def test_emotion_4(self):
        result=emotion_detector("I am really afraid that this will happen")
        expected_result = 'fear'
        self.assertEqual(result['dominant_emotion'], expected_result)

    def test_emotion_5(self):
        result=emotion_detector("I feel disgusted just hearing about this")
        expected_result = 'disgust'
        self.assertEqual(result['dominant_emotion'], expected_result)

if __name__ == '__main__':
    unittest.main()