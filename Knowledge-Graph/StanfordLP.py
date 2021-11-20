#-*- codeing = utf-8 -*-
# @Time : 2021/11/14 17:57
# @Author : lzf
# @File : StanfordLP.py
# @Software :PyCharm

# Simple usage
import csv
import pandas as pd
from stanfordcorenlp import StanfordCoreNLP
import json
nlp = StanfordCoreNLP(r'D:\Anaconda3\stanford-corenlp-4.3.1')
#分词（word_tokenize）、词性标注（pos_tag）、命名实体识别（ner）、句法依存分析（dependency_parse）、句法解析（parse）
file_path='D:\All_Script\Python_deagel/Stanford11.csv'
f = open ( file_path, 'a+', encoding='utf-8', newline='' )
writer = csv.writer ( f )
writer.writerow ( ['key','LOCATION','COUNTRY',"TIME"] )

filepath1='D:\Program Files (x86)/neo4j-community-3.5.28-2\import/news.csv'
filepath2='D:\Program Files (x86)/neo4j-community-3.5.28-2\import/activity.csv'

d1 = pd.read_csv ( filepath1, usecols=['content'] )
print(d1[0:])
#d = pd.read_csv ( 'news.csv', usecols=['content'] )

key=0
sentence = 'Guangdong University of Foreign Studies is located in Guangzhou.'
for x in d1['content'][0:]:  #424对应CSV426
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

        locnum=[]
        LOC=[]
        COUN=[]
        TIME1=[]
        for xx in nlp.ner(x):
            if 'LOCATION' in xx :
                NER0=str(xx).split("'",4)[1]
                print("LOCATION:::",num,":  ",NER0)
                #if NER0 not in LOC:
                LOC.append(NER0)
                if str(nlp.ner(x)[num+1]).split("'",4)[3]=="O":
                    print("O")
                    LOC.append ( ";" )
                locnum.append(num)

            if 'COUNTRY' in xx :
                NER1=str(xx).split("'",4)[1]
                print("COUNTRY:::",num,":  ",NER1)
                #if NER1 not in COUN:
                COUN.append ( NER1 )
                LOC.append ( NER1 )
                if str(nlp.ner(x)[num+1]).split("'",4)[3]=="O":
                    print("O")
                    COUN.append ( ";" )
                    LOC.append  (";" )

            if 'DATE' in xx :
                NER2=str(xx).split("'",4)[1]
                print("DATE:::",num,":  ",NER2)
                #if NER2 not in TIME1 :
                TIME1.append ( NER2 )
                if str(nlp.ner(x)[num+1]).split("'",4)[3]=="O":
                    print("O")
                    TIME1.append ( ";" )
            num=num+1
        LOC1 = ' '.join ( LOC ).strip ()
        COUN1 = ' '.join ( COUN ).strip ()
        TIME11 = ' '.join ( TIME1 ).strip ()
        writer.writerow ( [key, LOC1, COUN1,TIME11] )
    except:
        writer.writerow ( [key, "[]", "[]","[]"] )
        print("wu")
    print ( key,"------------------------------------------------------------------------" )
    key = key + 1
#for xx1 in nlp.ner(x):

nlp.close()  # Do not forget to close! The backend server will consume a lot memery.
