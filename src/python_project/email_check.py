email = input("please enter the email") # d@g.com
k,j=0,0

if len(email)>=6:
    if email[0].isalnum():
        if "@" in email and email.count("@")==1:
            if (email[-4]==".") ^ (email[-3]==".") ^ (email[-2]==".") :
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i == "_" or i == "." or i == "@":
                        continue
                    elif i==i.isdigit():
                        continue


                if k==1 :
                   print(" email has space value:5")
                # elif  l==1:
                #    print(" other condition not full fill:7")
                elif j==1:
                   print(" email has anathor special char:6")

                else:
                    print("ok")
            else:
                print("email have not proper with ' . '': 4")
        else:
            print("email has no @ value: 3")
    else:
        print("email is not start with alphanumaric :2")
else:
    print("email is wrong length not properc: 1")
