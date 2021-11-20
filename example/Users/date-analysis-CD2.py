import math
import queue
import csv 
import matplotlib.pyplot as plt
import numpy as np
filename='all-distance.csv'

with open(filename,encoding='utf-8') as f:
	reader=csv.reader(f)
	header_row=next(reader)
	points=[]
	maxd=0
	mind=0
	
	for row in reader:
		distance=int(row[1])
		id_net=float(row[0])
		num=int(row[2])
		xz=''
		if id_net<=16 :
			xz='real'
		else :
			xz='fake'
		new_point={'id_net':id_net,'distance':distance,'num':num,'xz':xz}	
		points.append(new_point)		
		if maxd <= distance :
			maxd=distance
	
	x_date_fake=[]
	x_date_real=[]
	y_date_fake=[]
	y_date_real=[]
	count_real=0
	count_fake=0
	
	for i in range(maxd):
		n=0
		for row in 	points[:]:
			if row['xz']=='real':
				if row['distance']==i:
					n=row['num']+n
		x=i
		y=n
		x_date_real.append(x)
		y_date_real.append(y)
	for i in range(maxd):
		n=0
		for row in 	points[:]:
			if row['xz']=='fake':
				if row['distance']==i:
					n=row['num']+n
		x=i
		y=n
		x_date_fake.append(x)
		y_date_fake.append(y)			
					
					
	z1 = np.polyfit(x_date_fake, y_date_fake, 1) 
	p1 = np.poly1d(z1)
	print (z1)  
	k=z1[0]
	print (z1)
	print (k)
	plt.plot(x_date_real, y_date_real, marker='*', c='r')
	plt.plot(x_date_fake, y_date_fake, marker='*', c='b')
	plt.title('red is real news,blue is fake news')
	plt.xlabel('distance')
	plt.ylabel('num')
	plt.show()
	
		
