# -*- codeing = utf-8 -*-
# @Time : 2020/12/13 22:10
# @Author : lzf
# @File : uuid.py
# @Software :PyCharm
import time, hashlib

def create_id():
    m = hashlib.md5 ()
    m.update ( bytes ( str ( time.perf_counter() ), encoding='utf-8' ) )
    return m.hexdigest ()
print ( type ( create_id () ) )
print ( create_id () )
