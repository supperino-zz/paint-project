from tkinter import *

class tool:
        #self.Canvas = Canvas
    def __init__(self, Canvas=None):
        self.x1_line_pt, self.y1_line_pt = None, None
        self.x2_line_pt, self.y2_line_pt = None, None
        self.left_but = "up"
        self.x_pos, self.y_pos = None, None

    def left_but_down(self, event=None):
        self.left_but = "down"
        self.x1_line_pt = event.x
        self.y1_line_pt = event.y
 
    def left_but_up(self, event=None):
        self.left_but = "up"
        self.x_pos,self.y_pos = None, None
        self.x2_line_pt = event.x
        self.y2_line_pt = event.y

class brush(tool):
    def motion(self, event=None):
            self.pencil_draw(event)

    def pencil_draw(self, event=None):
        if self.left_but == "down":
            if self.x_pos is not None and self.y_pos is not None:
                event.widget.create_line(self.x_pos, self.y_pos,event.x, event.y, smooth=TRUE)
            self.x_pos = event.x
            self.y_pos = event.y

class rectangle(tool):
    def left_but_down(self, event=None):
        self.left_but = "down"
        self.x1_line_pt = event.x
        self.y1_line_pt = event.y
 
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
            self.x2_line_pt, self.y2_line_pt,fill="midnight blue",outline="yellow",
            width=2)

class paint:
    def __init__(self, root):
        self.drawing_area = Canvas(root)
        self.drawing_area.pack()
        self.deftool = "rectangle"
        self.tool = tool(self.drawing_area)
        self.select_tool()

    def select_tool(self):
        if self.deftool == "rectangle" :
            self.tool = rectangle(self.drawing_area)
        else :
            self.tool = brush(self.drawing_area)
            self.drawing_area.bind("<Motion>", self.tool.motion)

        self.drawing_area.bind("<ButtonPress-1>", self.tool.left_but_down)
        self.drawing_area.bind("<ButtonRelease-1>", self.tool.left_but_up)

root = Tk()
paint_application = paint(root)
mainloop(
