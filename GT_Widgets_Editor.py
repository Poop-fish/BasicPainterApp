from GT_imports import *
import GT_Widgets_Editor
import colorsys

#! ----------------Widget Classes --------------------------------

class CustomColorPicker:
    def __init__(self, color_callback):
        self.color_callback = color_callback  
        self.current_color = (0, 0, 0)  

    def open_picker(self):
        """Open the custom color picker in a new window."""
        picker_window = tk.Toplevel()
        picker_window.title("Custom Color Picker")
        picker_window.geometry("400x500")
        picker_window.resizable(False, False)

        color_canvas = tk.Canvas(picker_window, width=200, height=200, bg="white")
        color_canvas.pack(side="top", padx=20, pady=10)
        self.draw_color_triangle(color_canvas)

        shade_label = ttk.Label(picker_window, text="Shade")
        shade_label.pack(side="top", padx=20)
        shade_slider = ttk.Scale(picker_window, from_=0, to=100, orient="horizontal", command=self.on_shade_change)
        shade_slider.set(100)  
        shade_slider.pack(side="top", padx=20, pady=10)

        button_frame = tk.Frame(picker_window)
        button_frame.pack(side="top", pady=10)

        predefined_colors = [
            ("Red", "#FF0000"),
            ("Green", "#00FF00"),
            ("Blue", "#0000FF"),
            ("Yellow", "#FFFF00"),
            ("Orange", "#FFA500"),
            ("Purple", "#800080"),
        ]

        for color_name, color_code in predefined_colors:
            color_button = tk.Button(button_frame, text=color_name, bg=color_code, command=lambda color=color_code: self.on_color_pick_predefined(color))
            color_button.pack(side="left", padx=5, pady=5)

        close_button = ttk.Button(picker_window, text="Close", command=picker_window.destroy)
        close_button.pack(side="bottom", pady=10)

        color_canvas.bind("<Button-1>", lambda event: self.on_color_pick(event, color_canvas))

    def draw_color_triangle(self, canvas):
        """Draw a simple gradient to simulate the color triangle."""
        for i in range(200):
            for j in range(i, 200):
                r, g, b = self.get_color_for_triangle(i, j)
                canvas.create_line(i, j, i+1, j+1, fill=f"#{r:02x}{g:02x}{b:02x}", width=1)

    def get_color_for_triangle(self, x, y):
        """Simulate HSV-to-RGB color values."""
        hue = (x + y) % 360 / 360.0
        saturation = (x + 100) / 300.0
        value = (y + 100) / 300.0
        return self.hsv_to_rgb(hue, saturation, value)

    def hsv_to_rgb(self, h, s, v):
        """Convert HSV to RGB."""
        import colorsys
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        return int(r * 255), int(g * 255), int(b * 255)

    def on_color_pick(self, event, canvas):
        """Handle color selection from the canvas."""
        x, y = event.x, event.y
        if x < 200 and y < 200:
            self.current_color = self.get_color_for_triangle(x, y)
            self.color_callback(f"#{self.current_color[0]:02x}{self.current_color[1]:02x}{self.current_color[2]:02x}")

    def on_color_pick_predefined(self, color):
        """Handle selection from predefined colors."""
        self.current_color = self.hex_to_rgb(color)
        self.color_callback(color)

    def on_shade_change(self, value):
        """Adjust shade based on slider value."""
        if isinstance(self.current_color, tuple):
            value = float(value)
            r, g, b = self.current_color
            factor = value / 100.0
            r, g, b = int(r * factor), int(g * factor), int(b * factor)

            self.color_callback(f"#{r:02x}{g:02x}{b:02x}")

    def hex_to_rgb(self, hex_code):
        """Convert HEX to RGB."""
        hex_code = hex_code.lstrip('#')
        return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

#!------------ Editor Management --------------------------------
is_eraser = False
def paint(self, event):
    x, y = event.x, event.y
    if self.last_x and self.last_y:
        draw_color = "white" if is_eraser else self.current_color
        self.canvas.create_line(
            self.last_x, self.last_y, x, y, width=self.brush_size,
            fill=draw_color, capstyle=tk.ROUND, smooth=tk.TRUE
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

