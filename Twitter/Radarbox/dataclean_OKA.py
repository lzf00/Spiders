# -*- codeing = utf-8 -*-
# @Time : 2020/12/1 18:14
# @Author : lzf
# @File : dataclean_KADENA.py
# @Software :PyCharm
import csv
def clearBlankLine():
    file1 = open('D:\All_Script\Python_Radarbox/Radarbox_OKA.csv', 'r', encoding='utf-8') # 要去掉空行的文件
    file2 = open('D:\All_Script\Python_Radarbox/Radarbox_OKA_clean1.csv', 'w', encoding='utf-8')
    try:
        for line in file1.readlines():
            if line == '\n':
                line = line.strip("\n")
            file2.write(line)

    finally:
        file1.close()
        file2.close()

def unique_file():
    file1 = open('D:\All_Script\Python_Radarbox/Radarbox_OKA_clean1.csv', 'r', encoding='utf-8')
    file2 = open('D:\All_Script\Python_Radarbox/Radarbox_OKA_clean1_f1.csv', 'w', encoding='utf-8')
    writer = csv.writer(file2)
    lines_seen = set()  # 生成没有空行的文件
    try:
        for line in file1.readlines():
            if line[-11:] not in lines_seen:
                file2.write(line)
                print('line:',line[-11:])
                # writer.writerow([line['text'],line['time']])
                lines_seen.add(line[-11:])
            # else:
            #     print(line[-11:])

    finally:
        file1.close()
        file2.close()

if __name__ == '__main__':
    clearBlankLine()
    unique_file()
