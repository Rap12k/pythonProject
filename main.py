# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# basic text analysis

import pandas as pd
import pprint
import matplotlib.pyplot as plt
import spacy
import en_core_web_sm
from collections import Counter
from spacy.matcher import Matcher

nlp = en_core_web_sm.load()
nlp.max_length = 1850000


def read_csv():
    data = pd.read_excel('/Users/robertpitter/Desktop/20191226-reviews-e.xls')
    data.drop(['asin', 'name', 'rating', 'date', 'verified', 'body', 'helpfulVotes'], axis=1, inplace=True)
    unique_phone = data['Phone'].unique()
    # print(unique_phone)

    phone_data = {}
    # print(unique_phone)
    # print(len(unique_phone))
    for phone in unique_phone:
        phone_data[phone] = data[data['Phone'] == phone]['title']

    samplePhone = 'Apple MGLW2LL/A iPad Air 2 9.7-Inch Retina Display, 16GB, Wi-Fi (Silver) (Renewed)'
    # print(phone_data[samplePhone])

    all_text = phone_data[samplePhone].str.cat(sep=' ')
    doc = nlp(all_text, disable=['ner'])
    words = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    word_freq = Counter(words)
    #print(samplePhone, word_freq.most_common(5))

    matcher = Matcher(nlp.vocab)
    pattern = [{'POS': 'ADJ'}]  # , {'POS': 'NOUN'}]
    matcher.add('ADJ', [pattern])
    matches = matcher(doc, as_spans=True)
    adj = []
    for span in matches:
        adj.append(span.text.lower())
        phrase_freq = Counter(adj)
    #print(samplePhone, phrase_freq.most_common(5))

    reviewsphrase = {}
    reviewscount = {}

    for phone in phone_data:
        all_text = phone_data[phone].str.cat(sep = ' ')
        doc = nlp(all_text, disable=['ner'])
        words = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
        word_freq = Counter(words)
        reviewscount[phone] = (word_freq.most_common(5))

    for phone in phone_data:
        all_text = phone_data[phone].str.cat(sep=' ')
        doc = nlp(all_text, disable=['ner'])
        matcher = Matcher(nlp.vocab)
        pattern = [{'POS': 'ADJ'}]  # , {'POS': 'NOUN'}]
        matcher.add('ADJ', [pattern])
        matches = matcher(doc, as_spans=True)
        adj = []
        for span in matches:
            adj.append(span.text.lower())
            phrase_freq = Counter(adj)
        reviewsphrase[phone] = (phrase_freq.most_common(5))

    #print("Word Count")
    #pprint.pprint((reviewscount))
    print("Review Adjective Count")
    pprint.pprint((reviewsphrase))

    '''
    basic text analysis in python
    can get the most common words used in a column from excel
    can also use the pattern match to find the most common phrases with adjectives
    tutorial followed: https://robertorocha.info/using-nlp-to-analyze-open-ended-responses-in-surveys/
    '''


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_csv()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
