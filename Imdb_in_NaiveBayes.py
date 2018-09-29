#P76071200 CSIE NCKU
#Chung-Yao Ma 2018/09/29

import os
import json
import numpy
import time

word_index = open("imdb_word_index.json", "r")
text = word_index.read()
json_index = json.loads(text)

x_test = numpy.load("./imdb/x_test.npy")
x_train = numpy.load("./imdb/x_train.npy")

y_test = numpy.load("./imdb/y_test.npy")
y_train = numpy.load("./imdb/y_train.npy")

positive = {}
negative = {}
pos_sum = 0
neg_sum = 0

k = 100

ts = time.time()

for i in range(len(x_train)):
    print("Comment %d : ")
    for word in x_train[i]:
        #positive
        if y_train[i] == 1:
            if word<k:
                if word not in positive:
                    positive[word] = 1
                else:
                    positive[word] += 1
                pos_sum += 1
                print("Word_list : ",word," Label :",y_train[i]," time : ",positive[word])
                print(pos_sum)  
        #negative
        else:
            if word<k:
                if word not in negative:
                    negative[word] = 1
                else:
                    negative[word] += 1
                neg_sum += 1
                print("Word_list : ",word," Label :",y_train[i]," time : ",negative[word])
                print(neg_sum)  

te = time.time()
print(te-ts)