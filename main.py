# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import matplotlib.pyplot as plt
import nltk

from nltk.sentiment.vader import SentimentIntensityAnalyzer

from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize

from nltk.stem import WordNetLemmatizer

nltk.download('all')


def preprocess_text(text):
    # Tokenize the text
    tokens = word_tokenize(text.lower())
    # Remove stop words
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    # Join the tokens back into a string
    processed_text = ' '.join(lemmatized_tokens)
    return processed_text


def read_csv():
    data = pd.read_excel('/Users/robertpitter/Desktop/20191226-reviews-e.xls')
    data.drop(['asin','name','rating','date','verified','body','helpfulVotes'], axis=1, inplace=True)
    #print(data.head())

    data['title'] = data['title'].apply(preprocess_text)
    #print(data.head())
    #print(data.isna().sum())
    data['title'].value_counts(normalize = True).plot.bar()
    plt.show(block=True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_csv()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
