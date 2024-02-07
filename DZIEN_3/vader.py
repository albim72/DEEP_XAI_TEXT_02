from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

sentence = "To jest świetny dzień!"
sentence2 = "bardzo zły dzień"
sentence3 = "very teribble day"
#analiza sentymentu
sentiment_score = analyzer.polarity_scores(sentence)

print(f'tekst: {sentence3}')
print(f'wyniki analizy sentymentu: {sentiment_score}')

#interpretcja wyników
if sentiment_score['compound']>=0.0:
    print("tekst jest pozytywny")
elif sentiment_score['compound']<=-0.5:
    print("teskt jest negatywny")
else:
    print("tekst neutralny")
