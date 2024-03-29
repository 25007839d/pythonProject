from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 20")

def logout():
    os.system("shutdown -l")

def shutdown():
    os.system("shutdown /r /t 20")
st = Tk()
st.title("shut_down_app")
st.geometry("500x500")
st.config(bg="Blue")

r_button = Button(st,text="Restart",font=("Time New Roman",20,"bold"),relief = RAISED,cursor ="plus",command=restart)
r_button.place(x=150,y=60,height=50,width=200)

rt_button = Button(st,text="Restart Time",font=("Time New Roman",20,"bold"),relief = RAISED,cursor ="plus",command=restart_time)
rt_button.place(x=150,y=180,height=50,width=200)

lg_button = Button(st,text="Log-out",font=("Time New Roman",20,"bold"),relief = RAISED,cursor ="plus",command=logout)
lg_button.place(x=150,y=300,height=50,width=200)

sh_button = Button(st,text="shut down",font=("Time New Roman",20,"bold"),relief = RAISED,cursor ="plus",command=shutdown)
sh_button.place(x=150,y=420,height=50,width=200)

st.mainloop()
