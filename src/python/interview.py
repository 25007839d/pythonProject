#
# def gen(n):
#     for i in range(1,n):
#
#      yield i
#
# object = gen(1000)
# print(next(object))
# print(next(object))
# print(next(object))
# for i in object:
#     if i==100:
#         break
#     print(i)

# # math matical decorator
# def deco(xxx):
#     def inner():
#         print("before deco value",xxx())
#         f = xxx()
#         if f<=100:
#             a=100-f
#             b=a+f
#             print("after deco value =",b)
#         else:
#             print("no change in deco value=",f)
#     return inner
# @deco
# def sum():
#     a=32
#     b=25
#     c=a+b
#     return c
#
# a= sum()

 # string decorator
# def uppe(u):
#     def inner():
#       a= u()
#       if a>0:
#           print (a+100)
#
#
#     return inner
#
# @uppe
# def strin():
#     a =10
#     b=20
#
#     return a+b
#
# b= strin()


#
#
# def hello_decorator(func):
#     def inner1(*args, **kwargs):
#         print("before Execution")
#
#         # getting the returned value
#         returned_value = func(*args, **kwargs)
#         print("after Execution")
#
#         # returning the value to the original frame
#         return returned_value
#
#     return inner1

#
# def hello_decorator(func):
#     def inner1(*args, **kwargs):
#         print("before Execution")
#
#         # getting the returned value
#         returned_value = func(*args, **kwargs)
#         print("after Execution")
#
#         # returning the value to the original frame
#         return returned_value
#
#     return inner1
#
#
# # adding decorator to the function
# @hello_decorator
# def sum_two_numbers(a, b):
#     print("Inside the function")
#     return a + b
#
#
# a, b = 1, 2
#
# # getting the value through return of the function
# print("Sum =", sum_two_numbers(a, b))

# code for testing decorator chaining
# def decor1(func):
# 	def inner():
# 		x = func()
# 		return x * x
# 	return inner
#
# def decor(func):
# 	def inner():
# 		x = func()
# 		return 2 * x
# 	return inner
#
# @decor1
# @decor
# def num():
# 	return 10

# print(num())

# lambda

# def sum1():
#     x=20
#
#     return (lambda n:x+n)
# a= sum1()
# print(a(10))

#filter

# a = [20,60,43,46,68]
# def high_marks(n):
#     if n>=33:
#         return False
#     else:
#         return True
# result = list(filter(high_marks,a))
#
# print(result)

#array
#
# from array import *
# a = array('b',[12,23,55,52])
# print(a)
# for i in a:
#     print(i)
# print(list(a))
# a.pop(2)
# print(a)

# word count


# s=list(input ("enter the string"))
# st = str(s)
# d={}
# for x in s:
#      if x in d. keys() :
#
#            d[x]= d[x]+1
#      elif x not in d. keys():
#            d[x] = +1
#
# try:
#     del d[' ']
# except:
#     print("blank string not available")
# print(d)

# max number

# x= [2,3,52,3,5,3]
# a = 0
# for i in x:
#
#     if i>a:
#         a=i
#     else:
#         pass
# print(a)

# n max number
# x = [32,2,30,4]
#
# a = 0
# b=0
# c=0
# for i in x:
#
#     if i>a:
#         b=a
#         a=i
#     elif i<a:
#         if i>b:
#             c=b
#             b=i
#         else:
#             c=i
#
# print(a)
# print(b)
# print(c)

# string is mutable
#
# def immu(a):
#
#     x=''
#     for i in a:
#
#         if i =='r':
#             x=x+'s'
#             pass
#
#         else:
#             x=x+i
#
#     return x
#
#
# a= immu('ram')
# print(a)
# print(type(a))
# str="as is my father"

# x= "ram"
# y= x.replace('r','xx')
# print(y)

# dictionary.
#
# a= {'ram':1,'shyam':2,'mohan':3}
# print(a.items())
# print(a.keys())
# print(a.get('ram'))
# a.c

# compheransion

# lst = [i+2 for i in range(20)]
# lst2 = [i for i in range(20) if i%2==0]
# lst3 = [i for i in range(11) if i%2==0 if i%3==0]
# print(lst)
# print(lst2)
# print(lst3)
# new_set = {i if i%2==0 else i*1000 for i in range(10)}
# print(new_set)


# dict1 = {k:v for k, v in lst}
# a= [1,5,3,5,23]
# b=['ss','sds','ssd','sde','dsx']
# # e = [54,555,585,85,88]
# # c= {'ram':2,'shyam':4}
# d={}
# e={}
# def itr(i):
#     for j in i:
#         return j
# print(d.fromkeys(a,itr(b)))
#
# x = dict(zip(a,b))
# print(x)
# for i in b:
#     d.update({'fdf':1})
#     c= dict(a)
# z=(zip(a,b,c))
# for i in z:
#     print(i)
# ds =dict(zip(a,b))
#
# print(ds)




# dict3 = {n:n*2 for n in range(20) if n%2==0}
# dict4 = {n:n*2 for n in range(20) if n%2==0 if n%3==0}
# list
# n=[10,33,52,21]
# a=len(n)
# print(a)
# list=[]
# for i in range(len(n)):
#     x=n[a-1]
#     list.append(x)
#     a=a-1
# print(list)
#
## dict
# a=['ram','shyam']
# b=[2,6]
# dis = {'ram':1,'shyam':3,'coo':''}
#
# di=dict(zip(a,b))
# print(di)
#
# print(di.keys())
# print(di.values())
# print(di.items())
# print(di.update({'sita':2}))# to update value
# print(di.setdefault('ram')) # to set default vlue if key not available the default value will null
# print(di.get('ram')) # to collect the value
#
# print(di.items())

# a = 'dushyant kumar'
# dic={}
# for i in a :
#     if  i in dic.keys():
#         dic[i]=dic[i]+1
#     else:
#         dic[i]=+1
#
# dic.pop(' ')
# print(dic)

# file handling
import pathlib
#. Write a program to check whether the given file exist or not. If it is available then print its content?


# File handling:
# 1. Write a program to check whether the given file exist or not. If it is available then print its
# content?
# path = (r"C:\Users\KAJAL\OneDrive\Desktop\New Text Document.txt")
# try:
#   file = open(path)
#   file1=file.read()
#   print(file1)
#
#
#
# except IOError:
#   print("File does not exists")



# 2. Write a function in Python to count and display the total number of words in a text file.

# file = open(path)
# file1=file.read()
# print(file1)
# char_count = len(file1)
# word_count = len(file1.split())
# print(word_count)
# print(char_count)






# 3. Write a function in Python to read lines from a text file. Your function should find and display
# the occurrence of the word "the"
# file = open(path)
# file1=file.read()
# split_file=(file1.split())
# print(split_file)
#
# dis={}
# for i in split_file:
#   if i in dis.keys():
#     dis[i]=dis[i]+1
#   else:
#     dis[i]=1
# print(dis)



# 4. Write a function in Python to count uppercase character in a text file.
# a=[]
# cou = 0
# for i in split_file:
#   upper=i[0]
#
#   if upper == upper.upper() :
#        a.append(upper) # 1st method
#        cou=cou+1 # 2nd method
#
#
# print(len(a))
# print(cou)



# 5. Write a function in Python to count words in a text file those are ending with alphabet "e".

# a=[]
# cou = 0
# for i in split_file:
#   l = len(i)
#   last_alp = i[l-1]
#
#
#   if last_alp == 'e' :
#        a.append(last_alp) # 1st method
#        cou=cou+1 # 2nd method
#
# print(len(a))
# print(cou)
# General:
# 1. What are types of arguments?
'''1. default arguments - def add(b=5,c=10):
 
2. keyword arguments - print (add(b=10,c=15,a=20))
3. positional arguments - def add(a,b,c):





# 2. What is decorator? Write a decorator to display function name and print start and end.
# 3. What is generator? Explain advantages. Write a generator for Fibonacci series.
# 4. What is difference between shallow copy and deepcopy?
# 5. How exception handling work in python?
# Very Important Programs:
# 1. Write a python program for count character from string after each character is changed.
# e.g. input = 'aaaabahhhhhaaa' output = a4b1a1h5a3
# 2. You have a list of N+1 integers between 1 and N. You know there’s at least one duplicate,
# but there might be more. For example, if N=3, your list might be 3, 1, 1, 3 or it might be 1, 3, 2, 2
# Print out a number that appears in the list more than once.'''

li = [2,3,5,3,2,2,4,4]
