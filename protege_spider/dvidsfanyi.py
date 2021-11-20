import difflib
import shlex				
import csv
import os
import re
import sys
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
from openpyxl import Workbook

symmetric_dataset = False
from csv import reader
import hashlib
import random
import openpyxl
from openpyxl import Workbook
import requests
apiurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'

appid='20210917000948146'
secretKey='eEmnox8LALVoh3J8UTWo'
def translateBaidu(content, fromLang='en', toLang='zh'):
	

	salt = str(random.randint(32768, 65536))
	sign = appid + content + salt + secretKey
	sign = hashlib.md5(sign.encode("utf-8")).hexdigest()
	try:
	#if 1:
		paramas = {
            'appid': appid,
            'q': content,
            'from': fromLang,
            'to': toLang,
            'salt': salt,
            'sign': sign
        }
		response = requests.get(apiurl, paramas)
		jsonResponse = response.json()  # 获得返回的结果，结果为json格式
		print(jsonResponse)
		dst = str(jsonResponse["trans_result"][0]["dst"])  # 取得翻译后的文本结果
	
		return dst
	except Exception as e:
		print(e)
		return False						
def redlist4(path,filename1):#读活动dvids文件2	
	filename2=path+'/'+filename1
	try:
		with open(filename2,encoding='utf-8') as f:	
			reader=csv.reader(f)
			part=[]
			header_row=next(reader)		
			for row in reader:	
				title=chuli1(row[3])
				content=row[7]					
				new_case={'time':row[2],'content':content,'unit':row[5],'title':title,
				'spot':row[4],'href':row[1],'related':[],'related_organization':[],
				'chinese_title':'','chinese_content':'','chinese_spot':''}
				if 	new_case not in part:							
					part.append(new_case)
			return 	part															
	except FileNotFoundError:	
		pass
def chuli1(string):
	string=string.replace(':','-')	
	string=string.replace('“','')
	string=string.replace('”','')
	string=string.replace('"','')
	return 	string
	
def writer_activity(row,i):	#写入
	stu=['title','content','time','href',
	'spot','related','related_organization','chinese_spot','chinese_title','chinese_content'
			]# write reprint1
	path=''

	j=int(i/500)
	name='dvids'+str(j)+'.csv'
	with open(name,"a+",newline='', encoding='utf-8-sig') as f:
		writer = csv.writer(f)	
		#writer.writerow(stu)
		
		#for row in edges[:]:
		try:
			stu=[i,row['title'],row['content'],row['time'],row['href'],
				row['spot'],str(row['related']),str(row['related_organization'])
				,row['chinese_spot'],row['chinese_title'],row['chinese_content']]
			writer.writerow(stu)
		except:
				pass
					
	print('write succed ')	
def timechange2(time_string):#时间格式转换
	wordtime= [word1 for word1 in re.split('[. ]',time_string)if word1 !='' and word1 !=' ']
	year=wordtime[2]		
	day=wordtime[1]
	month=	wordtime[0]
	#monthlist=['January','February','March','April','May','June','July','August','September','October','November','December']
	#month=monthlist.index(month)
	time=year+'/'+month+'/'+day
	return time
	
def test():

	alls_activity=[]				
	path='D:\All_Script\Python_deagel/activity_dvids'
	files= os.listdir(path)
	j=0
	for filei in files:#活动dvids
		edges1=redlist4(path,filei)
		edges2=[]
		for row in edges1:
			j=j+1
			if j<=361:
				continue
			try:
				time=timechange2(row['time'])
				row['time']=time
			except:
				continue	
			content=row['content']
			wordss= [word1 for word1 in re.split('[\n]',content) if word1 !=''and word1 !=' ']
			contents=''.join(wordss)
			row['chinese_spot']=translateBaidu(row['spot'])
			print(row['chinese_spot'])
			row['chinese_content']=translateBaidu(contents)
			print(row['chinese_content'])
			title=row['title']
			row['chinese_title']=translateBaidu(title)
			print(row['chinese_title'])
			#writer_activity ( row, j )
			if row['chinese_spot']!=False:
				writer_activity ( row,j)
			else:
				print("错误")
				sys.exit ()
			
			if row not in alls_activity:
				alls_activity.append(row)
	
	#n=500
	#l=int(len(alls_activity)/n)
	#for i in range(l+2):

		#	start=i*n
		#	end=start+n
		#	edges3=[]
			#	for row in alls_activity[start:end]:
		#	edges3.append(row)
		#name='activity_dvids'+str(i)+'.csv'
		#writer_activity(edges3,name)

test()	
			

