# -*- codeing = utf-8 -*-
# @Time : 2020/9/25 17:01
# @Author : lzf
# @File : network.py
# @Software :PyCharm
# fake news
import math
import queue
import csv
for i in range(2,100):
  filename = 'D:\Anaconda3\envs\DATA set/real News1/normal'+str(i)+'.csv'
    #filename = 'fn'+str(i)+'.csv'
  with open ( filename, encoding='utf-8' ) as f:
    reader = csv.reader ( f )    #调用csv.reader()，并将前面存储的文件对象作为实参传递给它，从而创建一个与该文件相关联的阅读器（reader）对象。我们将这个阅读器对象存储在reader中
    header_row = next ( reader )   #迭代器next（），模块csv包含函数next()，调用它并将阅读器对象传递给它时，它将返回文件的下一行。在前面的代码中，我们只调用了next()一次，因此得到的是文件的第一行，其中包含文件头，我们将返回的数据存储在header_row()中

    highs = []
    users = []
    reprints = []   #三个列表 highs，users，reprints

    count = 1
    netidnum =98

    for row in reader:
        userid_new = float ( row[1] )    #表中的mid
        if row[3] == 'null':
            orginid = float ( 0 )
        else:
            orginid = float ( row[3] )   #表中的parent

        new_user = {'user_id': userid_new, 'net_id': netidnum, 'lever_num': 0, 'degree': 1}
        users.append ( new_user )     #将new_user添加到列表users中

        new_reprint = {'reprint_id': count, 'orgin_id': orginid, 'next_id': userid_new, 'net_id': netidnum}
        reprints.append ( new_reprint )   #将new_reprint添加到列表reprints中
        count = count + 1

#广度优先遍历，生成传播网络
    lever = 0
    co = 2
    nu = 0
    q = queue.Queue ()   #对列q
    for rowr in reprints[0:]:
        if rowr['orgin_id'] == float ( 0 ):  #根节点（创始者）
            for rowu in users[0:]:
                if rowu['user_id'] == rowr['next_id']:
                    v = rowu
                    q.put ( v )     #将users中的数据写入队列q
                    rowu['lever_num'] = lever

            lever = lever + 1     #从根节点到第一层

    while co != count:
        u = q.qsize ()  #u=队列q中数据大小
        i = 0
        for i in range ( u ):
            nextd = q.get ()   #从队列中返回并删除一个节点
            for rowr in reprints[0:]:
                if rowr['orgin_id'] == nextd['user_id']:
                    for rowu in users[0:]:
                        if rowu['user_id'] == rowr['next_id']:
                            v = rowu
                            q.put ( v )
                            rowu['lever_num'] = lever
                            co = co + 1
        lever = lever + 1

    distance = float ( row[5] )

    for row in reprints[0:]:
        if row['orgin_id'] != float ( 0 ):
            a = row['orgin_id']
            for rowu in users[0:]:
                if rowu['user_id'] == a:
                    rowu['degree'] = rowu['degree'] + 1
    sum1 = float ( 0 )
    sum2 = float ( 0 )
    n = count
    for row in users[0:]:
        k = row['degree']
        k2 = math.pow ( k, 2 )
        sum1 = sum1 + float ( k2 )
        sum2 = sum2 + float ( k )
    sum1 = sum1 / float ( n )
    sum2 = sum2 / float ( n )
    down = float ( sum2 )
    up = float ( math.sqrt ( sum1 ) )
    Hr = float ( up / down )
    Hs = float ( math.sqrt ( n ) )
    h = math.log ( Hs ) - math.log ( Hr )  # Heterogeneity parameters异质性

    num1 = 0
    num2 = 0
    for row in users[0:]:
        if row['lever_num'] == 1:
            num1 = num1 + 1
        if row['lever_num'] == 2:
            num2 = num2 + 1
    rls = float ( num2 / num1 )  # Ratio of layer size
    print ( num1, num2 )
    print("rls=",rls)   #层大小的比例n2/n1

    stu1 = ['user_id', 'net_id', 'lever_num', 'degree', 'Authenticity']  # write user1
    nameuser = 'User_' + str ( netidnum ) + 'real.csv'   #文件名
    out = open ( nameuser, 'a', newline='' )
    csv_write = csv.writer ( out, dialect='excel' )
    csv_write.writerow ( stu1 )   #写入目录
    for row in users[0:]:
        stu = [row['user_id'], row['net_id'], row['lever_num'], row['degree'], 'real']
        csv_write.writerow ( stu )  #写入数据

    stu2 = ['reprint_id', 'orgin_id', 'next_id', 'net_id']  # write reprint1
    namer = 'Reprint_' + str ( netidnum ) + 'real.csv'
    out = open ( namer, 'a', newline='' )
    csv_write = csv.writer ( out, dialect='excel' )
    csv_write.writerow (stu2)
    for row in reprints[0:]:
        stu = [row['reprint_id'], row['orgin_id'], row['next_id'], row['net_id']]
        csv_write.writerow ( stu )

    stu3 = ['net_id', 'num', 'rls', 'h', 'Authenticity','distance']  # write network
    out = open ( 'Network1.csv', 'a', newline='' )         #‘a’追加内容， 使用newline（）使文件不空行
    csv_write = csv.writer ( out, dialect='excel' )  #以excel格式写文件
    #csv_write.writerow ( stu3 )
    stu = [netidnum, count, rls, h, 'real',distance]
    csv_write.writerow ( stu )

    print ( "write over" )





