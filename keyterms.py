import string
from collections import Counter
import pandas as pd
import nltk
from nltk.tag.perceptron import PerceptronTagger
from lxml import etree
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

root = etree.parse("news.xml").getroot()
headlines = []
lemmatizer = WordNetLemmatizer()
stop_words = stopwords.words('english') + list(string.punctuation)
vectorizer = TfidfVectorizer()
vocabulary = []
i = 0
list_to_print = []
for news in root[0]:
    headlines.append(f"{news[0].text}:")
    counts = Counter()
    text = ""
    for word in word_tokenize(news[1].text.lower()):
        word = lemmatizer.lemmatize(word)
        if word not in string.punctuation and word not in stopwords.words("english"):
            if nltk.pos_tag([word])[0][1] == 'NN':
                counts.update([word])
                text += word + " "
    vocabulary.append(text)
    i += 1
    counts_sorted = sorted(counts.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
tfidf_matrix = vectorizer.fit_transform(vocabulary)
terms = vectorizer.get_feature_names_out()
for i in range(len(headlines)):
    print(headlines[i])
    df = pd.DataFrame(tfidf_matrix[i].T.todense(), index=terms, columns=["tfidf"])
    df.index.name = 'word'
    df = df.sort_values(['tfidf', 'word'], ascending=[False, False]).head(5)
    print(' '.join(list(df.index)), '\n')