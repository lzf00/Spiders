import csv
def clearBlankLine():
    file1 = open('D:\All_Script\Twitter/MIL_Radar.csv', 'r', encoding='utf-8') # 要去掉空行的文件
    file2 = open('D:\All_Script\Twitter/MIL_Radar_clean1.csv', 'w', encoding='utf-8')
    try:
        for line in file1.readlines():
            if line == '\n':
                line = line.strip("\n")
            file2.write(line)

    finally:
        file1.close()
        file2.close()

def unique_file():
    file1 = open('D:\All_Script\Twitter/MIL_Radar_clean1.csv', 'r', encoding='utf-8')
    file2 = open('D:\All_Script\Twitter/MIL_Radar_clean1_f1.csv', 'w', encoding='utf-8')
    writer = csv.writer(file2)
    lines_seen = set()  # 生成没有空行的文件
    try:
        for line in file1.readlines():
            if line not in lines_seen:
                file2.write(line)
                print('line:',line)
                # writer.writerow([line['text'],line['time']])
                lines_seen.add(line)

    finally:
        file1.close()
        file2.close()

if __name__ == '__main__':
    clearBlankLine()
    unique_file()


