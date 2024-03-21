from tkinter import * 

window = Tk()
window.title("Miles to KM converter")
window.config(padx=20,pady=20)

my_label = Label(text="Miles")
my_label.grid(column=2,row=0)
 
is_equal = Label(text="Is equals to")
is_equal.grid(column=0,row=1)
 
km_result = Label(text="0", font=("Arial",24))
km_result.grid(column=1,row=1)
 
km_label = Label(text="Km", font=("Arial",24))
km_label.grid(column=2,row=1)
 
def button_click():
    number = int(input.get())
    result = number * 1.609
    km_result.config(text=round(result,2))

calc_button = Button(text="Calculate",command=button_click)
calc_button.grid(column=1,row=2)

input = Entry(width=10)
input.grid(column=1,row=0)
 

window.mainloop()
 