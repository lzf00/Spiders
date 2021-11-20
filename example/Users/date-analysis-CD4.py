import matplotlib.pyplot as plt
import math
import csv 
filename= 'Network.csv'
with open(filename,encoding='utf-8') as f:
	reader=csv.reader(f)
	header_row=next(reader)
	net=[]	
	for row in reader:
		idnet=float(row[0])
		num=row[1]
		a=float(row[2])
		a=math.log(a)
		rls=round(a,2)
		h=float(row[3])
		Authenticity=str(row[4])
		distance=float(row[5])
		new={'net_id':idnet,'num':num,'rls':rls,'h':h,'Authenticity':Authenticity,'p':0,'Distance':distance}
		net.append(new)


	points_real=[]
	points_fake=[]
	maxa=5.37133409111475
	mina=0.366751095479942
	maxb=1.57471767371918
	minb=0.3951377622739
	cost=(maxa-mina)/9
	cost2=(maxb-minb)/9
	x_date_fake=[]
	x_date_real=[]
	y_date_fake=[]
	y_date_real=[]
	count_real=0
	count_fake=0
	minl=mina
	for row in 	range(9):

		minr=minl+cost
		mid=(minl+minr)/2
		
		nwe_ponit={'left':minl,'right':minr,'num':0,'mid':mid}	
		minl=minl+cost
		points_real.append(nwe_ponit)
	minl=minb	
	for row in 	range(9):
		
		minr=minl+cost2
		mid=(minl+minr)/2	
		nwe_ponit={'left':minl,'right':minr,'num':0,'mid':mid}	
		minl=minl+cost2
		points_fake.append(nwe_ponit)
	for row in net[0:]:
		if row['Authenticity']=='real':
			for row1 in points_real[0:]:
				if row['Distance']<row1['right'] and row['Distance']>=row1['left']:
					row1['num']=row1['num']+1
					count_real=count_real+1
		if row['Authenticity']=='fake':				
			for row1 in points_fake[0:]:
				if row['Distance']<row1['right'] and row['Distance']>=row1['left']:
					row1['num']=row1['num']+1
					count_fake=count_fake+1

	for row in points_real[0:]:
		x=row['mid']
		if row['num'] !=0:
			y=float(row['num']/count_real)				
		else:
			y=0			
		x_date_real.append(x)			
		y_date_real.append(y)			
	for row in points_fake[0:]:
		x=row['mid']
		if row['num'] !=0:
			y=float(row['num']/count_fake)				
		else:
			y=0			
		x_date_fake.append(x)			
		y_date_fake.append(y)	

	plt.plot(x_date_real, y_date_real, marker='*', c='r')
	plt.plot(x_date_fake, y_date_fake, marker='*', c='b')
	plt.title('red is real news,blue is fake news')
	plt.xlabel('CD')
	plt.ylabel('probability')
	plt.show()	
