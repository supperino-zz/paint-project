from tkinter import *
color = "#000000"

def red():
  global color
  color = "#ff0000"

def green():
  global color
  color = "#228b22"

def black():
  global color
  color = "#000000"

def blue():
  global color
  color = "#0000ff"

def draw(x1, y1, x2, y2):
  w.create_oval(x1, y1, x2, y2, fill=color, outline = color)

def motion(event):
  x1, y1 = (event.x), (event.y)
  x2, y2 = (event.x), (event.y)
  draw(x1, y1, x2, y2)
  return

master = Tk()
master.title("Painthon")

w = Canvas(master, width=1000, height=500)
w.bind('<B1-Motion>', motion)
w.pack()

bottomframe = Frame(master)
bottomframe.pack(side = BOTTOM)

redbutton = Button(bottomframe, text="Red", fg="red", command = red)
redbutton.pack(side = LEFT)

greenbutton = Button(bottomframe, text="Green", fg="green", command = green)
greenbutton.pack(side = LEFT)

bluebutton = Button(bottomframe, text="Blue", fg="blue", command = blue)
bluebutton.pack(side = LEFT)

blackbutton = Button(bottomframe, text="Black", fg="black", command = black)
blackbutton.pack(side = RIGHT)

mainloop()