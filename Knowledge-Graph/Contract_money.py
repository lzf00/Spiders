# -*- codeing = utf-8 -*-
# @Time : 2021/11/20 19:35
# @Author : lzf
# @File : Contract_money.py
# @Software :PyCharm
# Simple usage
import csv
import pandas as pd
from stanfordcorenlp import StanfordCoreNLP
import json
nlp = StanfordCoreNLP(r'D:\Anaconda3\stanford-corenlp-4.3.1')
#分词（word_tokenize）、词性标注（pos_tag）、命名实体识别（ner）、句法依存分析（dependency_parse）、句法解析（parse）
# file_path='D:\All_Script\Python_deagel\hetong/hetong1.csv'
# f = open ( file_path, 'a+', encoding='utf-8', newline='' )
# writer = csv.writer ( f )
# writer.writerow ( ['key',"Money"] )

filepath1=r'D:\All_Script\Python_deagel\hetong\hetong1.csv'
#filepath2='D:\Program Files (x86)/neo4j-community-3.5.28-2\import/activity.csv'

d1 = pd.read_csv ( filepath1, usecols=['content'] )
print(d1[0:])
#d = pd.read_csv ( 'news.csv', usecols=['content'] )

key=2
Ms=[]
for x in d1['content'][0:]:  #424对应CSV426
    print ( 'Named Entities:', nlp.ner ( x ) )
    try:
        #print ('Tokenize:', nlp.word_tokenize(x))
        #print ('Part of Speech:', nlp.pos_tag(x))
        print ('Named Entities:', nlp.ner(x))
        #print ('Constituency Parsing:', nlp.parse(x))
        #print ('Dependency Parsing:', nlp.dependency_parse(x))
        numc=0
        all_numc=[]
        num=0
        for c in nlp.ner(x):
            tag=str ( c ).split ( "'", 4 )[3]
            #print ( type(tag) )
            if tag=="O":  #间隔标签为大写的欧（O）
                #print(numc)
                all_numc.append(numc)
            numc=numc+1

        money=[]
        for xx in nlp.ner(x):

            if 'MONEY' in xx :
                NER3=str(xx).split("'",4)[1]
                print("DATE:::",num,":  ",NER3)
                #if NER2 not in TIME1 :
                money.append ( NER3 )
                if str(nlp.ner(x)[num+1]).split("'",4)[3]=="O":
                    print("O")
                    money.append ( ";" )
            else:
                LOC1='[]'
            num=num+1
        LOC1 = ' '.join ( money ).strip ()
        Ms.append(LOC1)

        #writer.writerow ( [key, LOC1, COUN1,TIME11] )
    except:
        #writer.writerow ( [key, "[]", "[]","[]"] )
        LOC1="[]"
        Ms.append(LOC1)
        print("wu")
    print ( key,"------------------------------------------------------------------------" )
    key = key + 1

data = pd.read_csv ( filepath1 )  # pandas读文件某一列
# print ( data )
print ( data.columns )  # 获取列索引值
data1 = Ms  # 获取列名为flow的数据作为新列的数据
#context.append ( "xxx ")
print(len(Ms))
print("money:::",Ms)
data['picture'] = data1  # 将新列的名字设置为cha
data.to_csv ( filepath1, mode='w', index=False ,encoding='utf-8')
# mode=a，以追加模式写入,header表示列名，默认为true,index表示行名，默认为true，再次写入不需要行名
print ( data )

nlp.close()  # Do not forget to close! The backend server will consume a lot memery.



