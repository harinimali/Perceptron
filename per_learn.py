from __future__ import division

import re
from collections import defaultdict
import os
import sys
import json
import io

d = {}
s = {}
h = {}
wordstoremove = ('i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours',
                 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself',
                 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which',
                 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been',
                 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and',
                 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about',
                 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to',
                 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then',
                 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few',
                 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same',
                 'so', 'than', 'too', 'very', 'can', 'will', 'just', 'don', 'should', 'now', 's')

indir = sys.argv[1]
max_iterations = 20
weights=defaultdict(int)
features= list()
Class= ["spam","ham"]

def maindict(l):
    for word in l:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1



def cleaning(word):
    word = word.lower()
    if (len(word) < 2):
        return None

    elif (word in wordstoremove):
        return None

    return word

def convertolist(text):
    clean_words = map(cleaning, re.split('\W+', text.strip()))
    return filter(lambda word: word and (len(word) > 0), clean_words)





def writeoutput(mod):
    with open('nbmodel.txt','w+') as fp:
        json.dump(mod, fp)

def perceptrontrain(indir):


    for root, dirs, filenames in os.walk(indir):

        for f in filenames:

            if (f == ".DS_Store" or f == 'LICENSE' or f == 'README.txt'):
                print (" ")
            else:
                with open(os.path.join(root, f), 'r') as r:
                    book = r.read()
                    word = convertolist(book)
                    maindict(word)
                    # for w in d:
                    # vocab.append(w)
                    # t= len(vocab)
                    # answerKey.append(word)
                    # h= len(answerKey)

                #w = [0 for x in range(flen)]
                b = 0


                for i in range(max_iterations):

                    # for keyh in d:

                    for t in range(len(f)):

                        a = 0
                        for word in d.keys():
                            a += d.keys() * weights[k]

                        a = a + b

                        if f.find("ham") == -1:

                            y = 1

                        elif f.find("spam") == -1:
                            y = -1

                        if ((y * a)  <= 0):
                            for k in d.keys():
                                weights[k] += (y * d.keys())
                            b += y
    print weights
    print b
                # x=sum(d.values())

    #print len(d)

    #print counts
    #print counth

    #print d[features[0]]
    #print len(w)


                #print w





def main():
    perceptrontrain(sys.argv[1])


if __name__ == '__main__':
    main()


#print answerKey

#print vocab


