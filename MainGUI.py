 
 
from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import Monitoring_Engine

from tkinter import messagebox, ttk

villagename=""

def center_window(w,h):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
def read_input():
    print("inside read_input")
    
 
    patient_name=textBox1.get()
    doctor_name=textBox2.get()
    doctor_mob=textBox3.get()
    Monitoring_Engine.read_thingspeak_data(patient_name,doctor_name,doctor_mob)

   
   
   
    

   

    
root=Tk()
root.configure(background='#6495ED')
root.title("PATIENT MONITORING SYSTEM THROUGH IOT")
center_window(800, 600)
image = Image.open("maintemp.JPG")

# Resize the image using resize() method
resize_image = image.resize((1200, 800))

img = ImageTk.PhotoImage(resize_image)

# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.pack()


username = Label(root,text = "PATIENT MONITORING SYSTEM", font=("Courier", 20,'bold'),fg='#f00',bg='#6495ED').place(x = 100,y = 40)


# code to create label 
label1 = Label(root,text = "Patient Name  ",bg='#6495ED',font=("Ariel", 10)).place(x = 140,y = 150)
label2 = Label(root, text = "Doctor Name : ",bg='#6495ED',font=("Ariel", 10)).place(x = 140,y = 210)  
label3 = Label(root, text = "Doctor Mobile No: ",bg='#6495ED',font=("Ariel", 10)).place(x = 140,y = 270)  

   


#code to insert textbox
textBox1 = tk.Entry(root, width = 30) 
textBox1.place(x = 350,y = 150,height=30)

textBox2 = tk.Entry(root, width = 30)
textBox2.place(x = 350,y = 210,height=30)

textBox3 = tk.Entry(root, width = 30)
textBox3.place(x = 350,y = 270,height=30) # N





#command=lambda: retrieve_input() >>> just means do this when i press the button
button=Button(root, height=1, width=20, font=("Ariel", 10,'bold'),text="START MONITORING", command=lambda: read_input()).place(x=150,y=350)

# Button for closing
exit_button = Button(root, height=1, width=13, font=("Ariel", 10,'bold'),text="Exit", command=root.destroy).place(x=470,y=350)

mainloop()

