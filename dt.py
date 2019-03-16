'''import nltk
from nltk import word_tokenize
from nltk.util import ngrams


text = "Hi How are you? i am fine and you"
token=nltk.word_tokenize(text)
bigrams=ngrams(token,2)
trigrams=ngrams(token,3)
new_trigrams = []
c = 2
print(token)
while c < len(token) - 2:
    new_trigrams.append((token[c], token[c+1], token[c+2]))
    c += 2
    print(new_trigrams)'''
import collections

# To download the needed libraries:
import nltk



# coding=utf-8

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def bigrams(base, words):
    bigrams = []
    suggestions = []
    print(len(base))
    print(len(words))
    for i in range(0, len(base)):
        if (i == len(base) - 1):
            break
        else:
            if (base[i].lower() == words[1].lower() and base[i - 1].lower() == words[0].lower()):
                print(base[i],"mariammm")
                bigrams.append(base[i + 1])

    counter = collections.Counter(bigrams)

    for i in range(0, len(counter.most_common())):
        if (i >= 3):
            break
        else:
            suggestions.append(counter.most_common()[i][0])

    return suggestions


def trigrams(base, words):
    trigrams = []
    suggestions = []

    for i in range(0, len(base)):
        if (i == len(base) - 2):
            break
        else:
            if (base[i].lower() == words[2].lower()
                    and base[i - 1].lower() == words[1].lower()
                    and base[i - 2].lower() == words[0].lower()):
                trigrams.append(base[i + 1])

    counter = collections.Counter(trigrams)

    for i in range(0, len(counter.most_common())):
        if (i >= 3):
            break
        else:
            suggestions.append(counter.most_common()[i][0])

    return suggestions


#with open('C:\/Users\Mariam\Downloads\/bigram-trigram-python-master\shakespeare.txt', 'r') as myfile:
with open('C:\/Users\Mariam\Desktop\data.txt', 'r') as myfile:

    data = myfile.read().replace('\n', ' ')
txtfiltered = [w for w in word_tokenize(data.replace(',', ' ').replace('.', ' '))]

print(bigrams(txtfiltered, ['I', 'want']))

print(trigrams(txtfiltered, ['reserve', 'a', 'table']))