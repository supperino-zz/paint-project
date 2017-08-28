from tkinter import *

class tools:
    def __init__(self, Canvas=None):
        self.Canvas = Canvas
        self.left_but = "up"
        self.x_pos, self.y_pos = None, None

    def left_but_down(self, event=None):
        self.left_but = "down"
        print(event.x, event.y)
 
    def left_but_up(self, event=None):
        self.left_but = "up"
        self.x_pos = None
        self.y_pos = None
 
    def motion(self, event=None):
            self.pencil_draw(event)
 
    def pencil_draw(self, event=None):
        if self.left_but == "down":
            if self.x_pos is not None and self.y_pos is not None:
                event.widget.create_line(self.x_pos, self.y_pos,event.x, event.y, smooth=TRUE)
            self.x_pos = event.x
            self.y_pos = event.y

class paint:
    def __init__(self, root):
        drawing_area = Canvas(root)
        drawing_area.pack()
        self.tools = tools(drawing_area)
        drawing_area.bind("<Motion>", self.tools.motion)
        drawing_area.bind("<ButtonPress-1>", self.tools.left_but_down)
        drawing_area.bind("<ButtonRelease-1>", self.tools.left_but_up)  

root = Tk()
paint_application = paint(root)
mainloop()
