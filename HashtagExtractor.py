import os.path
from nltk.tokenize import sent_tokenize #punkt needed
from nltk.corpus import stopwords #stopwords needed
from collections import defaultdict

top_n = 5
data = defaultdict(list)

class Hashtag:
    def __init__(self, filename, word, phrase ):
        self.filename = filename
        self.word = word
        self.phrase = phrase


def add_tokens_to_list(sentence, filename):
    tokens = sentence.lower().split()
    filtered_tokens = [i for i in tokens if i not in stopwords.words('english')]
    for filtered_token in filtered_tokens:
        hashtag = Hashtag(filename, filtered_token, sentence)
        data[filtered_token].append(hashtag)


def get_hastags(path, file):
    filepath = os.path.normpath(path + file)
    with open(filepath) as f:
        text = f.read()
        sent_tokenize_list = sent_tokenize(text)
        for sent in sent_tokenize_list:
            add_tokens_to_list(sent, file)

get_hastags('c:/Users/Alessandra/Downloads/eigen/test docs/', 'doc1.txt')

oog = data['battle']
for oo in oog:
    print(oo.phrase)

for key, value in data.items():
    if len(data[key]) > 5:
        print(key)
        # for each bla in data[key]
            # save bla.word, bla.filename, b.phrase