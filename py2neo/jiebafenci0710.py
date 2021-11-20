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
#from grakel.datasets import fetch_dataset
#from grakel.kernels import WeisfeilerLehman, VertexHistogram,RandomWalk,ShortestPath,Propagation,PyramidMatch,LovaszTheta,SvmTheta
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
#from grakel import Graph
#from grakel.kernels import NeighborhoodHash,PyramidMatch
import numpy as np
import pandas as pd
import jieba
import jieba.analyse
import codecs
#from translate import Translator
symmetric_dataset = False
all_edges=[]
all_jinzan=[]
all_jinfei=[]
nodes=[]
edges=[]

def redlist1(filename1):#读文件1，武器产品csv
		
	try:
		with open(filename1,encoding='utf-8') as f:	
			reader=csv.reader(f)
			header_row=next(reader)		
			for row in reader:			
										
				new_case={'class':row[0],'bussiness':row[1],'product':row[2],'describe':row[3],'progress':row[4],'parameter':row[5]}								
				all_edges.append(new_case)		#将读入的字典加入边列表
	except FileNotFoundError:	
		pass

def redlist2(filename1):#读文件2,janes新闻csv
	try:
		with open(filename1,encoding='utf-8') as f:	
			reader=csv.reader(f)
			header_row=next(reader)		
			for row in reader:	#按行读文件
				time=row[3]
				time=time.replace(' ','')		
				contents=row[5]
				contents=contents.replace(' ','')	
				contents=contents.replace("'","")
				new_case={'id':row[0],'key':row[1],'key_process':row[2],'time':time,'title':row[4],'content':contents,'href':row[6]}								
				all_jinzan.append(new_case)															
	except FileNotFoundError:	
		pass

def redlist3(filename1):#读文件3，产品经费csv
		
	try:
		with open(filename1,encoding='utf-8') as f:	
			reader=csv.reader(f)
			header_row=next(reader)		
			for row in reader:	
				time=row[3]
				time=time.replace(' ','')		
				contents=row[5]
				contents=contents.replace(' ','')	
				contents=contents.replace("'","")
				new_case={'product':row[0],'2020实际经费':row[1],'2021颁布经费':row[2],'2022申请经费':row[3]}								
				all_jinfei.append(new_case)															
	except FileNotFoundError:	
		pass

def wordfrequency():# 词频统计，暂时不用
	name='weapon-all.csv'
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
def verb_words():#提取动词
	words = [word.strip() for word in open("D:/python_work/武器/table/动词.txt","r",encoding='utf-8').readlines()]
	return words  

def noun_words():#名词表
	words = [word.strip() for word in open("D:/python_work/武器/table/名词.txt","r",encoding='utf-8').readlines()]
	return words  	

def it_words():#指代词表
	words = [word.strip() for word in open("D:/python_work/武器/table/指代词.txt","r",encoding='utf-8').readlines()]
	return words  	

def property_words():#属性词表
	words = [word.strip() for word in open("D:/python_work/武器/table/属性.txt","r",encoding='utf-8').readlines()]
	return words  
	
def timechange(time):#-

	words= [word1 for word1 in re.split('[年月日 /]',time)]
	print(time,words)
	year=words[0]
	month=words[1]
	day=words[2]
	if len(year)==2:
		year='20'+year			
	datetime=year+'-'+month+'-'+day
	#datetime2=year+'-'+month+'-'+day
	timestamp=Time_to_timestamp(datetime)
	return datetime,timestamp	
def selection_sort(lists):
	n=len(lists)
	for i in range (0,n):
		mins = i
		for j in range(i+1,n):
			a=lists[j]  #
			b=lists[mins]
			if a['timestamp']<b['timestamp']:  #时间排序
				mins=j
				lists[mins],lists[i]=lists[i],lists[mins]
	return lists	

def Time_to_timestamp(times):#转换为时间戳
	import time	
	timeArray = time.strptime(times, "%Y-%m-%d")     
	timeStamp = float(time.mktime(timeArray))	 #将本地时间的时间元组转换为纪元以来的秒数。
	return timeStamp	
def timelist(edges):#标记时间序列	
	selection_sort(edges)	
	return edges			

def writer_Triplet_edge(edges):	#写处理完毕的数据：关系表
	path='D:/python_work/武器/'
	namer=path+'edges'+'.csv'
	with open(namer,"w+",newline='', encoding='utf-8-sig') as f:
		writer = csv.writer(f)	
		stu=[':START_ID',':END_ID',':TYPE','attribute']
		writer.writerow(stu)
		for row in edges[0:]:
			stu=[row['x'],row['y'],row['relationship'],row['attributeedge']]			
			writer.writerow(stu)
		print('work over')
def writer_Triplet_node(edges):	#写处理完毕的数据：节点表
	path='D:/python_work/武器/'
	namer=path+'nodes.csv'
	stu=['entity:ID','name',':LABEL','attribute']
	
	with open(namer,"w+",newline='', encoding='utf-8-sig') as f:
		writer = csv.writer(f)
		writer.writerow(stu)	
		for row in edges[0:]:
			stu=[row['id'],row['name'],row['class'],row['attributenode']]		
			writer.writerow(stu)
		print('work over')

def writer_Triplet(edges):	#处理完毕的数据，测试文本函数
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
			
def fenci2():  # 处理数据得到三元组
	
	add_cidian()
	bushuwords=['发射平台','运输','部署']
	xinzhuangwords=['长度','宽度','高度','重量','直径','翼展']
	fanweiwords=['作战范围','范围']
	shechengwords=['最大射程','有效射程','射程']
	Triplet=[]

	for row in all_edges[0:]:
		if row['bussiness'] =='' or row['product']=='' or row['class']=='':
			break
		content1=row['describe']
		content2=row['progress']
		content3=row['parameter'] #参数
		class1=row['class']
		if '公司' not in row['bussiness']:
			bussiness=row['bussiness']+'公司'
		else:
			bussiness=row['bussiness']
		product=row['product']
		#产品实体与公司关系建立
		new={'subject':product,'relationship':'公司所属','objects':bussiness,'class_s':'产品','class_o':'公司','attributeedge':'','attributenode':''}
		if new not in Triplet:
			Triplet.append(new)
		#产品实体与分类关系建立
		new={'subject':product,'relationship':'分类','objects':class1,'class_s':'产品','class_o':'产品分类','attributeedge':'','attributenode':''}
		if new not in Triplet:
			Triplet.append(new)

		#描述实体与产品关系建立
		Descriptionentity=row['product']+'(描述)'
		new={'subject':product,'relationship':'描述','objects':Descriptionentity,'class_s':'产品','class_o':'参数','attributeedge':'','attributenode':''}
		if new not in Triplet:
			Triplet.append(new)
		words= [word1 for word1 in re.split('[。]',content3)]	#使用‘句号。’切分content3，并将分词结果word1依次存入words列表中

		#处理content3，参数
		for roww in words[0:]:	
			seg_list1 = jieba.cut_for_search(roww) #jieba搜索引擎模式
			date=[]
			
			for rows in seg_list1:
				date.append(rows)
			s=''
			for row1 in propertywords[0:]:		
				if row1 in roww:
					s=row1	
			if s!='':	#s不为空则做处理
				ss=roww.replace(' ','')  #replace(old,new,num) / (旧字符串，新字符串，最大替换次数)
				ss=ss.replace(s,'')	
				o=s
				if ss!='':  #表示此参数有参数值
					if o in bushuwords:
						o='部署'+'/'+row['product']
						ss=ss.replace(' ','')
						new={'subject':product,'relationship':'描述所属','objects':o,'class_s':'产品','class_o':'部署','attributeedge':'','attributenode':ss}
						if new not in Triplet:
							Triplet.append(new)
					elif '打击'in o:		
						o='打击目标'+'/'+row['product']
						ss=ss.replace(' ','')
						new={'subject':product,'relationship':'描述所属','objects':o,'class_s':'产品','class_o':'打击目标','attributeedge':'','attributenode':ss}
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
							new={'subject':Descriptionentity,'relationship':'描述所属','objects':o,'class_s':'参数','class_o':'参数类型','attributeedge':'','attributenode':''}
							if new not in Triplet:
								Triplet.append(new)
						else:
							for rowtt in Triplet[0:]:
								if 	rowtt['objects']==s and Descriptionentity==rowtt['subject']:
									rowtt['attributenode']=rowtt['attributenode']+ss
					elif o in fanweiwords:
						o='作战范围'+'/'+row['product']
						ss=ss.replace(' ','')
						new={'subject':Descriptionentity,'relationship':'描述所属','objects':o,'class_s':'参数','class_o':'参数类型','attributeedge':'','attributenode':ss}
						if new not in Triplet:
							Triplet.append(new)
					elif o in shechengwords:	
						o='射程'+'/'+row['product']
						ss=ss.replace(' ','')
						new={'subject':Descriptionentity,'relationship':'描述所属','objects':o,'class_s':'参数','class_o':'参数类型','attributeedge':'','attributenode':ss}
						if new not in Triplet:
							Triplet.append(new)
					else:
						o=o+'/'+row['product']
						ss=ss.replace(' ','')
						new={'subject':Descriptionentity,'relationship':'描述所属','objects':o,'class_s':'参数','class_o':'参数类型','attributeedge':'','attributenode':ss}
						if new not in Triplet:
							Triplet.append(new)	
						
		#
		for row_y in all_jinfei[0:]:
			if product==row_y['product']:
				
				new={'subject':product,'relationship':'预算变化','objects':'2022经费',
				'class_s':'产品','class_o':'经费','attributeedge':'','attributenode':row_y['2022申请经费']}
				if new not in Triplet:
					Triplet.append(new)	
				new={'subject':'re2022经费','relationship':'预算变化','objects':'2021经费',
				'class_s':'经费','class_o':'经费','attributeedge':'','attributenode':row_y['2021颁布经费']}
				if new not in Triplet:
					Triplet.append(new)	
				new={'subject':'2021经费','relationship':'预算变化','objects':'2020经费',
				'class_s':'经费','class_o':'经费','attributeedge':'','attributenode':row_y['2020实际经费']}
				if new not in Triplet:
					Triplet.append(new)			
					
		
		#进展
		process=[]
		for row_jin in	all_jinzan[0:]:
			if 'List' not in row_jin['title']	and row_jin['content']!='' and row_jin['content']!='[]' :
				key=row_jin['key']	
				if key in product:
					time,timestamp=timechange(row_jin['time'])
					new={'time':time,'timestamp':timestamp,'content':row_jin['content'],'title':row_jin['title'],'href':row_jin['href'],'key':key}
					if new not in process:
						process.append(new)
				
		if len(process)>1:
			process=timelist(process)
		processlist=[]
		last=0
		for row_p in process[0:]:
			print(row_p['time'],'*',row_p['title'],'\n')
		count=1	
		for row_p in process[0:]:
			if len(processlist)==0:
				theobjects=row_p['time']+'-进展-'+str(count)+row_p['title']
				new={'subject':product,'relationship':'进展','objects':theobjects,
				'class_s':'产品','class_o':'进展内容','attributeedge':row_p['time'],'attributenode':row_p['content']+'//'+row_p['href']}
				
				if new not in Triplet:
					Triplet.append(new)	
				if new not in processlist:	
					processlist.append(new)	
					last=new
					count=count+1
			else:
				#last=processlist[-1]
				
				theobjects=row_p['time']+'-进展-'+str(count)+row_p['title']
				if 	last['objects'] !=theobjects:
					new={'subject':last['objects'],'relationship':'进展','objects':theobjects,
				'class_s':'进展内容','class_o':'进展内容','attributeedge':row_p['time'],'attributenode':row_p['content']+'//'+row_p['href']}
					if new not in Triplet:
						Triplet.append(new)	
					if new not in processlist:	
						processlist.append(new)	
						last=new	
						count=count+1
		for row_pp in processlist[0:]:	
			print(row_pp['subject'],'/',row_pp['objects'],'\n')			
	Documentchange(Triplet)	
	writer_Triplet(Triplet)


def Documentchange(date): #处理得到节点和关系表
		
	nodes=[]
	edges=[]
	enetiy=[]
	count=0
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
	writer_Triplet_node(nodes)			
	writer_Triplet_edge(edges)				
	
def add_cidian():	#往jieba额外添加关键词和词频
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
		jieba.add_word(row,freq=len(row))

def test():  #备份上一次结果
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
						new={'subject':Progressentity,'relationship':'进展所属','objects':roww,'class_s':'进展时间','class_o':'进展内容','attributeedge':'','attributenode':''}
						if new not in Triplet:
							Triplet.append(new)		
				
					if len(Progresslist)>0:
						last=Progresslist[-1]
						new={'subject':last,'relationship':'进展','objects':Progressentity,'class_s':'进展时间','class_o':'进展时间','attributeedge':datetime,'attributenode':''}
						if new not in Triplet:
							Triplet.append(new)		
					else:
						new={'subject':product,'relationship':'进展','objects':Progressentity,'class_s':'产品','class_o':'进展时间','attributeedge':datetime,'attributenode':''}
						if new not in Triplet:
							Triplet.append(new)		 						
					Progresslist.append(Progressentity)		
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
#name='C:/Users/Administrator/Documents/Tencent Files/770507089/FileRecv/weapon-0708.csv'
path='D:/python_work/武器/'
name='weapon-导弹.csv'
redlist1(path+name)
name='weapon-电磁频谱.csv'
redlist1(path+name)
name='weapon-侦查武器.csv'
redlist1(path+name)
name='weapon-反导武器.csv'
redlist1(path+name)
name='weapon-核武器.csv'
redlist1(path+name)
name='janes.csv'
redlist2(path+name)
name='武器经费.csv'
redlist3(path+name)

verbwords=verb_words()
nounwords=noun_words()
itwords=it_words()
propertywords=property_words()

stopwords=['(',')','[',']']
jieba.load_userdict('D:/python_work/武器/table/user_dict.txt')  #将自定义词典载入jieba词库
fenci2()
