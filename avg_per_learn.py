from __future__ import division
import os
import sys
import json
import io
import operator
import random
from collections import defaultdict



finalDict={}


def writeoutput(mod):
    with open('avg_per_model.txt','w+') as fp:
        json.dump(mod, fp)



weights = defaultdict(int)
avgweights=defaultdict(int)

ag1=0
def avg_perceptrontrain(indir):
    b = 0
    beta=0
    counter=1
    flist=[]
    for root, dirs, files in os.walk(indir):
        for x in files:
            if (x == '.DS_Store' or x == 'LICENSE' or x == 'README.md' or x == '__MACOSX'):
                print (" ")
            else:
                filename = os.path.join(root, x)
                flist.append(filename)




    for t in range(0, 30):
        random.shuffle(flist)
        for q in flist:

            with io.open(q, 'r', encoding='latin1') as f:
                fdata = f.read()

                fdata = fdata.lower()

                fdata = fdata.split()

                a=0

                for word in fdata:
                    a += weights[word]
                a = a + b



                if 'spam' in q:
                    y = 1
                else:
                    y = -1


                if ((y * a) < 1):
                    b= b + y
                    beta=beta+(y*counter)
                    for w in fdata:
                        weights[w] += y
                        avgweights[w] += (y*counter)


                counter +=  1
    #ag1=(1/counter)
    #print counter


    for w in fdata:

        avgweights[w] = weights[w]  - ((1.0/counter)* avgweights[w])

    beta= b - ((1.0/counter)*beta)








    print avgweights
    print beta
    print counter


    finalDict['weights'] = avgweights
    finalDict['bias'] = beta

    return finalDict


def main():
    we=avg_perceptrontrain(sys.argv[1])
    writeoutput(we)




if __name__ == '__main__':
    main()

