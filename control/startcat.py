import tkinter as tk
from PIL import ImageTk, Image

def start_cat():
  root = tk.Tk()
  root.attributes("-fullscreen", True)

  img = ImageTk.PhotoImage(Image.open("cat.jpg"))
  panel = tk.Label(root, image = img).pack()

  root.mainloop()