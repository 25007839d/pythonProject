from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down =str(round(sp.download()/(10**6),3))+ "Mbps"
    up = str(round(sp.upload()/(10**6),3))+ "Mbps"
    lab_down.config(text=down)


sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x600")
sp.config(bg="Green")


lab = Label(sp,text="Internet Speed Test",font=("Time New Roman",20,"bold"),bg="Blue",fg="Red")
lab.place(x=60,y=40,height=30,width=380)

Download_Speed = Label(sp,text="Download Speed",font=("Time New Roman",20,"bold"),bg="Blue",fg="Red")
Download_Speed.place(x=60,y=120)

s_00 = Label(sp,text="00",font=("Time New Roman",20,"bold"),bg="Blue",fg="Red")
s_00.place(x=60,y=220)

Upload_Speed = Label(sp,text="Upload Speed",font=("Time New Roman",20,"bold"),bg="Blue",fg="Red")
Upload_Speed.place(x=60,y=310)

s_00= Label(sp,text="00",font=("Time New Roman",20,"bold"),bg="Blue",fg="Red")
s_00.place(x=60,y=410)

button =Button(sp,text="CHECK SPEED",font=("Time New Roman",20,"bold"),relief=RAISED)
button.place(x=60,y=500,height=50,width=380)



sp.mainloop()
