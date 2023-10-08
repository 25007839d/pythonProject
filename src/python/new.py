# list = ['ram','shyam','sita']
# str = 'dushyany'
# num= 32514
# l= len(list)
# n_list = []
# # for reverse of list
# for i in range(len(list)):
#      n_list.append(list[l-1])
#      l=l-1
# print(n_list)
# print(list[::-1])

# armastrom number

# arm_num = int(input("plz enter the arm. number"))
# arm_num_s = str(arm_num)
# c = arm_num
# l = len(arm_num_s)
# b=0
# for i in range(l):
#     a= arm_num%10
#     b= b+(a*a*a)
#     arm_num=arm_num//10
#
# if b==c:
#     print("number is a armstrom number")
#
# else:
#     print("number is not an armstrom number")
#
# #---------------------------------while loop---------------------------------
# arm = 153
# cc=arm
# aa=0
# bb=0
#
# while arm>0:
#     aa=arm%10
#     bb=bb+(aa**3)
#     arm=arm//10
# if bb==cc:
#     print("number is a armstrom number")
#
# else:
#     print("number is not an armstrom number")

##factorial
# def factorial(n):
#         fac = n
#         a=1
#         while fac>1:
#             a=a*(fac)
#             fac=fac-1
#         print(a)
# num = int(input("plz enter the ............"))
# a=factorial(num)

##polondrom
# inp = 32
# c=inp
# rev = 0
# while inp >0:
#     rev=rev*10+inp%10
#     inp=inp//10
# if c==rev:
#     print('it is polondrom number')
# else:
#     print('it is not polondrom number')


# a = [i for i in range(10) ] , [i for i in range(10) if i%2==0]
# print(a)

#-----------------for loop --------------------------------------------
# inp1 = 121
# cc=inp1
# l = len(str(inp1))
# rev=0
# for i in range(l):
#     rev=rev*10+inp1%10
#     inp1=inp1//10
# if c == rev:
#     print('it is polondrom number')
# else:
#     print('it is not polondrom number')

## prme number
# def prime(num):
#     true=0
#     rem = 1
#     for i in range(2,num):
#          rem = num%i
#          if rem ==0:
#              true=0
#              break
#          else:
#              true=1
#     if true ==0:
#         print("it is not a prime num")
#     else:
#         print("it is a prime num")
#
# a = prime(10)
# print(a)

# if rem==0:
#     print("it is not a prime number")
# else:
#     print('it is a prime number')


## os module

# import os
# print(os.getcwd())
# # print(os.listdir(r'C:\Users\KAJAL\OneDrive\Desktop\Brainwork\Cloud'))
# print(os.chdir(r'C:\Users\KAJAL\OneDrive\Desktop\Brainwork\Cloud\SCD PROJECT\Dushyant\Raw_data_file'))
# print(os.getcwd())
# a=[]
# l_file =''
# for root,directory,file in os.walk(os.getcwd()):
#    for i in file:
#
#        a.append(i[11:21])
# latestfile = (max(a))
# print(latestfile)
#
# for root,directory,file in os.walk(os.getcwd()):
#     for  i in file:
#
#         if latestfile in i[11:21]:
#             l_file = i
#
# print(l_file)
# npath = r'C:\Users\KAJAL\OneDrive\Desktop\Brainwork\Cloud\SCD PROJECT\Dushyant\Raw_data_file' +"\\"+ l_file
# print(npath)
# a=os.listdir(r"C:\Users\KAJAL\OneDrive\Desktop\Brainwork\Cloud\SCD PROJECT\Dushyant\Raw_data_file")
# print(a)
# rdd=sc.parallelize(a)
# print(rdd.collect())
# #
# def date_extract (ele):
#     x = re.search("\d{4}_\d{2}_\d{2}",ele)
#     return x[0]
#
# rdd1=rdd.map(lambda x: date_extract(x))
# print(rdd1.collect())
# date_collect = (rdd1.sortBy(lambda x:x,ascending=False).collect()[0])
# print(date_collect)
# latest_file = rdd.filter(lambda x: date_extract(x) == date_collect).collect()[0]
# print(latest_file)
# dir=r"C:\Users\KAJAL\OneDrive\Desktop\Brainwork\Cloud\SCD PROJECT\Dushyant\Raw_data_file"
# #===

# list =[1,3,2,5,2,2]
# dic={}
# for i in range(len(list)):
#
#         dic[list[i]].append(list.index(list[i]))
#
#         # dic.update({list[i]:[list.index(list[i])]})
#
#
# print(dic)

# list = [1,3,5,1,4,3,2,2,5,3,5,]
# e=[]
# o=[]
# for i in list:
#     if i%2==0:
#         e.append(i)
#     else:
#         o.append(i)
# print(e,o)

# def smart_division(func):
#     def inner(a,b):
#         print("We are dividing",a,"with",b)
#         if b==0:
#             print("OOPS...cannot divide")
#             return
#         else:
#             return func(a*2,b)
#     return inner
# def smart_div(func):
#     def inner(a,b):
#         print("We are dividing",a,"with",b)
#         if b==0:
#             print("OOPS...cannot divide")
#             return
#         else:
#             return func(a+2,b+4)
#     return inner
#
# @smart_div
# @smart_division
# def division(a,b):
#      return a/b
#
# print(division(20,2))





