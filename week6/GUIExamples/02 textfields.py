import tkinter as tk


def clicked():
    res = "Hello " + txt_input.get()
    output_var.set(res)


window = tk.Tk()
window.geometry("300x50")
window.title("GUI Example")

txt_input = tk.Entry(window, width=10)
txt_input.focus()
txt_input.grid(column=0, row=0)

btn = tk.Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)

output_var = tk.StringVar(window)
txt_output = tk.Entry(window, width=30, textvariable=output_var, state="readonly")
txt_output.grid(column=2, row=0)

window.mainloop()
