from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')


def sentimental_test(word):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(word)
    return scores
