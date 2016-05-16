#!/usr/bin/env python3
"""
字符串正规化
"""
s = 'pýtĥöñ\fis\tawesome\r\n'
remap = {
        ord('\t') : ' ',
        ord('\f') : ' ',
        ord('\r') : None, #表示删除回车符
        }

a = s.translate(remap)
print(a)
