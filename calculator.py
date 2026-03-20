
# calculator

import customtkinter as ctk

ctr = ctk.CTk()
ctr.title("Сalculator Pro")
ctr.geometry("300x450")
ctr.resizable(False, False)

# natija oynasi
entry = ctk.CTkEntry(ctr, width=275, height=60, font=("Segoe UI",30), justify="right")
entry.pack(pady=15)

#tugmalar bosilganda ishlaydigan funksiya
def button_click(value):
    if value == "C":
        entry.delete(0, "end")
    elif value == "⌫":
        entry.delete(len(entry.get())-1, "end")
    elif value == "=":
        try:
         result = eval(entry.get())
         entry.delete(0, "end")
         entry.insert(0, str(result))
        except:
            entry.delete(0, "end")
            entry.insert(0, "Error")
    else:
        if value not in ["+", "-", "*", "/", "="]:
            entry.insert("end", value)
        else:
            endy = entry.get()[-1]
            if endy not in ["+", "-", "*", "/", "=","."]:
              entry.insert("end", value)
# kaviaturadagi tugmalarni ishlatish

def key_press(event):
    key = event.keysym
    char = event.char

    if char.isdigit():
        entry.insert("end", char)
        return "break"

    elif key in ["plus", "KP_Add"]:
         entry.insert("end", "+")
         return "break"

    elif key in ["minus", "KP_Subtract"]:
         entry.insert("end", "-")
         return "break"

    elif key in ["asterisk", "KP_Multiply"]:
          entry.insert("end", "*")
          return "break"

    elif key in ["slash", "KP_Divide"]:
         entry.insert("end", "/")
         return "break"

    elif key == "Return":  # Enter
         button_click("=")
         return "break"

    elif key == "BackSpace":
         button_click("⌫")
         return "break"

    elif key == "Escape":
         button_click("C")
         return "break"

    elif key in ["period", "KP_Decimal"]:
         entry.insert("end", ".")
         return "break"

#tugmalar
buttons = [
    ["C", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".",".",  "=",]
]

#frame
frame = ctk.CTkFrame(ctr)
frame.pack()


for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text in ["+","-","*","/","=","%"]:
            color = ("#1E1E1E") #toq kulrang
            text_color = "white"
        elif text in["C","⌫"]:
            color = ("#FF4500") #qizil
            text_color = "white"
        else:
            color = ("#4CAF50") # yashil (raqamlar uchun)
            text_color="white"
            hover_color = "#66BB6A" # yashil
        btn = ctk.CTkButton(frame,command=lambda t=text: button_click(t),

                text = text           ,
                width=60,
                height=60,
                font=("Segoe UI", 30),
                fg_color = color,
                text_color = text_color,
                hover_color = "#333333")

        btn.grid(row=i, column =j, pady=5, padx= 3)

#kalaviatura eventini ulash

ctr.bind("<Key>", lambda e: "break")

ctr.mainloop()
