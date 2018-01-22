# -*- coding: utf-8 -*-

import jieba
import jieba.analyse
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text  import  TfidfTransformer
from sklearn.cluster import KMeans

def creat_TwoDimensionalArray(number) :
    array = []
    for index in range(number):
        item = []
        array.append(item)
    return array

data = pd.read_csv('Data/dataset-utf8.csv')
dataContent = data['postContent']
dataContent_array = []
replaceText_array = []

for item in dataContent :
#   取代文字 stopword 放置於replaceText 等待替換
#    for text in replaceText_array :
#        item = item.replace(text , '')
#  精確切割
#    seg_list = jieba.cut(item , cut_all=False)
#  關鍵詞抽取
    # topK限定最大的抽取詞彙數量
    # withWeight決定抽取的關鍵詞彙是否包含權重
    # allowPOS是否針對特定
    seg_list = jieba.analyse.extract_tags(item, topK=20, withWeight=False, allowPOS=())
# dataContent_array是儲存需切割後的字串，以空白區隔，vectorizer會將字串進行切割轉為斷詞陣列
    dataContent_array.append(" ".join(seg_list))
# 計算開始
# 內文篩選與擷取相關資料
vectorizer = CountVectorizer()
# 詞彙出現頻率
word_feq = vectorizer.fit_transform(dataContent_array)
# 出現的詞彙
word = vectorizer.get_feature_names()
# 分數計算
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(word_feq)
# 分群
clusterNumber = 10
kmeans = KMeans(n_clusters=clusterNumber, random_state=0).fit(tfidf)
number = 0
content_list = creat_TwoDimensionalArray(clusterNumber)
for label in kmeans.labels_ :
    content_list[label].append(dataContent[number])
    print ('PostContent index-%d : %s' %(number+1 , dataContent[number]))
    number = number + 1 
for cluster in range(clusterNumber) :
    print('Cluster %d' %(cluster))
    for content in content_list[cluster] :
        print(content)

