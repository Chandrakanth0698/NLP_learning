from nltk.sentiment import SentimentIntensityAnalyzer


def sentimental_test(word):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(word)
    return scores
