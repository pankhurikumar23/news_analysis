import pickle
from nltk.sentiment.util import *
from textblob import TextBlob

source_list = ["EconomicTimes", "Hindu", "HindustanTimes", "IndianExpress", "TimesOfIndia"]
REPLACE_NO_SPACE = re.compile("(\')|(\,)|(\")|(\()|(\))|(\[)|(\])")
REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\/)|(<p>)|(\\n)")
REPLACE_WITH_PERIOD = re.compile("(\;)|(\:)|(\!)|(\?)|(\-)")

def analysisTokenize():
    i = 0
    tokenized_articles = []
    for article in articles:
        token_article = tokenize.sent_tokenize(article)
        tokenized_articles.append(token_article)

    analyzer = SentimentIntensityAnalyzer()
    for article in tokenized_articles:
        i = 0
        for sentence in article:
            print(sentence)
            scores = analyzer.polarity_scores(sentence)
            for k in sorted(scores):
                print('{0}: {1}, '.format(k, scores[k]), end='')
            print()
        if i == 0:
            break

def conductAnalysis():
    for source in source_list:
        filename = "data/Ayodhya/" + source
        file = open(filename, 'rb')
        articles = pickle.load(file)
        print(source + " " + str(len(articles)))

        articles = [REPLACE_NO_SPACE.sub("", article.lower()) for article in articles]
        articles = [REPLACE_WITH_SPACE.sub(" ", article) for article in articles]
        articles = [REPLACE_WITH_PERIOD.sub(".", article) for article in articles]

        analysis = []
        count = [0, 0]
        for article in articles:
            thing = TextBlob(article)
            if thing.sentiment[0] > 0.1:
                count[0] += 1
            else:
                count[1] += 1
            analysis.append({'polarity': thing.sentiment[0], 'subjectivity': thing.sentiment[1]})
        # print(count)

        filename1 = filename + '_clean'
        file = open(filename1, 'wb')
        pickle.dump(articles, file)
        file.close()
        filename2 = filename + '_scores'
        file = open(filename2, 'wb')
        pickle.dump(analysis, file)

def displayThings():
    for source in source_list:
        filename = "/data/Ayodhya/" + source + "_clean"
        file = open(filename, 'rb')
        articles = pickle.load(file)


if __name__ == "__main__":
    conductAnalysis()

    displayThings()