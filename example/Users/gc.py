# -*- codeing = utf-8 -*-
# @Time : 2020/11/9 15:57
# @Author : lzf
# @File : gc.py
# @Software :PyCharm
from collections import OrderedDict
seq = ''
chr_d = OrderedDict()
with open ( "C:\\Users\\Lzf\\Desktop\\test.fa.txt" , "r" ) as f:
     for line in f:
         #line = line.rstrip()
         line = line.strip()
         if line.startswith( ">" ):
             chr_d[seq] = ''
         else :
             line = line.upper()
             chr_d[seq]=chr_d[seq]+line
     for name,chr_seq in chr_d.items(): #此方法返回元组对的列表
         #print (name,chr_seq)
         seqLen = len (chr_seq)
         N = chr_seq.count( "N" )
         GC = chr_seq.count( "G" ) + chr_seq.count( "C" )
         print (name)
         print (seqLen,N / seqLen,GC / (seqLen - N))