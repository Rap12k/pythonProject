# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#basic text analysis

import pandas as pd
import matplotlib.pyplot as plt
import spacy
import en_core_web_sm
from collections import Counter
from spacy.matcher import Matcher


nlp = en_core_web_sm.load()
nlp.max_length = 1850000


def read_csv():
    data = pd.read_excel('/Users/robertpitter/Desktop/20191226-reviews-e.xls')
    data.drop(['asin','name','rating','date','verified','body','helpfulVotes'], axis=1, inplace=True)
    #print(data.head())
    all_text = data['title'].str.cat(sep=' ')
    doc = nlp(all_text, disable=['ner'])

    words = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    word_freq = Counter(words)
    print(word_freq.most_common(30))

    matcher = Matcher(nlp.vocab)
    pattern = [{'POS': 'ADJ'}, {'POS': 'NOUN'}]
    matcher.add('ADJ_PHRASE', [pattern])
    matches = matcher(doc, as_spans=True)
    phrases = []
    for span in matches:
        phrases.append(span.text.lower())
        phrase_freq = Counter(phrases)
    print(phrase_freq.most_common(30))
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
