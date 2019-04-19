#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r'''
102-char-encodings.py
'''

############################## Unicode Encodings ###############################

a = 'A'
b = '安'
c = 'あ'
print("Unicode encodings:")
print("A ->", ord(a))
print("安 ->", ord(b))
print("あ ->", ord(c))
print("66 ->", chr(66))
print("26412 ->", chr(26412))
print("12409 ->", chr(12409))

e = '\u4e2d\u6587'
print("\\u4e2d\\u6587 is", e)

######################### Character Type str to bytes ##########################
# Data read from network/disk is bytes stream

d = "ABC"
e = b"ABC"  # bytes type - each character only takes one byte space
f = "中文"
g = b"\xe4\xb8\xad\xe6\x96\x87"
h = b"\xe4\xb8\xad\xff"
print("ABC is encoded to", d.encode('ascii'))    # encode() str to bytes using ASCII
print("中文 is encoded to", f.encode('utf-8'))    # encode() Chinese str to bytes using UTF-8
#print(f.encode('ascii'))    # Chinese character cannot use ASCII encoding
print("b\"ABC\" is decoded to", e.decode('ascii'))
print("b\"\\xe4\\xb8\\xad\\xe6\\x96\\x87\" is decoded to", g.decode('utf-8'))
#print("b\"\\xe4\\xb8\\xad\\xff\" is decoded to", h.decode('utf-8')) # error
print("b\"\\xe4\\xb8\\xad\\xff\" is decoded to", h.decode('utf-8', errors='ignore'))

################################ Length ########################################

i = "XYZ"
j = b"\xe4\xb8\xad\xe6\x96\x87"
k = "中文"
print("len(\"XYZ\")=", len(i))
print("len(b\"\\xe4\\xb8\\xad\\xe6\\x96\\x87\")=", len(j))
print("len(\"中文\")=", len(k))
print("len(\"中文\".encode(\'utf-8\'))=", len(k.encode('utf-8')))

############################ Formatted Output ##################################
print("Timestamp: 0x%x, CPU: %d, temperature: %.1f, status: %s" % (0xabcd, 0, 67.38, "Good"))

