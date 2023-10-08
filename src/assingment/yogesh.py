
#
# a=leng()
# d = {'a':1, 'b':2, 'a':4,'a':6}
# print(d)
# print(sorted(d))


# class Mobile():
#     def __int__(self):
#         self.model='moto'
#     def show(self):
#        print(self.model)
#
#
#
# a=Mobile()
# a.show()

a = input(('enter the number'))
add=0
for i in str(a):

    b = int(i)**3
    add = add + b
print(add,a)

if add == a:
    print('it is a palindrome')
else:
    print('it is not a palindrome')





