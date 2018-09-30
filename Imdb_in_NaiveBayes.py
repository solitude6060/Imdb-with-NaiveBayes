#P76071200 CSIE NCKU
#Chung-Yao Ma 2018/09/29

import os
import json
import numpy
import time
import math

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

k = 10000

ts = time.time()

for i in range(len(x_train)):
    for word in x_train[i]:
        #positive
        if y_train[i] == 1 and word <=k:
            if word not in positive:
                positive[word] = 1
            else:
                positive[word] += 1
            pos_sum += 1 
        #negative
        elif y_train[i] == 0 and word<=k:
            if word not in negative:
                negative[word] = 1
            else:
                negative[word] += 1
            neg_sum += 1
#print([(k,positive[k]) for k in sorted(positive.keys())])
'''
check_pos = []
check_neg = []
for i in range(len(x_train)):
    for word in x_train[i]:
        #positive
        if y_train[i] == 1 and word <=k and word not in check_pos:
            if word not in positive :
                positive[word] = 1
                check_pos.append(word)
            else:
                positive[word] += 1
                check_pos.append(word)
            pos_sum += 1 
        #negative
        elif y_train[i] == 0 and word<=k and word not in check_neg:
            if word not in negative:
                negative[word] = 1
                check_neg.append(word)
            else:
                negative[word] += 1
                check_neg.append(word)
            neg_sum += 1
    check_pos = []
    check_neg = []
'''
te = time.time()
print(te-ts)

print("length of positive : %d" %(len(positive)))
#print("positive : ", positive)
print("length of negative : %d" %(len(negative)))
#print("negative : ", negative)

prior_pos = 0
prior_neg = 0
for key, value in positive.items():
    positive[key] = value/pos_sum
    prior_pos = value/pos_sum

for key, value in negative.items():
    negative[key] = value/neg_sum
    prior_neg = value/neg_sum

result = []
pos_logpb = 0
neg_logpb = 0

total = []
for i in range(1,k+1):
    #print(i)
    if i not in positive:
        positive[i] = 1/1000000000000000
    if i not in negative:
        negative[i] = 1/1000000000000000
    total.append(positive[i] + negative[i])
print(len(total))
'''
for comment in range(len(x_test)):
    for word in x_test[comment]:
        if word<=k and word in positive:
            pos_logpb += math.log10(positive[word])
            pos_logpb -= math.log10(total[word-1])
        if word<=k and word in negative:
            neg_logpb += math.log10(negative[word])
            neg_logpb -= math.log10(total[word-1])
    if pos_logpb+math.log10(prior_pos) >= neg_logpb+math.log10(prior_neg):
        result.append(1)
    else:
        result.append(0)
    pos_logpb = 0
    neg_logpb = 0
'''
check_test_pos = []
check_test_neg = []
for comment in range(len(x_test)):
    for word in x_test[comment]:
        if word<=k and word in positive and word not in check_test_pos:
            pos_logpb += math.log10(positive[word])
            pos_logpb -= math.log10(total[word-1])
            check_test_pos.append(word)
        if word<=k and word in negative and word not in check_test_neg:
            neg_logpb += math.log10(negative[word])
            neg_logpb -= math.log10(total[word-1])
            check_test_neg.append(word)
    if pos_logpb+math.log10(prior_pos) >= neg_logpb+math.log10(prior_neg):
        result.append(1)
    else:
        result.append(0)
    pos_logpb = 0
    neg_logpb = 0
    check_test_pos = []
    check_test_neg = []

print(len(result))

correct = 0
for i in range(len(y_test)):
    if y_test[i] == result[i]:
        correct += 1
accu = correct/25000
print(correct)
print(accu)
