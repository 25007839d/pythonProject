import pickle
a={'a':7,'b':2}
f='pic1.pkl'
pickle.dump(a,open(f,'wb'))

p=pickle.load(open(f,'rb'))
print(p)

# print(dir({open})) # is a function through this we can see function , class required details not all detals

# split ---------------------

# st ='this is a split'
# print(st.split(' '))


# def asd (**x):
#     return x
#
# print(asd(a=4,b=3,f=5))