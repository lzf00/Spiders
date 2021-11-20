import csv
def clearBlankLine():
    file1 = open('D:\All_Script\Python_vessel_MMSI/MMSI_7.9.csv', 'r', encoding='utf-8') # 要去掉空行的文件
    file2 = open('D:\All_Script\Python_vessel_MMSI/MMSI1.csv', 'w', encoding='utf-8')
    try:
        for line in file1.readlines():
            if line == '\n':
                line = line.strip("\n")
            file2.write(line)

    finally:
        file1.close()
        file2.close()

def unique_file():
    file1 = open('D:\All_Script\Python_vessel_MMSI/MMSI1.csv', 'r', encoding='utf-8')
    file2 = open('D:\All_Script\Python_vessel_MMSI/MMSI2.csv', 'w', encoding='utf-8')
    writer = csv.writer(file2)
    lines_seen = set()  # 生成没有空行的文件
    a=1
    try:
        for line in file1.readlines ():
            if line not in lines_seen:
                file2.write ( line )
                print ( 'line:', line )
                print(a)
                a=a+1
                # writer.writerow([line['text'],line['time']])
                lines_seen.add ( line )
            # else:
            #     print(line[-11:])

    finally:
        file1.close()
        file2.close()

if __name__ == '__main__':
    clearBlankLine()
    unique_file()
