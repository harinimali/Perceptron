

import re

import os
import sys
import json
import io
import math
import string
from collections import defaultdict



indir= sys.argv[1]


finaloutput=open('per_output2.txt','w+')



with open('per_model2.txt', 'r') as fp:
    data = json.load(fp)
    bias=data['bias']
    weights=data['weights']



print weights.keys()
raw_input()
#print bias



for root, dirs, files in os.walk(indir):


        for x in files:

            if (x == '.DS_Store' or x == 'LICENSE' or x == 'README.md' or x == 'README.txt'):
                print (" ")
            else:

                filename = os.path.join(root, x)
                with io.open(filename, 'r',encoding='latin1') as f:
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

