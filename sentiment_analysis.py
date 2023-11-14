from nltk.sentiment import SentimentIntensityAnalyzer
import nltk



def sentimental_test(word):
    nltk.download('vader_lexicon')
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(word)
    return scores
