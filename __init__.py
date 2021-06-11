#Imports
import tkinter as tk
import gui_txt_text
import numpy as np
import MLM
import UI

#Keywords
"""
wd = window     bp = BloodPressure
fr = frame      txt = Text
lbl = label
btn = button
ent = entry
gls = glucose
"""
#-------------------------------------------------------------------
#Events: Buttons
def open_Help():
    wd_help = tk.Toplevel(wd_main)
    fr_help = tk.Frame(wd_help, bg="grey")
    fr_help.configure(bg="grey")
    txt_help = tk.Label(fr_help, text=gui_txt_text.txt_help_text, anchor="w", justify="left")

    fr_help.grid()
    txt_help.grid()

def open_About():
    wd_about = tk.Toplevel(wd_main)
    fr_about = tk.Frame(wd_about)
    fr_about.configure(bg="grey")
    txt_about = tk.Label(fr_about, text=gui_txt_text.txt_about_text, anchor="e", justify="left")

    fr_about.grid()
    txt_about.grid()

def open_Info():
    wd_info = tk.Toplevel(wd_main)
    fr_info = tk.Frame(wd_info)
    fr_info.configure(bg="grey")
    txt_info = tk.Label(fr_info,
    text=gui_txt_text.txt_info_text,
    anchor="w", justify="left"
)

    fr_info.grid()
    txt_info.grid()
#-------------------------------------------------------------------
#Events: functions
def send_retrieve(event):
    gui_age = ent_age.get()
    gui_bmi = ent_bmi.get()
    gui_gls = ent_gls.get()
    gui_bp = ent_bp.get()
    age = UI.Age(gui_age)
    bmi = UI.BMI(gui_bmi)
    gls = UI.Glucose(gui_gls)
    bp = UI.BloodPressure(gui_bp)
    if age == False:
        lbl_result["text"] = f"{gui_txt_text.lbl_result_text}\nInvalid value for age"
    elif bmi == False:
        lbl_result["text"] = f"{gui_txt_text.lbl_result_text}\nInvalid value for BMI"
    elif gls == False:
        lbl_result["text"] = f"{gui_txt_text.lbl_result_text}\nInvalid value for glucose levels"
    elif bp == False:
        lbl_result["text"] = f"{gui_txt_text.lbl_result_text}\nInvalid value for blood pressure"
    else:
        MLM.userData = [[age,bmi,gls,bp]]
        MLM.fitting()#creates and trains the model
        result = MLM.prediction()#obtains a prediction
        lbl_result["text"] = f"{gui_txt_text.lbl_result_text}\n\nResult: {result}%\nThank you for using my app!"#displays the result

#-------------------------------------------------------------------
#Main window
wd_main = tk.Tk(className="Type-2 diabetes test")
wd_main.configure(bg="black")
fr_main = tk.Frame(bg="grey")
lbl_result = tk.Label(master=fr_main,
    text= gui_txt_text.lbl_result_text,
    fg="white",
    bg="black",
    width=40,
    height=10,
    anchor="nw", justify="left"
)
fr_main_btn = tk.Frame(bg="grey")
##Age
lbl_age = tk.Label(master=fr_main, text="Age",bg="grey",fg="black")
ent_age = tk.Entry(master=fr_main,
    fg="black",
    bg="white",
    width=20
)
##BMI
lbl_bmi = tk.Label(master=fr_main, text="BMI",bg="grey",fg="black")
ent_bmi = tk.Entry(master=fr_main,
    fg="black",
    bg="white",
    width=20
)
##Glucose
lbl_gls = tk.Label(master=fr_main, text="Glucose",bg="grey",fg="black")
ent_gls = tk.Entry(master=fr_main,
    fg="black",
    bg="white",
    width=20
)
##BloodPressure
lbl_bp = tk.Label(master=fr_main, text="Blood Pressure",bg="grey",fg="black")
ent_bp = tk.Entry(master=fr_main,
    fg="black",
    bg="white",
    width=20
)

##Buttons
btn_send = tk.Button(master=fr_main,
    text="Send",
    width=8,
    height=1,
    bg="black",
    fg="white",
)
#btn_send["command"] = send_retrieve()

btn_help = tk.Button(master=fr_main_btn,
    text="Help",
    width=8,
    height=1,
    bg="black",
    fg="White",
    command=open_Help
)
btn_about = tk.Button(master=fr_main_btn,
    text="About",
    width=8,
    height=1,
    bg="black",
    fg="White",
    command=open_About
)
btn_info = tk.Button(master=fr_main_btn,
    text="Type-2 diabetes",
    width=15,
    height=1,
    bg="black",
    fg="White",
    command=open_Info
)

#-------------------------------------------------------------------

def startup():
    #Output: Main window
    fr_main.grid()
    lbl_result.grid()
    ##Age
    lbl_age.grid(sticky="w")
    ent_age.grid(sticky="ew")
    ##BMI
    lbl_bmi.grid(sticky="w")
    ent_bmi.grid(sticky="ew")
    ##Glucose
    lbl_gls.grid(sticky="w")
    ent_gls.grid(sticky="ew")
    ##BloodPressure
    lbl_bp.grid(sticky="w")
    ent_bp.grid(sticky="ew")
    ##Buttons
    btn_send.grid()
    fr_main_btn.grid()
    btn_help.grid(row=0,column=1,padx=6.51,pady=3)
    btn_about.grid(row=0,column=2,padx=6,pady=3)
    btn_info.grid(row=0,column=3,padx=6.49,pady=3)
    btn_send.bind("<Button-1>", send_retrieve)

    wd_main.mainloop()

startup()
