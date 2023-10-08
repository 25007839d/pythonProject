def decode_fac(fac):
        inp = fac
        a=1
        for i in range (1,inp):
            a=1*a

            if inp == a:
                return i
            else:
                continue




def  factorial(inp):

        a= 1

        for i in range(1,(inp+1)):
            a = a*i
            print(a)

        return a

input1 = int(input("plz enter the factorial number"))

d = decode_fac(input1)
# a = factorial(input1)
print(d)