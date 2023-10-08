def fac(fun):
    print("1")

    def inner(a):
        print("factorial2")
        add = fun(a)
        l = add
        c = 1
        while l > 0:
            c = c * l
            l = l - 1

        return c

    return inner


def odd_evn(fun):
    print("2")

    def inner(a):
        print("odd_even2")
        v = fun(a)
        if v % 2 == 0:
            print(v, "this is a even number")
        else:
            print(v, "this is a odd number")

    return inner


def deco(fun):
    print("3")

    def inner(a):
        print("deco3")
        print("***********************")
        fun(a)
        print("***********************")

    return inner


def has(fun):
    print("4")

    def inner(a):
        print("has4")
        print("########################")
        fun(a)
        print("########################")

    return inner


@has
@deco
@odd_evn
@fac
def add(a):
    print("this no is", a)
    return a


b = add(3)

