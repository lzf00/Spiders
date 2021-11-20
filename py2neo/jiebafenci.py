import csv
import os
import re
import jieba.posseg as pseg
import nltk
import psutil
import datetime
from nltk import pos_tag
from nltk import word_tokenize
from datetime import datetime
from datetime import timezone
from datetime import timedelta
import queue
import  math
import random
import matplotlib.pyplot as plt
import networkx as nx
import turtle
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
import jieba
import jieba.analyse
import codecs
symmetric_dataset = False
all_edges=[]

nodes=[]
edges=[]

def redlist1(filename1):#读文件2
		
	try:
		with open(filename1,encoding='utf-8') as f:	
			reader=csv.reader(f)
			header_row=next(reader)		
			for row in reader:									
				new_case={'class':row[0],'bussiness':row[1],'product':row[2],'describe':row[3],'progress':row[4],'parameter':row[5]}								
				all_edges.append(new_case)															
	except FileNotFoundError:	
		pass

def wordfrequency():# 词频统计
	name='weapon-0708.csv'
	#设置pd的显示长度
	pd.set_option('max_colwidth',500)
	 
	#载入数据
	rows=pd.read_csv(name, header=0,encoding='utf-8',dtype=str)
	 
	segments = []
	for index, row in rows.iterrows():
		content = row[2]
		#TextRank 关键词抽取，只获取固定词性
		words = jieba.analyse.textrank(content, topK=500,withWeight=False,allowPOS=('ns', 'n', 'vn', 'v'))
		content = row[3]
		#TextRank 关键词抽取，只获取固定词性
		words = jieba.analyse.textrank(content, topK=500,withWeight=False,allowPOS=('ns', 'n', 'vn', 'v'))
		splitedStr = ''
		for word in words:
			# 记录全局分词
			segments.append({'word':word, 'count':1})
			splitedStr += word + ' '
	dfSg = pd.DataFrame(segments)
	 
	# 词频统计
	dfWord = dfSg.groupby('word')['count'].sum()
	#导出csv
	dfWord.to_csv('keywords.csv',encoding='utf-8')
def verb_words():#动词表
	words = [word.strip() for word in open("D:/python_work/table/动词.txt","r",encoding='utf-8').readlines()]
	return words  

def noun_words():#动词表
	words = [word.strip() for word in open("D:/python_work/table/名词.txt","r",encoding='utf-8').readlines()]
	return words  	

def it_words():#指代词表
	words = [word.strip() for word in open("D:/python_work/table/指代词.txt","r",encoding='utf-8').readlines()]
	return words  	

def property_words():#属性词表
	words = [word.strip() for word in open("D:/python_work/table/属性.txt","r",encoding='utf-8').readlines()]
	return words  
	
def timeget(content):#-
	timeword=['年','月','日']
	mark=0
	seg_list1 = jieba.cut_for_search(content) #搜索引擎模式  
	date=[]
	for row in seg_list1:
		if row in timeword:
			mark=1
		date.append(row)	
	if mark==1:
		year=''
		month=''
		day=''
		datetimes=[0,0,0]
		datetime=''
		for j in range(len(date)):
			row=date[j]
			if row=='年':
				last=date[j-1]
				year=last
				if year.isdigit(): 
					if int(year)<2022 and int(year)>1900:
						datetimes[0]=int(year)
				else:
					return 0		
			if row=='月':
				last=date[j-1]
				month=last
				if month.isdigit(): 
					datetimes[1]=int(month)
			if row=='日':
				last=date[j-1]
				day=last		
				if day.isdigit(): 			
					datetimes[2]=int(day)	 				
		if datetimes[0]==0 and datetimes[1]==0 and  datetimes[2]==0 :
			return 0
					
		datetime=str(datetimes[0])+'-'+str(datetimes[1])+'-'+str(datetimes[2])
		return datetime
	else:
		return 0	
		
def writer_edge(edges):	#处理完毕的数据
	namer='news-同源5.csv'
	
	with open(namer,"a+",newline='', encoding='utf-8-sig') as f:
		
		writer = csv.writer(f)	
		for row in edges[0:]:
			stu=[row['class'],row['bussiness'],row['product'],row['describe'],row['progress']]		
			writer.writerow(stu)
		print('work over')


def writer_Triplet_edge(edges):	#处理完毕的数据
	path='D:/Program Files (x86)/neo4j-community-3.5.28-2/bin/import/'
	namer=path+'edges'+'.csv'
	with open(namer,"a+",newline='', encoding='utf-8-sig') as f:
		writer = csv.writer(f)	
		stu=[':START_ID',':END_ID',':TYPE','attribute']
		writer.writerow(stu)
		for row in edges[0:]:
			stu=[row['x'],row['y'],row['relationship'],row['attributeedge']]			
			writer.writerow(stu)

def writer_Triplet_node(edges):	#处理完毕的数据
	path='D:/Program Files (x86)/neo4j-community-3.5.28-2/bin/import/'
	namer=path+'nodes.csv'
	stu=['entity:ID','name',':LABEL','attribute']
	
	with open(namer,"a+",newline='', encoding='utf-8-sig') as f:
		
		writer = csv.writer(f)
		writer.writerow(stu)	
		for row in edges[0:]:
			stu=[row['id'],row['name'],row['class'],row['attributenode']]		
			writer.writerow(stu)
		print('work over')

def writer_Triplet(edges):	#处理完毕的数据
	path='D:/python_work/武器/'
	namer=path+'test.csv'
	stu=['subjiect','relationship','object',
	'class_s','class_o','attributeedge','attributenode']
	
	with open(namer,"a+",newline='', encoding='utf-8-sig') as f:
		
		writer = csv.writer(f)
		writer.writerow(stu)	
		for row in edges[0:]:
			stu=[row['subject'],row['relationship'],row['objects'],
			row['class_s'],row['class_o'],row['attributeedge'],row['attributenode']]		
			writer.writerow(stu)
		print('work over')		
			
	
def fenci2():
	
	add_cidian()
	bushuwords=['发射平台','运输']
	xinzhuangwords=['长度','宽度','高度','重量','直径','翼展']
	fanweiwords=['作战范围','范围']
	shechengwords=['最大射程','有效射程','射程']
	Triplet=[]
	edges=[]
	nodes=[]
	count=0	
	for row in all_edges[0:]:
		class1=row['class']+'(分类)'
		if '公司' not in row['bussiness']:
			bussiness=row['bussiness']+'(公司)'
		else:
			bussiness=row['bussiness']	
		product=row['product']+'(产品)'
		#产品实体与公司关系建立
		new={'subject':product,'relationship':'公司所属','objects':bussiness,'class_s':'产品','class_o':'公司','attributeedge':'','attributenode':''}
		if new not in Triplet:
			Triplet.append(new)
		#产品实体与分类关系建立
		new={'subject':product,'relationship':'分类','objects':class1,'class_s':'产品','class_o':'产品分类','attributeedge':'','attributenode':''}
		if new not in Triplet:
			Triplet.append(new)
		#对描述建立分析
		
	es,ns,count=Documentchange(Triplet,count)	
	edges.extend(es)
	nodes.extend(ns)
	writer_Triplet(Triplet)	
	for row in all_edges[0:]:
		Triplet=[]
		content1=row['describe']
		content2=row['progress']
		content3=row['parameter']
		class1=row['class']+'(分类)'
		bussiness=row['bussiness']+'(公司)'
		product=row['product']+'(产品)'
		
		#对描述建立分析
		
		#描述实体与产品关系建立
		Descriptionentity=row['product']+'(描述)'
		new={'subject':product,'relationship':'描述','objects':Descriptionentity,'class_s':'产品','class_o':'描述实体','attributeedge':'','attributenode':''}
		if new not in Triplet:
			Triplet.append(new)
		words= [word1 for word1 in re.split('[。]',content3)]	#if word1 not in stopwords
		
		for roww in words[0:]:	
			seg_list1 = jieba.cut_for_search(roww) #搜索引擎模式 
			date=[]
			
			for rows in seg_list1:
				date.append(rows)
			s=''
			for row1 in propertywords[0:]:		
				if row1 in roww:
					s=row1	
			if s!='':				
				ss=roww.replace(' ','')
				ss=ss.replace(s,'')	
				o=s
				if ss!='':
					if o in bushuwords:
						o='部署'+'/'+row['product']
						ss=ss.replace(' ','')
						new={'subject':Descriptionentity,'relationship':'描述所属','objects':o,'class_s':'描述实体','class_o':'描述客体','attributeedge':'','attributenode':ss}
						if new not in Triplet:
							Triplet.append(new)
					elif 	o in xinzhuangwords:
						o='形状'+'/'+row['product']
						ss=roww.replace(' ','')
						mark=0
						for rowtt in Triplet[0:]: 
							if 	rowtt['objects']==o and Descriptionentity==rowtt['subject']:
									rowtt['attributenode']=rowtt['attributenode']+ss
									mark=1
						if mark==0:	
							new={'subject':Descriptionentity,'relationship':'描述所属','objects':o,'class_s':'描述实体','class_o':'描述客体','attributeedge':'','attributenode':''}
							if new not in Triplet:
								Triplet.append(new)
						else:
							for rowtt in Triplet[0:]:
								if 	rowtt['objects']==s and Descriptionentity==rowtt['subject']:
									rowtt['attributenode']=rowtt['attributenode']+ss
					elif o in fanweiwords:
						o='作战范围'+'/'+row['product']
						ss=ss.replace(' ','')
						new={'subject':Descriptionentity,'relationship':'描述所属','objects':o,'class_s':'描述实体','class_o':'描述客体','attributeedge':'','attributenode':ss}
						if new not in Triplet:
							Triplet.append(new)
					elif o in shechengwords:	
						o='射程'+'/'+row['product']
						ss=ss.replace(' ','')
						new={'subject':Descriptionentity,'relationship':'描述所属','objects':o,'class_s':'描述实体','class_o':'描述客体','attributeedge':'','attributenode':ss}
						if new not in Triplet:
							Triplet.append(new)
					else:
						o=o+'/'+row['product']
						ss=ss.replace(' ','')
						new={'subject':Descriptionentity,'relationship':'描述所属','objects':o,'class_s':'描述实体','class_o':'描述客体','attributeedge':'','attributenode':ss}
						if new not in Triplet:
							Triplet.append(new)	
						
		conut=1
		#对进展建立分析
		words= [word1 for word1 in re.split('[。]',content2) if word1 not in stopwords  ]	#if word1 in verbwords and word1 in nounwords	
		Progresslist=[]
		for roww in words[0:]:
			if roww!='':
				seg_list1 = jieba.cut_for_search(roww) #搜索引擎模式 
				#时间判断
				datetime1=timeget(roww)
				datetime=''
				if datetime1!=0:
					datetime=datetime1
					if len(Progresslist)!=0:
						conut=conut+1		
				#进展实体
				Progressentity=product+'-'+'进展'+'-'+str(conut)
				
				#进展实体与产品关系建立
				date=[]
				for row in seg_list1:
					date.append(row)
				if Progressentity in Progresslist:	
					
					for row_T in Triplet[0:]:
						if row_T['subject']==Progressentity:
							row_T['objects']=row_T['objects']+roww
							break
				else:
					
					if  roww!='':		
						new={'subject':Progressentity,'relationship':'进展所属','objects':roww,'class_s':'进展实体','class_o':'进展客体','attributeedge':'','attributenode':''}
						if new not in Triplet:
							Triplet.append(new)		
				
					if len(Progresslist)>0:
						last=Progresslist[-1]
						new={'subject':last,'relationship':'进展','objects':Progressentity,'class_s':'进展实体','class_o':'进展实体','attributeedge':datetime,'attributenode':''}
						if new not in Triplet:
							Triplet.append(new)		
					else:
						new={'subject':product,'relationship':'进展','objects':Progressentity,'class_s':'产品','class_o':'进展实体','attributeedge':datetime,'attributenode':''}
						if new not in Triplet:
							Triplet.append(new)		 						
					Progresslist.append(Progressentity)		
					
					
		es,ns,count=Documentchange(Triplet,count)	
		edges.extend(es)
		nodes.extend(ns)
		writer_Triplet(Triplet)					
	writer_Triplet_node(nodes)			
	writer_Triplet_edge(edges)			
	
def Possessive(date,subject):#所有格分析
	
	for i in range(len(date)):
		row3=date[i]	
		if row3 =='的' and row3!=date[-1]: 
			subjects=[]					
			objects=date[i+1]
			if 	objects in nounwords:
				j=i-1
				while date[j] not in verbwords and date[j] in nounwords  and subject!=date[j]:
					subjects.append(date[j])
					j=j-1
				s=''
						
				for q in range(len(subjects)):
					s=subjects[q]+'的'+s
						
				s=s+objects
				date[i]=s
				date[i+1]=s			
				for q in range(len(subjects)):
					row4=subjects[q]
					for p in range(len(date)):
						if date[p]==row4:
							date[p]=s
				if s not in nounwords:			
					nounwords.append(s)			
	print(date)														
	return date				
def Documentchange(date,count):
		
	nodes=[]
	edges=[]
	enetiy=[]
	for row in 	date[0:]:	
		if row['subject'] not in enetiy:
			enetiy.append(row['subject'])
			new={'id':count,'name':row['subject'],'class':row['class_s'],'attributenode':row['attributenode']}
			if new not in nodes:
				nodes.append(new)
				count=count+1
		if row['objects'] not in enetiy:
			enetiy.append(row['objects'])
			new={'id':count,'name':row['objects'],'class':row['class_o'],'attributenode':row['attributenode']}
			if new not in nodes:
				nodes.append(new)
				count=count+1	
	
	for row in 	date[0:]:
		a= row['subject']
		x=0
		b=	row['objects'] 
		y=0
		for row1 in nodes[0:]:
			if 	a==	row1['name']:
				x=row1['id']
				break
		for row1 in nodes[0:]:
			if 	b==	row1['name']:
				y=row1['id']
				break		
		new={'x':x,'y':y,'relationship':row['relationship'],'attributeedge':row['attributeedge']}
		if new not in edges:
			edges.append(new)		
				
	return 	edges,nodes	,count
def add_cidian():	
	for row in all_edges[0:]:
		content1=row['describe']
		content2=row['progress']
		words= [word1 for word1 in re.split('[。]',content1)  ]	#if word1 in verbwords and word1 in nounwords
		for row in words[0:]:	
			seg_list1 = jieba.cut_for_search(row) #搜索引擎模式 
			date=[]
			for row in seg_list1:
				date.append(row)
			for i in range(len(date)):
				row=date[i]
				if row.isdigit():
				
					word=row+date[i+1]
					#print(word)
					jieba.add_word(word,freq=len(word))
					nounwords.append(word)
	for row in propertywords[0:]:
		jieba.add_word(word,freq=len(word))							
def test():
		conut=0
		#对进展建立分析
		words= [word1 for word1 in re.split('[。]',content2) if word1 not in stopwords  ]	#if word1 in verbwords and word1 in nounwords	
		Progresslist=[]
		for row in words[0:]:
			seg_list1 = jieba.cut_for_search(row) #搜索引擎模式 
			#时间判断
			datetime1=timeget(row)
			datetime=''
			if datetime1!=0:
				datetime=datetime1
				conut=conut+1		
			#进展实体
			Progressentity=product+'-'+'进展'+'-'+str(conut)
			date=[]
			for row in seg_list1:
				date.append(row)
			for j in range(len(date)):
				rowj=date[j]
				if '公司' in rowj:
					date[j]=bussiness	
			#主体获取
			subject=Progressentity

			date=Possessive(date,subject)	
			relationship=[]
			for row1 in date[0:]:
				if row1 in verbwords:	
					relationship.append(row1)
			
			for row1 in date[0:]:
				if row1 in verbwords :	
					relationship.append(row1)

			objects=[]
			for row2 in date[0:]:
				if 	row2 !=subject and row2 in nounwords:
					objects.append(row2)
					
			objects2=[]		
			for p in range(len(objects)):
				row_p=objects[p]
				mark=0
				for q in range(len(objects)):		
					row_q=objects[q]
					if row_p in row_q:
						mark=1
					if 	row_p==row_q:
						mark=0
						
				if mark==0:
					objects2.append(row_p)	
				
			count1=0	
			verb='所属'	
			for row1 in date[0:]:		
				if row1 in objects2:
					if 	 row1!='' and subject !=row1:	
						new1={'subject':subject,'relationship':verb,'objects':row1,'class_s':'进展实体','class_o':'客体','attribute—edge':'','attribute—node':''}
						if new1 not in Triplet:
							Triplet.append(new1)
						
				if row1 in relationship:
					verb=relationship[count1]
					count1=count1+1			
							
							
			#进展实体与产品关系建立
			new={'subject':product,'relationship':'进展','objects':Progressentity,'class_s':'产品','class_o':'进展实体','attribute':datetime,'attribute—node':''}
			if new not in Triplet:
				Triplet.append(new)				
				
				
				
#wordfrequency()	

name='weapon-0708.csv'
redlist1(name)
verbwords=verb_words()
nounwords=noun_words()
itwords=it_words()
propertywords=property_words()


stopwords=['(',')','[',']']
jieba.load_userdict('D:/python_work/table/user_dict.txt')
fenci2()
