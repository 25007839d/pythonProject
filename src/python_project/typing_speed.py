from time import *
import random as r


def mistake(par_test,upa_test):
    error =0
    for i in range(len(par_test)):
        try:
            if par_test[i]!=upa_test[i]:
                error=error+1
        except:
            error=error+1
    return error

def speed_time(t_start,t_end,user_input):
    time_diff = round((t_end-t_start),2)
    speed = len(user_input)/time_diff
    return round(speed,2)



test = ["dhjbj","jjgyj","rttttttrt"]
test1 = r.choice(test)
print("*******Typing Speed*******")
print(test1)
print()
print()

time_1 = time()
testinput= input("enter")
time_2=time()

total_error = mistake(test1,testinput)
speed = speed_time(time_1,time_2,testinput)
print("word per second:",speed,"\n","total error :",total_error)