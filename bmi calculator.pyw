from tkinter import *
window = Tk()
window.configure(background="#b8f2e6")
window.title("BMI")
window.geometry("280x220")
window.resizable(False, False)
w_unit = "Kg"
h_unit = "cm"


def switch_weigth_unit():
	global w_unit
	if w_unit=="Kg" : 
		B1.config(background = "light salmon" , text=" lb ")
		w_unit = "lb"
	else : 
		B1.config(background = "light green" , text=" Kg ")
		w_unit = "Kg"


def switch_height_unit():
	global h_unit
	if h_unit=="cm" : 
		B2.config(background = "light salmon" , text="inch")
		h_unit = "inch"
	else : 
		B2.config(background = "light green" , text=" cm ")
		h_unit = "cm"


def check_input():
    try :
        w = int(E1.get())
        h = int(E2.get())
        E1.delete(0, 'end')
        E2.delete(0, 'end')
        calculate(w,h)
    except:
        E1.delete(0, 'end')
        E2.delete(0, 'end')
        L3.config(text="enter height & weigth truly" , fg = "#000000")


def calculate(w,h):
    if h_unit=="inch":
        h*=2.54
    if w_unit=="lb":
        w/=2.205
    BMI = (w/((h/100)**2))
    if BMI<18.5 :
        L3.config(text=f"your BMI is {BMI:.1f} (Under weigth)", fg = "#eba834")
    elif 18.5<BMI<=25:
        L3.config(text=f"your BMI is {BMI:.1f} (Normal)"      , fg = "#3cc279")
    elif 25<BMI<=30:
        L3.config(text=f"your BMI is {BMI:.1f} (Over weight)" , fg = "#ef476f")
    elif 30<BMI:
        L3.config(text=f"your BMI is {BMI:.1f} (Obese)"       , fg = "#d90429")


L1 = Label(window,text="weigth :" , background = "#b8f2e6")
L1.place(x=30 , y=15)
E1 = Entry(window,width=6)
E1.place(x=110 , y=15 , height=25)
B1 = Button(window , background = "light green" , text=" Kg ", command = switch_weigth_unit) 
B1.place(x=190 , y=15 , height=25 , width=50)
 

L2 = Label(window,text="height :" , background = "#b8f2e6")
L2.place(x=30 , y=55)
E2 = Entry(window,width=6)
E2.place(x=110 , y=55 , height=25)
B2 = Button(window , background = "light green" , text=" cm " , command = switch_height_unit) 
B2.place(x=190 , y=55 , height=25 , width=50) 
 

B3 = Button(window, background = "light grey" , text="calculate" , command = check_input) 
B3.place(x=100 , y=110 , height=40 ) 
L3 = Label(window,text="" , font = "Helvetica 13 bold" , background = "#b8f2e6")
L3.place(x=20 , y=170)


window.mainloop()