import matplotlib.pyplot as plt
import math
import csv

filename = 'Network.csv'

with open ( filename, encoding='utf-8' ) as f:
    reader = csv.reader ( f )
    header_row = next ( reader )
    net = []

    for row in reader:
        idnet = float ( row[0] )
        num = row[1]
        a = float ( row[2] )
        rls = a
        h = float ( row[3] )
        Authenticity = str ( row[4] )
        distance = float ( row[5] )    #节点对的距离？？？
        new = {'net_id': idnet, 'num': num, 'rls': rls, 'h': h, 'Authenticity': Authenticity, 'p': 0, 'Distance': distance}
        net.append ( new )

    ni = float ( 2.7 )
    reals = []
    fakes = []
    for i in range ( 15 ):
        new_real = {'id': i, 'num': 0}
        new_fake = {'id': i, 'num': 0}
        reals.append ( new_real )
        fakes.append ( new_fake )
    for row in net[0:]:
        rlsc = row['Distance']
        if row['Authenticity'] == 1:
            ins = 0
            while rlsc < 30.1:
                rlsc = rlsc + ni
                ins = ins + 1
            for rows in reals[0:]:
                if rows['id'] == ins:
                    rows['num'] = rows['num'] + 1
        if row['Authenticity'] == 0:
            ins = 0
            while rlsc < 30.1:
                rlsc = rlsc + ni
                ins = ins + 1
            for rows in fakes[0:]:
                if rows['id'] == ins:
                    rows['num'] = rows['num'] + 1

    ps = []
    for i in range ( 11 ):
        pfi = 0
        pri = 0
        pi = float ( 0 )
        for row1 in reals[0:]:
            if row1['id'] == i:
                pri = row1['num']
        for row1 in fakes[0:]:
            if row1['id'] == i:
                pfi = row1['num']

        if pfi != 0 and pri != 0:
            pi = float ( pfi / (pfi + pri) )
        else:
            pi = 0
        new_p = {'id': i, 'pi': pi}
        ps.append ( new_p )

    for row in net[0:]:
        rlsc = row['Distance']
        if row['Authenticity'] == 'real':
            ins = 0
            while rlsc < 30.1:
                rlsc = rlsc + ni
                ins = ins + 1
            for rows in ps[0:]:
                if rows['id'] == ins:
                    row['p'] = float ( 1 ) - rows['pi']
        if row['Authenticity'] == 'fake':
            ins = 0
            while rlsc < 30.1:
                rlsc = rlsc + ni
                ins = ins + 1
            for rows in ps[0:]:
                if rows['id'] == ins:
                    row['p'] = rows['pi']

    # for row in net[0:]:
    #  if row['Authenticity']=='real':
    #     plt.scatter(row['rls'],row['p'],edgecolor='red')
    #  if row['Authenticity']=='fake':
    #     plt.scatter(row['rls'],row['p'],edgecolor='blue')

    ni = 0
    for row in ps[0:]:

        x = 3 + ni
        yi = float ( row['pi'] )
        if yi == float ( 0 ):
            y = 0
        else:
            y = math.log ( yi )
        plt.scatter ( x, y )
        ni = ni + 2.7
    plt.title ( "distance distribution" )
    plt.xlabel ( "distance" )
    plt.ylabel ( "Possibility of false news" )
    plt.show ()
