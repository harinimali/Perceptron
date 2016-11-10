
from __future__ import division
import re

import os
import sys
import json
import io
import math
import string
from collections import defaultdict



indir= sys.argv[1]




finaloutput=open('avg_per_output2.txt','w+')



with open('avg_per_model2.txt', 'r') as fp:
    data = json.load(fp)
    bias=data['bias']
    weights=data['weights']



def calculations(filecount):
    hprecision = 0.0
    hrecall = 0.0
    hf1 = 0.0
    sprecision = 0.0
    srecall = 0.0
    sf1 = 0.0

    with open(indir2, 'r') as fp:
        data = fp.readlines()

    a1 = 0.0
    b1 = 0.0
    c1 = 0.0
    a2 = 0.0
    b2 = 0.0
    c2 = 0.0
    accuracy = 0.0

    for d in data:
        d = d.strip('\n').split(' ')


        #print d[-1]

        if (d[0] == 'HAM') and (re.search('ham', d[-1])):
            a1 += 1

        elif(d[0] == 'HAM') and (re.search('spam', d[-1])):
            b1 += 1
        elif (d[0] == 'SPAM') and (re.search('ham', d[-1])):
            c1 += 1

        if (d[0] == 'SPAM') and (re.search('spam', d[-1])):
            a2 += 1
        elif (d[0] == 'SPAM') and (re.search('ham', d[-1])):
            b2 += 1
        elif (d[0] == 'HAM') and (re.search('spam', d[-1])):
            c2 += 1
    # print a1
    # print a2

    if filecount != 0:
        accuracy = float(a1 + a2) / float(filecount)
    else:
        accuracy = 0

    if (a1 + b1):
        hprecision = float(a1) / float(a1 + b1)
    else:
        hprecision = 0
    if (a1 + c1):

        hrecall = float(a1) / float(a1 + c1)
    else:
        hrecall = 0

    if (a2 + b2):
        sprecision = float(a2) / float(a2 + b2)
    else:
        sprecision = 0
    if (a2 + c2):

        srecall = float(a2) / float(a2 + c2)
    else:
        srecall = 0
    if (hprecision + hrecall):
        hf1 = float((2 * hprecision * hrecall) / float(hprecision + hrecall))
    else:
        hf1 = 0

    if (sprecision + srecall):
        sf1 = float(2 * sprecision * srecall) / (sprecision + srecall)
    else:
        sf1 = 0

    print ("Ham precision:", hprecision)
    print ("Ham recall:", hrecall)
    print ("Ham F1 Score: ", hf1)
    print ("Spam precision:", sprecision)
    print ("Spam recall:", srecall)
    print ("Spam F1:", sf1)
    print ("Accurcy:", accuracy)
#print bias

con=0

for root, dirs, files in os.walk(indir):


        for x in files:

            if (x == '.DS_Store' or x == 'LICENSE' or x == 'README.md' or x == 'README.txt'):
                print (" ")
            else:

                filename = os.path.join(root, x)

                with io.open(filename, 'r',encoding='latin1') as f:
                    con+=1
                    contents = f.read()
                    contents = contents.lower()

                    contents = contents.split()
                    a=0

                    for w in contents:
                        if w in weights.keys():

                            a += weights[w]

                    a = a + bias

                    if ( a >0 ):

                        print "spam",filename
                        finaloutput.write("SPAM ")
                    else:
                        print "ham" , filename
                        finaloutput.write("HAM ")
                    finaloutput.write(filename + "\n")



calculations(con)