from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalysis(unittest.TestCase):
    def test_sentiment_analyzer(self):
        result1 = sentiment_analyzer('I love working with Python')
        self.assertEqual(result1['label'],'SENT_POSITIVE')
        result2 = sentiment_analyzer('I hate working with Pyhton')
        self.assertEqual(result1['label'],'SENT_NEGATIVE')
        result3 = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(result3['label'],'SENT_NEUTRAL',   'verificando 3')

unittest.main()