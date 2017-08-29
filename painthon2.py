from tkinter import *

class Tool:
    def __init__(self, Canvas=None):
        self.x1_line_pt, self.y1_line_pt = None, None
        self.x2_line_pt, self.y2_line_pt = None, None
        self.left_but = "up"
        self.right_but = "up"
        self.x_pos, self.y_pos = None, None

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

class Brush(Tool):
    def motion(self, event=None):
        self.pencil_draw(event)
        self.x_pos = event.x
        self.y_pos = event.y

    def pencil_draw(self, event=None):
        if self.left_but == "down":
            if self.x_pos is not None and self.y_pos is not None:
                event.widget.create_line(self.x_pos, self.y_pos,event.x, event.y, smooth=TRUE)

class Eraser(Tool):
    def motion(self, event=None):
        self.erase(event)
        self.x_pos = event.x
        self.y_pos = event.y

    def erase(self, event=None):
        if self.left_but == "down":
            if self.x_pos is not None and self.y_pos is not None:
                event.widget.create_line(self.x_pos, self.y_pos,event.x, event.y, smooth=TRUE, fill = "white", width = 20)

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
            self.x2_line_pt, self.y2_line_pt,fill="",outline="midnight blue",
            width=2)

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
            self.x2_line_pt, self.y2_line_pt,fill="", outline="midnight blue",
            width=2)            

class Paint:
    def __init__(self, root):
        self.drawing_area = Canvas(root, width=1000, height=500)
        self.drawing_area.pack()
        self.deftool = "eraser"
        self.tool = Tool(self.drawing_area)
        self.select_tool()

    def select_tool(self):
        if self.deftool == "rectangle" :
            self.tool = Rectangle(self.drawing_area)
        elif self.deftool == "brush" :
            self.tool = Brush(self.drawing_area)
            self.drawing_area.bind("<Motion>", self.tool.motion)
        elif self.deftool == "circle" :
            self.tool = Circle(self.drawing_area)
        else :
            self.tool = Eraser(self.drawing_area)
            self.drawing_area.bind("<Motion>", self.tool.motion)

        self.drawing_area.bind("<ButtonPress-1>", self.tool.left_but_down)
        self.drawing_area.bind("<ButtonRelease-1>", self.tool.left_but_up)

root = Tk()
paint_application = Paint(root)
mainloop()