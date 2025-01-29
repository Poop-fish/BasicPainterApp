from GT_imports import *
import GT_Editor_Management

#!------------ Editor Management --------------------------------
def reset(self, event):
    self.last_x, self.last_y = None, None

def change_color(self, color):
    self.current_color = color

def pick_color(self):
    color_code = colorchooser.askcolor(title="Pick a Color")[1]
    if color_code:
        self.current_color = color_code

def update_brush_size(self, value):
    self.brush_size = int(float(value))
    self.brush_size_label.config(text=f"{self.brush_size}")

def clear_canvas(self):
    self.canvas.delete("all")

def new_canvas(self): 
    self.clear_canvas()


