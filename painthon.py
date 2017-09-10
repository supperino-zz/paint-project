from tkinter import *

class Tool:
	def __init__(self, Canvas=None):
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

	def setColor(self):
		self.color = "red" #teste
		print("Mudou cor")
		print(self.color)

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

class Paint:
	def __init__(self):
		self.root = Tk()
		self.root.title("Painthon")
		self.frame = Frame(self.root, borderwidth = 1)
		self.frame.pack()
		self.drawing_area = Canvas(self.frame, borderwidth = 2, relief=SUNKEN, width=1000, height=500, background = "white")
		self.drawing_area.pack(side = RIGHT)
		self.tool = Tool(self.drawing_area)
		self.runGUI()

	def select_tool(self, x):
		if x == 1 :
			self.tool = Rectangle(self.drawing_area)
		elif x == 2 :
			self.tool = Brush(self.drawing_area)
		elif x == 3 :
			self.tool = Circle(self.drawing_area)
		else :
			self.tool = Eraser(self.drawing_area)
		self.tool.run(self.drawing_area)

	def runGUI(self):
		#self.brushicon = PhotoImage(file = "~/Pictures/brush.png")
		#self.erasericon = PhotoImage(file = "~/Pictures/eraser.png")

		brushbutton = Button(self.frame, text="Pincel", fg="black", command = lambda: self.select_tool(2))
		brushbutton.configure(width = 6)
		brushbutton.pack(side=TOP, anchor=NE)

		eraserbutton = Button(self.frame, text="Borracha", fg="black", command = lambda: self.select_tool(4))
		eraserbutton.configure(width=6)
		eraserbutton.pack(side=TOP, anchor=NE)

		retbutton = Button(self.frame, text="Retângulo", fg="black", command = lambda: self.select_tool(1))
		retbutton.pack(side=TOP, anchor=NE)
		retbutton.configure(width=6)

		cirbutton = Button(self.frame, text="Círculo", fg="black", command = lambda: self.select_tool(3))
		cirbutton.pack(side=TOP, anchor=NE)
		cirbutton.configure(width=6)

		'''redbutton = Button(self.frame, text="", bg = "red", command = self.tool.setColor)
		redbutton.pack(side=TOP, anchor=NE)
		redbutton.configure(width=3)'''

paint_application = Paint()
mainloop()
