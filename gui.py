# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import numpy as np
from tkinter import *

main_window=Tk()
main_window.geometry('1100x600')

df=pd.read_excel('water-_2.xls')
df.sort_values(by='STATION CODE', ascending=True)

Independent=df[['STATION CODE']]
Dependent=df[['PH']]

X_train,X_test,Y_train,Y_test =train_test_split(Independent,Dependent,test_size=0.3)
rf=RandomForestRegressor()
model=rf.fit(np.array(X_train).reshape(-1,1),np.array(Y_train).reshape(-1,1))




Label(main_window , font=("Arial", 30),text="Water Quality Prediction Model" ,fg="white",bg="purple").pack(pady=20,)
Label(main_window , font=("Arial", 20),text="This Interface will inform whether any station in India has Polluted Water Bodies or not" , fg="black",bg="orange").pack(fill="x")
Label(main_window,font=("Arial", 20),text="Water Pollution in India \n is increasing at \n alarming rate" ,fg="white",bg="black").pack(side="left",fill="y")
Label(main_window,font=("Arial", 23),text="Enter Station Code for any Place in India in 4-digit number For eg 1148 (Ambika,Gujarat)" ,fg="white",bg="blue").pack(pady=40,fill="x")
my_no=Entry(main_window,font=("Arial", 19),width=50 ,borderwidth=6)
my_no.pack(pady=10)

def on_click():
    try:
        x=int(my_no.get())
        Result=np.array(rf.predict(np.array([[x]])))
        if Result>7.0 and Result <7.5:
            Label(main_window,text="Slightly Polluted \n\n P.H. is inbetween 7.0 and 7.5",font=("Copperplate Gothic Bold", 25)).pack()
        elif Result >7.5:
            Label(main_window ,text="Vigorously Polluted \n\n P.H. is greater than 7.5",font=("Copperplate Gothic Bold", 25)).pack()
        else :
            Label(main_window, text ="Not Polluted \n\n P.H is nearly about 7",font=("Copperplate Gothic Bold", 25)).pack()
    except:
        answer.config(text="Not a Number")
    

Button (main_window,font=("Copperplate Gothic Bold", 15), text = "Submit",foreground='green',command=on_click).pack(pady=20)



answer=Label(main_window,font=("Copperplate Gothic Bold", 25),text="",foreground='red')
answer.pack()





main_window.mainloop()