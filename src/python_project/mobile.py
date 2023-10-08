mobile = input("please enter your mobile no")
if len(mobile)==10:
    for i in mobile:
        if i.isnumeric():
            print("number is of")

        else:
            print("no alpha ")

else:
    print(" wrong number ")