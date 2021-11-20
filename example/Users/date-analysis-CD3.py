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
	count=0
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
	
	
	net=33
	x_date=[]
	y_date=[]
	for i in range(maxd):
		n=0
		for row in 	points[:]:
			if row['id_net']==net:
				if row['distance']==i:
					n=row['num']+n
					count=count+n
		x=i
		c=float(n/count)
		if c!=0:
			y=math.log(c)
			x_date.append(x)
			y_date.append(y)
		

	z1 = np.polyfit(x_date, y_date, 1) 
	p1 = np.poly1d(z1)
	print (z1)  
	k=z1[0]
	a=-(1/k)
	print (a)
	plt.plot(x_date, y_date, marker='*', c='b')
	plt.title('Distance distribution of each node network no.33')
	plt.xlabel('distance')
	plt.ylabel('probiblity')
	plt.show()
