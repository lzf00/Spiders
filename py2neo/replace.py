# -*- codeing = utf-8 -*-
# @Time : 2021/7/14 18:43
# @Author : lzf
# @File : replace.py
# @Software :PyCharm
'''
遇到文中的空格就换行，txt文件
'''
def delblankline(infile, outfile):
    infopen = open ( infile, 'r', encoding="utf-8" )
    outfopen = open ( outfile, 'w', encoding="utf-8" )
    db = infopen.read ()
    outfopen.write ( db.replace ( ' ', '\n' ) ) #replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
    infopen.close ()
    outfopen.close ()

delblankline ( "zzvips.txt", "o3.txt" )