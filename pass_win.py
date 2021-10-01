import tkinter as tk
import random
root= tk.Tk()
root.geometry("600x200")
def pass_word():
    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase="abcdefghijklmnopqrstuvwxyz"
    number="1234567890"
    special="!@#$%^&*()<>,._/\|-+{}[]"
    p1="".join(random.sample(uppercase,k=4))
    p2="".join(random.sample(lowercase,k=4))
    p3="".join(random.sample(number,k=4))
    p4="".join(random.sample(special,k=4))
    password=p1+p2+p3+p4
    password="".join(random.sample(password,k=len(password)))
    return password
def get_pass():
    password=pass_word()
    txtbox1.delete(0,tk.END)
    txtbox1.insert(tk.END,password)
def clear_text():
    txtbox1.delete(0,tk.END)
def copy_text():
    txt=txtbox1.get()
    root.clipboard_append(txt)
button1 = tk.Button(root,text="output password" , font = ("Meiryo UI", 18), command = get_pass)
button1.pack(expand=1)
txtbox1 = tk.Entry( font = ("Meiryo UI", 18),width=30)
txtbox1.pack (expand = 1)
button2 = tk.Button (root, text = "clear text box", font = ("Meiryo UI", 18), command = clear_text)
button2.pack (expand = 1)
button3 = tk.Button (root, text = "Copy the text box", font = ("Meiryo UI", 18), command = copy_text)
button3.pack (expand = 1)
root.mainloop ()
