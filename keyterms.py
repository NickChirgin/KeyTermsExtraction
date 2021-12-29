import string
from collections import Counter

from lxml import etree
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

root = etree.parse("news.xml").getroot()
lemmatizer = WordNetLemmatizer()

for news in root[0]:
    print(f"{news[0].text}:")
    counts = Counter()
    for word in word_tokenize(news[1].text.lower()):
        word = lemmatizer.lemmatize(word)
        if word not in string.punctuation and word not in stopwords.words("english"):
            counts.update([word])
    counts_sorted = sorted(counts.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    print(" ".join(x[0] for x in counts_sorted[:5]))
    print()