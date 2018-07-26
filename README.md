# DeepLearning_study

## Use this repo as the script for the evaluation of our retrieval mdoel

### All of the script code and data sample sources are in folder "Py_practice"

when run the script, first gather data
```
1. input data1 format like: "document_id    relevance_score   question     answering" from the calculation of our retrieval model
```
```
2. input data2 format like: "question   answer1   answer2   answer3(Q&A ground truth)"
```
### Notice: It's better to choose the same length of this two data in order to calculate label first
对于测试数据集中的每个“用户”问句：返回top20 answering，每个answering占一个row（所以78句会有78*20 = 1560行）对于每一行，如果返回的answer在1中数据达尔文最佳答句-1，2，3中出现，则赋值rater_score = 1 else = 0

## Environment: 
```
1. python == 3.6+
```
```
2. pip install np 
   pip install pandas
```


```
$ pip install
```
dafafdsa
