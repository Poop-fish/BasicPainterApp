from GT_imports import *
import GT_Widgets_Editor
import colorsys

#! ----------------Widget Classes --------------------------------
class CustomColorPicker:
    def __init__(self, master, color_callback):
        self.master = master
        self.color_callback = color_callback
        self.current_color = (0, 0, 0)
        
        self.color_canvas = tk.Canvas(master, width=200, height=200, bg="white")
        self.color_canvas.pack(side="top", padx=20, pady=10)
        
        self.draw_color_triangle()
        
        self.color_canvas.bind("<Button-1>", self.on_color_pick)
        self.shade_label = ttk.Label(master, text="Shade") 
        self.shade_label.pack(side="top", padx=20)
        self.shade_slider = ttk.Scale(master, from_=0, to=100, orient="horizontal", command=self.on_shade_change)
        self.shade_slider.set(100)  
        self.shade_slider.pack(side="top", padx=20, pady=10)

    def draw_color_triangle(self):
        for i in range(200):
            for j in range(i, 200):
                r, g, b = self.get_color_for_triangle(i, j)
                self.color_canvas.create_line(i, j, i+1, j+1, fill=f"#{r:02x}{g:02x}{b:02x}", width=1)

    def get_color_for_triangle(self, x, y):
        hue = (x + y) % 360 / 360.0 
        saturation = (x + 100) / 300.0 
        value = (y + 100) / 300.0 
        return self.hsv_to_rgb(hue, saturation, value)

    def hsv_to_rgb(self, h, s, v):
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        return int(r * 255), int(g * 255), int(b * 255)

    def on_color_pick(self, event):
        x, y = event.x, event.y
        if x < 200 and y < 200:
            self.current_color = self.get_color_for_triangle(x, y) 
            self.color_callback(f"#{self.current_color[0]:02x}{self.current_color[1]:02x}{self.current_color[2]:02x}")

    def on_shade_change(self, value):
        if isinstance(self.current_color, tuple):
            value = float(value) 
            r, g, b = self.current_color 
            factor = value / 100.0 
            r, g, b = int(r * factor), int(g * factor), int(b * factor)
            
            if factor < 0.1:
                factor = 0.1
                r, g, b = int(r * factor), int(g * factor), int(b * factor)
            
            self.color_callback(f"#{r:02x}{g:02x}{b:02x}")
        else:
            print("Warning: current_color is not properly initialized.")

#!------------------- Editor Management --------------------------------

is_eraser = False
def paint(self, event):
    x, y = event.x, event.y
    if self.last_x and self.last_y:
        self.canvas.create_line(
            self.last_x, self.last_y, x, y, width=self.brush_size,
            fill=self.current_color, capstyle=tk.ROUND, smooth=tk.TRUE
        )
    self.last_x, self.last_y = x, y

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

