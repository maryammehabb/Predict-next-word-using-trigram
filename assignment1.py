from string import punctuation
import nltk
import re


file=open('data.txt',encoding="utf8")
f = file.read()


def removepunc(text):
    result = ""
    for i in text:
        if i not in punctuation:
            result += i
    return result


words = []
words2 = []
withoutpunc = []
onelist = []
trigrams = []
threedic, dictionary = {}, {}
sentence = nltk.sent_tokenize(f)
#print("Sentences: ", sentence)

for i in sentence:
    word = re.sub(r'\d+', '', i)
    words.append(word)
#print("Words without numbers: ", word)

for i in range(len(words)):
    x = removepunc(words[i])
    withoutpunc.append(x)
print("Words without punctuation: ")
print(withoutpunc)

for i in withoutpunc:
    word = nltk.word_tokenize(i)
    words2.append(word)
#print("Words: ", words2)

for x in words2:
    for y in x:
        onelist.append(y)
#print("onelist : ",onelist)
print(len(onelist))


def trigam():
    length=0
    for i in range(len(onelist)):
        if length < i - 2:
            trigrams.append((onelist[length], onelist[length+1], onelist[length+2]))
            length += 2
    #print("Trigram: ", len(trigrams))
    #print(trigrams)
    return trigrams


def frequency(trigrams):
    count = 0
    for (x, y, z) in trigrams:
        if (x, y, z) in threedic:
            threedic[(x, y, z)] += 1
            count += 1
        else:
            threedic[(x, y, z)] = 1
            count += 1
        dictionary[(x, y, z)] = threedic[(x, y, z)]/count
    #print("three : ", threedic, len(threedic))
    #print(dictionary)
    #print(count)
    return dictionary


def test(x, y, dictionary):
    thirdword = ""
    p = -1
    for (a, b, c) in dictionary:
        if a != x or b != y:
            continue
        if dictionary[(a, b, c)] > p:
            p = dictionary[(a, b, c)]
            thirdword = c
    print(x, y, thirdword)
    print(p)


t = trigam()
f = frequency(t)
test("التعليم",  "المرئي", f)

