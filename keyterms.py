from nltk.tokenize import word_tokenize
from lxml import etree
from collections import Counter

xml = "news.xml"
root = etree.parse(xml).getroot()
result = ""
for j in range(0, len(root[0])):
    for i in root[0][j]:
        result = ""
        if i.get('name') == 'head':
            print(f"{i.text}:")
        if i.get('name') == 'text':
            sentence = i.text
            sentence = word_tokenize(sentence.lower())
            sentence = sorted(sentence, reverse=True)
            frequent = Counter(sentence)
            frequent = frequent.most_common(5)
            for word in frequent:
                result += word[0] + " "
            print(result[:-1])