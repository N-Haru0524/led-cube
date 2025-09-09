import tkinter as tk

root = tk.Tk()
root.title("Simple Tkinter Window")
root.geometry("300x200")

# labels
Static1 = tk.Label(text=u'test', foreground='#ff0000', background='#ffaacc')
Static1.place(x=150, y=228)

# Entry
EditBox = tk.Entry(width=50)
EditBox.insert(tk.END,"初期値")
EditBox.pack()

# get Entry value
value = EditBox.get()
print(value)

# delete Entry value
def DeleteEntryValue(event):
  #エントリーの中身を削除
  EditBox.delete(0, tk.END)

# button
button = tk.Button(text=u'削除')
button.bind("<Button-1>", DeleteEntryValue)
button.pack()

root.mainloop()