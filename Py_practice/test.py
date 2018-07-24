#!/usr/bin/python
#coding=utf-8

import numpy as np
import pandas as pd
import shutil


pada1 = pd.read_csv('test1.txt', sep='\t')
pada2 = pd.read_csv('test2.txt', sep='\t')
pada3 = pd.read_csv('test3.txt', sep='\t')

dicts = []
dicts = [pada1, pada2, pada3]

sum = 0
### precision@1
for i in range(len(dicts)):
    sum += dicts[i]["label"][0]
    
precision1 = sum / len(dicts)


### precision@k
def precision(dicts, k):
    if dicts == None:
        print("Please load your test set!")
        return 0
    if k<=0:
        print("please keep value K as the number more than 0!")
        return 0
    
    sum = 0
    for i in range(len(dicts)):
        sum += dicts[i]["label"][k-1]
    res = sum / len(dicts)
    return res


## total number of sentence in the sample dicts
def total(dicts):
    if dicts == None:
        print("Please load your test set!")
        return 0
    
    res = 0
    for i in range(len(dicts)):
        res += len(dicts[i])
    return res


## MAP value
def mAP(dicts, k):
    
    if dicts == None:
        print("Please load your test set!")
        return 0
    if k<=0:
        print("please keep value K as the number more than 0!")
        return 0
    
    sum1 = 0
    for q in dicts:
        sum2 = 0
        Nq = 0
        for i in range(k):
            sum2 += precision(dicts, i+1) * (precision(dicts, i+1) * len(dicts))
        for j in range(len(q)):
            Nq += q["label"][j]
            
        sum1 += sum2 / Nq
    return sum1 / total(dicts)

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
    return sum1 / total(dicts)


## Z is a constant number
Z = 2.331

## nDCG
def nDCG(dicts, k):
    if dicts == None:
        print("Please load your test set!")
        return 0
    if k<=0:
        print("please keep value K as the number more than 0!")
        return 0
    
    sum1 = 0
    for q in dicts:
        sum2 = 0
        for i in range(k):
            sum2 += (2**(precision(dicts, i+1) * len(dicts)) - 1) / np.log(1 + (i+1))
        
        sum1 += sum2 / Z
                     
        return sum1 / total(dicts)


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
