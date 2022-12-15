#take response and analyze it 
import nltk
word_list2 = [word for line in twitter['text'] for word in line.split()]
word_frequency = nltk.FreqDist(word_list2)
type(word_frequency)
from nltk.corpus import stopwords
print(stopwords.words('english'))
app = twitter['text'].apply(str.lower)
def fun_remove(line):
    x2 = line.split(' ')
    ret = ''
    for word in x2:
        if word not in stopwords.words('english'):
            ret += word + ' '
    return ret
        
rem = app.apply(fun_remove) 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
sentiment_ = rem.apply(sid.polarity_scores)
import matplotlib.pyplot as plt

fig = plt.figure(figsize = (10, 5))
 
# creating the plot
plt.pyplot.plot(sentiment_['positive'], sentiment_['negative'], color ='green',
        width = 0.4)
 
plt.xlabel("Sentiment positive")
plt.ylabel("Sentiment negative")
plt.title("Bitcoin Sentiment Analysis")
plt.xticks(rotation=90)
plt.show()