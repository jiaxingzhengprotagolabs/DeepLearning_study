#!/usr/bin/python
#coding=utf-8

import numpy as np
import pandas as pd
import shutil

## retrieve data: samples from the language library after calculation of the model
## fake data format:  document_id     relevance_score     question        answering         label
### pada1， 2， 3分别代表不同的问句得到的返回数据

pada1 = pd.read_csv('test1.txt', sep='\t')
pada2 = pd.read_csv('test2.txt', sep='\t')
pada3 = pd.read_csv('test3.txt', sep='\t')
raters = pd.read_csv('raters.txt', sep='\t')
## dicts is the sample data of this test script
dicts = []
## 假设我们有三个问句，分别得到三个结果集，拼接到一起构成dicts，也就是sample data
dicts = [pada1, pada2, pada3]

## calculate label for dicts

## calculate for precision@1
sum = 0
### precision@1
for q in dicts:
    sum += q["label"][0]
   
precision1 = sum / len(dicts)



### using the raters to give the dicts initialization of labels
def labeled(dicts, raters):
    tmp = dicts
    rater = raters.values.tolist()
    if tmp == None:
        print("Please load your test set!")
        return 0
    lens = 0
    if len(tmp) != len(raters):
        lens = len(tmp)
    else:
        lens = len(raters)
    
    for i in range(lens):
        for j in range(len(tmp[i]['answer'])):
            if tmp[i]['answer'][j] == rater[i][1]:
                tmp[i]['label'][j] = 1
                continue
            elif tmp[i]['answer'][j] == rater[i][2]:
                tmp[i]['label'][j] = 1
                continue
            elif tmp[i]['answer'][j] == rater[i][3]:
                tmp[i]['label'][j] = 1
                continue  
            else:
                tmp[i]['label'][j] = 0
    return tmp, rater

dicts, raters = labeled(dicts, raters)


### precision@k  k from 1 to n: represent the rank order
def precision(dicts, k):
    if dicts == None:
        print("Please load your test set!")
        return 0
    if k <= 0 or k > len(dicts):
        print("please input a valid value for k, which is from 1  to" + len(dicts))
        return 0
    
    sum = 0
    ## 对于sample中每一个rank为k的问答句pair precision@k = sum / sample中所有rank为k的问句总数
    for q in dicts:
        sum += q["label"][k-1]
    res = sum / len(dicts)
    return res



## MAP value
def mAP(dicts, k):
    
    if dicts == None:
        print("Please load your test set!")
        return 0
    if k <= 0 or k > len(dicts):
        print("please input a valid value for k, which is from 1  to" + len(dicts))
        return 0
    
    sum1 = 0
    for q in dicts:
        sum2 = 0
        Nq = 0
        for i in range(k):
            sum2 += precision(dicts, i+1) * (precision(dicts, i+1) * len(dicts))
        for j in range(len(q)):
            Nq += q["label"][j]

        if Nq == 0:
        	sum1 += 0
        else:
        	sum1 += sum2 / Nq

    return sum1 / len(dicts)

## rank(i) ???
def rank(q):
    return 1

## MRR
def mRR(dicts):
    if dicts == None:
        print("Please load your test set!")
        return 0
    
    sum1 = 0
    for q in dicts:
        sum1 += 1 / rank(q)
    return sum1 / len(dicts)


## Z is a constant number
Z = 2.331

## nDCG
def nDCG(dicts, k):
    if dicts == None:
        print("Please load your test set!")
        return 0
    if k <= 0 or k > len(dicts):
        print("please input a valid value for k, which is from 1  to" + len(dicts))
        return 0
    
    sum1 = 0
    for q in dicts:
        sum2 = 0
        for i in range(k):
            sum2 += (2**(precision(dicts, i+1) * len(dicts)) - 1) / np.log(1 + (i+1))
        
        sum1 += sum2 / Z
                     
        return sum1 / len(dicts)


if __name__ == '__main__':
	import sys
	args = sys.argv
	if args[1] == "precision":
		print("the precision@" + args[2] + " is ")
		print(precision(dicts, int(args[2])))
	elif args[1] == "MAP":
		print("the MAP of the sample for " + args[2] + "ranked is: " + str(mAP(dicts, int(args[2]))))
	elif args[1] == "MRR":
		print("the MRR of the sample is " + str(mRR(dicts)))
	elif args[1] == "nDCG":
		print("the nDCG of the sample for " + args[2] + " ranked is: " + str(nDCG(dicts, int(args[2]))))
