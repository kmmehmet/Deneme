
import tkinter as tk


window = tk.Tk()
window.title("4 İşlemli Hesap Makinesi")
window.geometry("300x300")


entry = tk.Entry(window, font=("Arial", 20), justify="right")
entry.pack(expand=True, fill="both")


keypad = tk.Frame(window)
keypad.pack(expand=True, fill="both")


buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "0", ".", "=", "/"
]


def click(button):

    if button == "=":

        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(0, "Hatalı Giriş!")

    elif button == "C":

        entry.delete(len(entry.get())-1, tk.END)

    else:

        entry.insert(tk.END, button)


row = 0
col = 0
for button in buttons:

    command = lambda x=button: click(x)

    tk.Button(keypad, text=button, font=("Arial", 20), command=command).grid(row=row, column=col, sticky="NSEW")

    col += 1
    if col == 4:
        col = 0
        row += 1


tk.Button(keypad, text="C", font=("Arial", 20), command=lambda: click("C")).grid(row=4, column=0, columnspan=2, sticky="NSEW")

window.mainloop()
