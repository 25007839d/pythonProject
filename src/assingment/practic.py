# st = 'sagar is good boy'
# sp=st.split(' ')
# rev=[]
# len=len(sp)
# print(len,sp)
# for i in sp:
#    rev.append(sp[len-1])
#    len=len-1
# print(rev)
#
# a=[2,5,8,6]
#
# li = {i:i for i in a}
# print(li)

#decorator
# def mul(fun):
#    def inner():
#       a=fun()
#       return a*2
#    return inner
# @mul
# def add():
#    a=10
#    b=20
#
#    return a+b
# a=add()
# print(a)

#generator

#
# def fac(num):
#    fact=1
#    for i in range(1,num+1):
#       fact=fact*i
#    yield fact
#
# num=int(input("enter"))
# a=fac(num)
# print(next(a))

# sum of 9 pair
# set1 = {3,4,5,6,0}
# set2 = {9,5,6,1,8}
# lis = []
#
# for i in set1:
#     for j in set2:
#         if i+j==9:
#             print((i,j))
#         else:
#             pass

# lambda
from functools import reduce
#
a = [1,3,4,4]
s = list(map(lambda x:x+3,a))
print(s)
#
# f = list(filter(lambda x:(x==3),a))
# print(f)
#
# import functools
#
# # initializing list
# lis = [1, 3, 5, 6, 2, ]
#
# # using reduce to compute sum of list
# print("The sum of the list elements is : ", end="")
# print(functools.reduce(lambda a, b: a + b, lis))
#
# # using reduce to compute maximum element from list
# print("The maximum element of the list is : ", end="")
# print(functools.reduce(lambda a, b: a if a > b else b, lis))

# DEEP COPY
# import copy
# s = [1,3,5,6,8,4,6]
# scp =copy.copy(s)
# print(s)
# print(scp)
# scp[1]=100
# print(s,scp)
#
# print('-----------------------------------------')
# d= [2,4,5,6,44,7]
# dcp = copy.deepcopy(d)
# print(d)
# print(dcp)
# d.append(9)
# print(d)
# print(dcp)
