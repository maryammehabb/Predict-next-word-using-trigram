from string import punctuation
from collections import Counter
import nltk
import os
from nltk import RegexpTokenizer, ngrams
from nltk.corpus import wordnet
import re
import string
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

def remove_punctuation(value):
    result = ""
    for c in value:
        # If char is not punctuation, add it to the result.
        if c not in string.punctuation:
            result += c
    return result

file=open('C:\/Users\Mariam\Desktop\data.txt','r')
f = file.read()
sentence = nltk.sent_tokenize(f)
print(sentence)
words = []
words2 = []
for i in sentence:
    #word = nltk.word_tokenize(i)
    word = re.sub(r'\d+', '', i)
    words.append(word)
print(word)
print("mariamm")
print(words)
print(words2)
withoutpunc = []
for i in range(len(words)):
    x = remove_punctuation(words[i])
    print(x)
    withoutpunc.append(x)
print(withoutpunc)
for i in withoutpunc:
    word = nltk.word_tokenize(i)
    words2.append(word)
print("hnaaaaaaaaaaaaa", words2)

onelist = []
for x in words2:
    for y in x:
        onelist.append(y)
print("onelist  ",onelist)
'''
bigrams= ngrams(words2, 2)
trigrams=ngrams(words2,3)
for i in trigrams:
    print(trigrams,"trrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")'''
new_trigrams = []
newbri = []
c = 0
cc = 0

while cc < len(onelist) - 1:
    newbri.append((onelist[cc], onelist[cc+1]))
    cc += 1
print(newbri)

while c < len(onelist) - 2:
    new_trigrams.append((onelist[c], onelist[c+1], onelist[c+2]))
    c += 2
print(new_trigrams)

trigram = Counter(new_trigrams)
print("tttttttttttttttttt",trigram)
countwords = Counter(onelist)
print(countwords)

ff = len(onelist)
print(ff)
