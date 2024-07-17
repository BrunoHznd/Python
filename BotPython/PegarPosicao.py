import tkinter as tk

def show_coords(event):
    x = event.x
    y = event.y
    coords_label.config(text=f"X coords: {x}, Y coords: {y}")

root = tk.Tk()
root.geometry("300x300")

coords_label = tk.Label(root, text="")
coords_label.pack()

canvas = tk.Canvas(root, width=900, height=900, bg="white")
canvas.bind("<Motion>", show_coords)
canvas.pack()

root.mainloop()
