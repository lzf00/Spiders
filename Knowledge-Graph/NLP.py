# -*- codeing = utf-8 -*-
# @Time : 2021/7/4 12:35
# @Author : lzf
# @File : NLP.py
# @Software :PyCharm
from numpy import *
from pylab import *
import pandas as pd
import jieba
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
#导入文本向量化工具CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer
#引入算法
vect=CountVectorizer(ngram_range=(1, 1),stop_words='english')# 通过词袋模型 ,max_features对所有关键词的term frequency进行降序排序，只取前max_features个作为关键词集
#d = pd.read_csv('fake_news16.csv', usecols=['内容'])#pandas读文件某一列
d = pd.read_csv('产品目录.csv', usecols=['进展'])#pandas读文件某一列
#d = pd.read_csv( '产品目录.csv', usecols=['进展'] )#pandas读文件某一列
#d = pd.read_csv('T疫情期间真实新闻.csv', usecols=['内容'])#pandas读文件某一列

#print(d)
file_path= 'missile_words.csv'
#file_path = 'F_NLP.csv'
#file_path = 'T_NLP.csv'
f = open(file_path, 'w', encoding='utf-8',newline='')
writer = csv.writer(f)

# 创建停用词列表
def stopwordslist():
      stopwords = [line.strip() for line in open('stop_word.txt',encoding='UTF-8').readlines()]
      return stopwords
stopwords = stopwordslist()
for x in d['进展']:
        try:
            #print(x)
            # 导入文本数据(这里是文本元组),用jieba对中文文本进行分词
            cn = jieba.cut ( x )
            cn = [' '.join ( cn )]# 使用空格作为词与词之间的分界线
            print ( '1:::',cn )          # 打印结果

            vect.fit ( cn )        # 用CountVectorizer算法拟合文本数据
            #print('2:::',cn)
            print('aaaaaaaaaa',len ( vect.vocabulary_ ))  #分词个数
            word_num=len ( vect.vocabulary_ )
            if(word_num>10):
                print ( '单词数：{}'.format ( len ( vect.vocabulary_ ) ) )
                print ( '分词：{}'.format ( vect.vocabulary_ ) )
                bag_of_words = vect.transform ( cn )        # 使用.transform功能
                print ( '转化为词袋的特征：\n{}'.format ( repr ( bag_of_words ) ) )
                print ( bag_of_words )
                print ( '词袋的密度表达：\n{}'.format ( bag_of_words.toarray () ) )
                tfidf = TfidfVectorizer ( max_features=10).fit_transform ( cn )
                tfidf=tfidf.toarray()
                tfidf=tfidf.tolist()
                #tfidf1 = np.array([*tfidf])
                print ( tfidf )
                writer.writerow(tfidf)
                #np.savetxt ( 'NLP.csv',tfidf1, fmt = '%.18', delimiter = ' ')
        except:
             ('：：：该文本不能进行分词')
