# print(range(1,6))
# for i in range(1,6):
#     print(i)
#
#
# import sys
# print(sys.getsizeof(i))
# print(sys.getsizeof(range(1,100)))

# list =[1,5,2,5,51,12,52]
#
# l= [a for a in list if a%2==0]
# print(l)
#
# l1 =[(lambda x :x*2) (a) for a in list if a%2==0  ]
# print(l1)

# import add_fun
# a=add_fun.add(10,20)
# print(a)

# Python program to illustrate--------------------------------
# enumerate function
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print ("Return type:", type(obj1))
print (list(enumerate(l1)))

# changing start index to 2 from 0
print (list(enumerate(s1, 1)))
