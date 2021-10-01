import random
from tkinter import *
from tkinter import ttk
root = Tk()
import random
def Uppercase(alen , uppercase):
    test=len(uppercase)
    while len(uppercase)<(test+alen):
        s="".join(random.sample(uppercase,k=len(uppercase)))
        uppercase+=s
            
    uppercase="".join(random.sample(uppercase,k=len(uppercase)))
    return uppercase  
    
def Lowercase(alen,lowercase):
    test=len(lowercase)
    while len(lowercase)<(test+alen):
        s="".join(random.sample(lowercase,k=len(lowercase)))
        lowercase+=s
            
    lowercase="".join(random.sample(lowercase,k=len(lowercase)))
    return lowercase

def Number(alen,number):
    test=len(number)
    while len(number)<test+alen:
        s="".join(random.sample(number,k=len(number)))
        number+=s
    number="".join(random.sample(number,k=len(number)))
    return number
def SpecialCharacter(alen,special):
    test=len(special)
    while len(special)< alen+test:
        s="".join(random.sample(special,k=len(special)))
        special+=s
    special="".join(random.sample(special,k=len(special)))
    return special

def genrator(n):
    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase="abcdefghijklmnopqrstuvwxyz"
    number="1234567890"
    #special="!@#$%^&*()<>,._/\|-+{}[]"
    special="@#$^&\%"
    diff=n-86
    each=diff//4
    p1=Uppercase(each,uppercase)
    p2=Lowercase(each,lowercase)
    p3=SpecialCharacter(each,special)
    p4=Number(each,number)
    total_char=p1+p2+p3+p4
    total_char="".join(random.sample(total_char,k=len(total_char)))
    print(len(total_char))
    password="".join(random.sample(total_char,k=n))
    return password
def main():
    len_pass=int(entry.get())
    password=genrator(len_pass)
    textbox.delete('1.0',END)
    textbox.insert(INSERT,password)
def clear():
    textbox.delete('1.0',END)
def copy():
    txt=textbox.get('1.0',END)
    root.clipboard_append (txt)
# frame
content = Frame(root)
frame = Frame(root,borderwidth=5)
#text area
textbox=Text(frame,font = ("Meiryo UI", 18))
textbox.grid(row=0,column=0)
txt="Enter length you want for your password"

#input label
label  = Label(content,text=txt)
label.grid(sticky=(NS))

#input length
entry  = Entry(content,width=20)
entry.grid(row=1,column=0)

#enter button
button = Button(content ,text="Enter",command=main)
button.grid(row=1,column=1)

#copy button
button_copy = Button(content,text="Copy",command=copy)
button_copy.grid(row=2,column=0)

#clear button
button_clear = Button(content,text="Clear",command=clear)
button_clear.grid(row=2,column=1)

content.grid(column=1,row=0)
frame.grid(row=0,column=0)
root.mainloop()
