# -*- codeing = utf-8 -*-
# @Time : 2021/11/6 19:25
# @Author : lzf
# @File : HanLP.py
# @Software :PyCharm
import hanlp
import pandas as pd
hanlp.pretrained.mtl.ALL # MTL多任务，具体任务见模型名称，语种见名称最后一个字段或相应语料库// SRL语义角色标注
HanLP = hanlp.load(hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_BASE_ZH)
filepath1='D:\Program Files (x86)/neo4j-community-3.5.28-2\import/news.csv'
filepath2='D:\Program Files (x86)/neo4j-community-3.5.28-2\import/activity.csv'

d1 = pd.read_csv ( filepath1, usecols=['content'] )
#print(d1[0:])
d = pd.read_csv ( 'news.csv', usecols=['content'] )
#print(d[0:])

HanLP['ner/ontonotes'].dict_whitelist = {'午饭后': 'TIME','F-15EX':'AIRF'} #自定义词典，午饭后这个词的类型为TIME
#doc = HanLP('2021年测试高血压是138，时间是午饭后2点45，低血压是44,F-35', tasks='ner/msra')
#doc.pretty_print()
#print(doc['ner/msra'])
#See https://hanlp.hankcs.com/docs/api/hanlp/components/mtl/tasks/ner/tag_ner.html

num=1
for x in d1['content'][55:80]:
    doc = HanLP(x)
    cons=doc["tok/fine"]
    print(cons)
    #print(doc)
    #print('ontonotes:::',doc['ner/ontonotes'])  # GPE,LOCATION
    #print ( 'msra:::', doc['ner/msra'] )  #LOCATION
    print('pku:::',doc['ner/pku'])  #ns
    #doc.pretty_print()

    for x1 in doc['ner/ontonotes']:
        if 'GPE' in x1 or 'LOCATION' in x1:
            print ( x1 )
            x1=x1.split(",", 3)[2]
            print(cons[int(x1)],cons[int(x1)+1])  #对分词结果操作
            print(num)

    for x2 in doc['ner/msra']:
        if 'LOCATION' in x2:
            print(x2)
            x3=str(x2)
            x3 = x3.split ( ",", 3 )[2]
            print ( cons[int(x3)],cons[int(x3)+1] )
            print(num)

    print(num,  " ::: -------------------------------------------------------- ")
    num=num+1

