#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

sum = 0
for i in range(100):
    sum = sum + i
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print(name)
    if name == 'Lisa':
        break
    print('Hello '+name)


names = ["Jack", "Bob", "Rose", "Lily", "Marry"]
dic = {};
for name in names:
    dic[name] = name.upper()
print(dic)
dic.clear()

for index in range(len(names)):
    dic[index] = names[index]
print(dic)
