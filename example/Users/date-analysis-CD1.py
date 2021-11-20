import matplotlib.pyplot as plt
import math
import csv 
import os
userss = []
reprints=[]
def redelist1(filename1,path):
	filename2=path+'/'+filename1
	users=[]
	try:	
		with open(filename2,encoding='utf-8') as f:
			reader=csv.reader(f)
			header_row=next(reader)
			for row in reader:
				userid_new=float(row[0])
				netidnum=int(row[1])
				ll=int(row[2])
				aa=str(row[4])
				new_user={'user_id':userid_new,'net_id':netidnum,'lever_num':ll,'Authority':aa}
				users.append(new_user)
	except FileNotFoundError:
		pass
	else:			
		
	     userss.extend(users)


def redelist2(filename1,path):
	filename2=path+'/'+filename1
	users=[]
	try:	
		with open(filename2,encoding='utf-8') as f:
			reader=csv.reader(f)
			header_row=next(reader)
			for row in reader:
				userid_new=float(row[0])
				net_id=int(row[3])
				orgin_id=float(row[1])
				next_id=float(row[2])
				new_user={'reprint_id':userid_new,'net_id':net_id,'orgin_id':orgin_id,'next_id':next_id}
				users.append(new_user)
	except FileNotFoundError:
		pass
	else:			
		
	     reprints.extend(users)	
	          
path1='D:/Anaconda3/envs/python38/fake news/example/Users'
path2='D:/Anaconda3/envs/python38/fake news/example/Reprints'
files1= os.listdir(path1) 
files2= os.listdir(path2) 
for filename in files1: 
     redelist1(filename,path1)
for filename in files2: 
     redelist2(filename,path2) 

i=22
count=0     
links=[]
points=[]
for row in range(30):
	new_point={'dsitance':row,'num':0}
	points.append(new_point)
for row1 in userss[0:]:
	if row1['net_id']==i:
		for row2 in userss[0:]:
			if row2['net_id']== i:
				distance=0		
				a_point=row1
				b_point=row2
				last_point_a=a_point
				last_point_b=b_point
				while(last_point_a['user_id']!=last_point_b['user_id']):											
					if last_point_a['lever_num']>=last_point_b['lever_num']:
						a_edgenew=float(0)
						for row5 in reprints[0:]:
							if row5['net_id']==i:
								if row5['next_id']==last_point_a['user_id']:
									a_edgenew=row5['orgin_id']			
						for row6 in userss[0:]:
							if row6['net_id']==i:
								if row6['user_id']==a_edgenew:
									last_point_a=row6
									distance=distance+1
					if last_point_a['lever_num']<last_point_b['lever_num']:
						b_edgenew=float(0)
						for row5 in reprints[0:]:
							if row5['net_id']==i:
								if row5['next_id']==last_point_b['user_id']:
									b_edgenew=row5['orgin_id']								
						for row6 in userss[0:]:
							if row6['net_id']==i:
								if row6['user_id']==b_edgenew:
									last_point_b=row6
									distance=distance+1																						
					
				for row7 in points[0:]:
					if row7['dsitance']==distance:
						row7['num']=row7['num']+1
				count=count+1
				print(count)

stu1 = ['net_id','distance','num'] #write user1
nameuser='1.csv'
out = open(nameuser,'a', newline='')
csv_write = csv.writer(out,dialect='excel')
csv_write.writerow(stu1)
for row in points[0:]:
	stu=[i,row['dsitance'],row['num']]
	csv_write.writerow(stu)
