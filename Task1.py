import nltk
import os

from nltk import RegexpTokenizer
from nltk.corpus import wordnet
import re
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer

#nltk.download('wordnet')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('punkt')

file=open('labtask1.txt','r')
f = file.read();
token2 = nltk.sent_tokenize(f)
print(token2)
token3=[]
for i in token2:
    token = nltk.word_tokenize(i)
    token = re.split('[-_,.\s ]', f)
    token3.append(token)
print (token3)
words = re.split('[-_,.\s ]', f)
print(words)
count=[]
for w in words:
    count.append(words.count(w))
print(count)

porter_stemmer = PorterStemmer()
stems=[]
for w in range(len(token3)):
    for j in range(len(token3[w])):
        stem = porter_stemmer.stem(token3[w][j])
        stems.append(stem)
print(stems)
count1=[]
for w in stems:
    count1.append(stems.count(w))
print(count1)

