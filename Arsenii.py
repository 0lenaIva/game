from tkinter import *

root  = Tk()

def btn_click():
    answer = input_.get()
    clear_entry()
    if answer == '4':
        message.configure(text="ok!")
    else:
        message.configure(text=":(")
        
def clear_entry():
    input_.delete(0, END)    
    
root['bg'] = '#fafafa'
root.title('title')
#root.wm_attributes('-alpha',0.7)
root.geometry('400x700')
#root.resizable(width=False, height = False)

canvas = Canvas(root, height = 700, width = 400)
canvas.pack()

frame = Frame(root, bg = '#fafafa')
frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

title = Label(frame, text="2 + 2 = ", bg = "#fafafa", font=35)
title.place(relx = 0.5, rely = 0.1, anchor = CENTER)

message = Label(frame,text=" ", bg = "#fafafa", font = 35)
message.place(relx = 0.5, rely = 0.2, anchor = CENTER)

input_ = Entry(frame, bg = 'white', width = 50)
input_.place(relx = 0.5, rely = 0.4, anchor = CENTER)



btn = Button(frame, text="SUBMIT", bg="grey", font = 35, command = btn_click)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)



root.mainloop()
