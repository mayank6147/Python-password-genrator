import tkinter as tk
root = tk.Tk ()
root.title ("tk")
root.geometry ("600x200")
def test ():
    txtbox1.insert (tk.END, "1234")
def clear_text ():
    txtbox1.delete (0, tk.END)
def copy_text ():
    txt = txtbox1.get ()
    print (txt)
    root.clipboard_append (txt) # This is the process of copying to the clipboard
button1 = tk.Button (root, text = "output sample character", font = ("Meiryo UI", 18), command = test)
button1.pack (expand = 1)
txtbox1 = tk.Entry (font = ("Meiryo UI", 18), width = 30)
txtbox1.pack (expand = 1)
button2 = tk.Button (root, text = "clear text box", font = ("Meiryo UI", 18), command = clear_text)
button2.pack (expand = 1)
button3 = tk.Button (root, text = "Copy the text box", font = ("Meiryo UI", 18), command = copy_text)
button3.pack (expand = 1)
root.mainloop ()
