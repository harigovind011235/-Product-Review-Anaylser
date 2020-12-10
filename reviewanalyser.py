from textblob import *
from newspaper import *
import nltk,os,ssl


if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

# url ="https://indianexpress.com/article/cities/delhi/rape-by-hiv-positive-man-not-attempt-to-murder-delhi-high-court-7097322/"
#
# article = Article(url)
#
# article.download()
# article.parse()
# article.nlp()
#
# # nltk.download()
#
# text = article.summary
# blob = TextBlob(text)
#
# senti = blob.sentiment.polarity
#
# print(senti)



url ="http://newsonair.com/Main-News-Details.aspx?id=405811"

article = Article(url)

article.download()
article.parse()
article.nlp()

# nltk.download()

text = article.summary
blob = TextBlob(text)

senti = blob.sentiment.polarity

print(senti)
