from tkinter import *
from tkinter import filedialog
import subprocess
import os
import io
from PIL import Image

class Tool:
	def __init__(self):
		self.x1_line_pt, self.y1_line_pt = None, None
		self.x2_line_pt, self.y2_line_pt = None, None
		self.left_but = "up"
		self.right_but = "up"
		self.x_pos, self.y_pos = None, None
		self.color = "black"

	def left_but_down(self, event=None):
		self.left_but = "down"
		self.x1_line_pt = event.x
		self.y1_line_pt = event.y

	def right_but_down(self, event=None):
		self.right_but = "down"
		self.x1_line_pt = event.x
		self.y1_line_pt = event.y
 
	def left_but_up(self, event=None):
		self.left_but = "up"
		self.x_pos,self.y_pos = None, None
		self.x2_line_pt = event.x
		self.y2_line_pt = event.y

	def motion(self, event=None):
		self.x_pos = event.x
		self.y_pos = event.y

	def setColor(self, color):
		self.color = color

class Brush(Tool):
	def motion(self, event=None):
		self.pencil_draw(event)
		self.x_pos = event.x
		self.y_pos = event.y

	def pencil_draw(self, event=None):
		if self.left_but == "down":
			if self.x_pos is not None and self.y_pos is not None:
				event.widget.create_line(self.x_pos, self.y_pos,event.x, event.y, smooth=TRUE, fill = self.color)

	def run(self, canvas):
		canvas.bind("<Motion>", self.motion)
		canvas.bind("<ButtonPress-1>", self.left_but_down)
		canvas.bind("<ButtonRelease-1>", self.left_but_up)

class Eraser(Tool):
	def motion(self, event=None):
		self.erase(event)
		self.x_pos = event.x
		self.y_pos = event.y	

	def erase(self, event=None):
		if self.left_but == "down":
			if self.x_pos is not None and self.y_pos is not None:
				event.widget.create_line(self.x_pos, self.y_pos,event.x, event.y, smooth=TRUE, fill = "white", width = 20)

	def run(self, canvas):
		canvas.bind("<Motion>", self.motion)
		canvas.bind("<ButtonPress-1>", self.left_but_down)
		canvas.bind("<ButtonRelease-1>", self.left_but_up)


class Rectangle(Tool):
	def left_but_up(self, event=None):
		self.left_but = "up"
		self.x_pos,self.y_pos = None, None
		self.x2_line_pt = event.x
		self.y2_line_pt = event.y
		self.rectangle_draw(event)

	def rectangle_draw(self, event=None):
		if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt,
		self.y2_line_pt):
			event.widget.create_rectangle(self.x1_line_pt, self.y1_line_pt,
			self.x2_line_pt, self.y2_line_pt,fill="",outline=self.color,
			width=2)

	def run(self, canvas):
		canvas.bind("<ButtonPress-1>", self.left_but_down)
		canvas.bind("<ButtonRelease-1>", self.left_but_up)

class Circle(Tool):
	def left_but_up(self, event=None):
		self.left_but = "up"
		self.x_pos,self.y_pos = None, None
		self.x2_line_pt = event.x
		self.y2_line_pt = event.y
		self.circle_draw(event)

	def circle_draw(self, event=None):
		if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt,
		self.y2_line_pt):
			event.widget.create_oval(self.x1_line_pt, self.y1_line_pt,
			self.x2_line_pt, self.y2_line_pt,fill="", outline=self.color,
			width=2)

	def run(self, canvas):
		canvas.bind("<ButtonPress-1>", self.left_but_down)
		canvas.bind("<ButtonRelease-1>", self.left_but_up)

class Text(Tool):
	def __init__(self):
		self.entry = "primeiro"
		self.canvas = Canvas()

	def left_but_down(self, event=None):
		if (self.entry != "primeiro"):
			self.entry.destroy()
		self.right_but = "down"
		self.x1_line_pt = event.x
		self.y1_line_pt = event.y
		self.read_text(event)

	def display_text(self, event=None):
		texto = self.entry.get()
		self.canvas.create_text(self.x1_line_pt,self.y1_line_pt, anchor="nw", 
								font=("Arial",15), fill="black", text = texto)
		self.entry.destroy()

	def read_text(self, event=None):
		self.entry = Entry(event.widget,bd=0, font=("Arial",15), bg= "white", fg = "black")
		self.entry.place(x= event.x, y= event.y)
		self.entry.bind("<Return>", self.display_text)
		self.entry.focus_force()

	def run(self, canvas):
		canvas.bind("<ButtonPress-1>", self.left_but_down)
		self.canvas = canvas

class Paint:
	def __init__(self):
		self.root = Tk()
		self.root.title("Painthon")
		self.frame = Frame(self.root)
		self.frame.pack(side = LEFT, fill = BOTH)
		self.frame2 = Frame(self.root)
		self.frame2.pack(side = LEFT,  fill = BOTH)
		self.drawing_area = Canvas(self.root, borderwidth = 2, relief=SUNKEN, width=1000, height=500, background = "white")
		self.drawing_area.pack(side = RIGHT)
		self.tool = Tool()
		self.saveCounter = 1
		self.runGUI()


	def select_tool(self, x):
		if x == 1 :
			self.tool = Brush()
		elif x == 2 :
			self.tool = Eraser()
		elif x == 3 :
			self.tool = Rectangle()
		elif x == 4 :
			self.tool = Circle()
		else :
			self.tool = Text()
		self.tool.run(self.drawing_area)

	def makeColorButton(self, color, frame):
		colorbutton = Button(frame, text="", bg = color, command = lambda: self.tool.setColor(color))
		colorbutton.configure(width = 1, height = 1)
		colorbutton.pack(side=BOTTOM, anchor=SE)
		return colorbutton

	def makeToolButton(self, frame, x, image):
		toolbutton = Button(frame, command = lambda: self.select_tool(x))
		toolbutton.configure(image = image)
		toolbutton.pack(side=TOP, anchor=NE)
		return toolbutton
	
	def save(self):
		self.filename = filedialog.asksaveasfilename(initialdir = "~/",title = "Selecione diretorio",filetypes = (("arquivo jpeg","*.jpg"),("todos os arquivos","*.*")))
		ps = self.drawing_area.postscript(colormode='color')
		img = Image.open(io.BytesIO(ps.encode('utf-8')))
		img.save(self.filename)

	def runGUI(self):
		self.brushicon = PhotoImage(file = "Icons/brush.png")
		self.erasericon = PhotoImage(file = "Icons/eraser.png")
		self.circleicon = PhotoImage(file = "Icons/circle.png")
		self.recticon = PhotoImage(file = "Icons/rectangle.png")
		self.texticon = PhotoImage(file = "Icons/text.png")

		brushbutton = self.makeToolButton(self.frame, 1, self.brushicon)

		eraserbutton = self.makeToolButton(self.frame2, 2, self.erasericon)

		retbutton = self.makeToolButton(self.frame, 3, self.recticon)

		cirbutton = self.makeToolButton(self.frame2, 4, self.circleicon)

		textbutton = self.makeToolButton(self.frame, 5, self.texticon)

		redbutton = self.makeColorButton("red", self.frame)		

		bluebutton = self.makeColorButton("blue", self.frame2)	

		yellowbutton = self.makeColorButton("yellow", self.frame)		

		greenbutton = self.makeColorButton("green", self.frame2)		

		blackbutton = self.makeColorButton("black", self.frame)	

		whitebutton = self.makeColorButton("white", self.frame2)

		savebutton = Button(self.frame, text="Save", command = self.save)
		savebutton.configure(width = 1, height = 1)
		savebutton.pack(side=BOTTOM, anchor=SE)

paint_application = Paint()

mainloop()
