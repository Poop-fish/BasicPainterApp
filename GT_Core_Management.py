from GT_imports import *
from GT_Ui_Management import *
import GT_Widgets_Editor 
from GT_CustomStyle import *

#! -------------------------- Core Management --------------------------------------------------
class BasicPaint:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint App")
        self.root.geometry("800x600")
        self.current_color = "black"
        self.brush_size = 5
        self.last_x, self.last_y = None, None
        self.is_eraser = False
        self.shape_mode = None
        self.shape_start_x = None
        self.shape_start_y = None
        self.shape_current = None
        self.colors = ["black", "red", "green", "blue", "yellow", "orange", "pink", "purple", "brown", "gray"]
        self.current_angle = 0
        self.radius = 60
        self.center_x = 85
        self.center_y = 400
        self.color_buttons = []
        self.shape_mode = None
        self.spin_speed = 50  
        self.is_spinning = True  

        apply_styles(root)
        create_ui_elements(self)

        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(side="top", fill="both", expand=True)

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)
        self.canvas.bind("<ButtonPress-1>", self.start_shape)

        self.spin_toggle_button = tk.Button(self.root, text="Stop Spin", command=self.toggle_spin)
        self.spin_toggle_button.pack(side="left", padx=5)
        
        # \\ slider widget in the main window //
        # self.speed_slider = ttk.Scale(self.root, from_=10, to=200, orient="horizontal", command=self.update_spin_speed)
        # self.speed_slider.set(self.spin_speed)
        # self.speed_slider.pack(side="left", padx=5)

        self.spin_buttons()

    def toggle_eraser(self):
        self.is_eraser = not self.is_eraser
        self.current_color = "white" if self.is_eraser else "black"
        if hasattr(self, 'eraser_button'):
            self.eraser_button.config(text="Drawing" if self.is_eraser else "Eraser")

    def change_color(self, color):
        GT_Widgets_Editor.change_color(self, color)

    def pick_color(self):
        GT_Widgets_Editor.pick_color(self)

    def update_brush_size(self, value):
        GT_Widgets_Editor.update_brush_size(self, value)

    def clear_canvas(self):
        GT_Widgets_Editor.clear_canvas(self)

    def new_canvas(self):
        GT_Widgets_Editor.new_canvas(self)

    def save_as_png(self):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        image = Image.new("RGB", (canvas_width, canvas_height), "white")
        draw = ImageDraw.Draw(image)

        for item in self.canvas.find_all():
            coords = self.canvas.coords(item)
            color = self.canvas.itemcget(item, "fill")
            if color == "white":
                continue
            width = self.canvas.itemcget(item, "width")
            width = int(float(width))
            draw.line(coords, fill=color, width=width)

        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

        if file_path:
            image.save(file_path)
            print(f"Image saved as {file_path}")

    def spin_buttons(self):
        """Update button positions for spinning animation."""
        if self.is_spinning: 
            for i, (button, angle) in enumerate(self.color_buttons):
                new_angle = angle + 5
                x = self.center_x + self.radius * math.cos(math.radians(new_angle))
                y = self.center_y + self.radius * math.sin(math.radians(new_angle))
                button.place(x=x - 15, y=y - 2)
                self.color_buttons[i] = (button, new_angle)
            self.root.after(self.spin_speed, self.spin_buttons)

    def toggle_spin(self):
        """Toggle spinning animation."""
        self.is_spinning = not self.is_spinning
        self.spin_toggle_button.config(text="Start Spin" if not self.is_spinning else "Stop Spin")
        if self.is_spinning:
            self.spin_buttons() 

    def update_spin_speed(self, value):
        """Update the spinning speed based on the slider value."""
        self.spin_speed = int(float(value))

    def start_shape(self, event):
        if self.shape_mode:
            self.shape_start_x = event.x
            self.shape_start_y = event.y
            self.shape_current = None

    def paint(self, event):
        """Handle shape drawing and freehand painting."""
        x, y = event.x, event.y
        if self.shape_mode:
            if self.shape_current:
                self.canvas.delete(self.shape_current)
            if self.shape_mode == 'circle':
                radius = int(math.sqrt((x - self.shape_start_x) ** 2 + (y - self.shape_start_y) ** 2))
                self.shape_current = self.canvas.create_oval(
                    self.shape_start_x - radius, self.shape_start_y - radius,
                    self.shape_start_x + radius, self.shape_start_y + radius,
                    outline=self.current_color, width=self.brush_size
                )
            elif self.shape_mode == 'square':
                side = max(abs(x - self.shape_start_x), abs(y - self.shape_start_y))
                self.shape_current = self.canvas.create_rectangle(
                    self.shape_start_x, self.shape_start_y,
                    self.shape_start_x + side, self.shape_start_y + side,
                    outline=self.current_color, width=self.brush_size
                )
        else:
            if self.last_x and self.last_y:
                draw_color = "white" if self.is_eraser else self.current_color
                self.canvas.create_line(
                    self.last_x, self.last_y, x, y, width=self.brush_size,
                    fill=draw_color, capstyle=tk.ROUND, smooth=tk.TRUE
                )
            self.last_x, self.last_y = x, y

    def reset(self, event):
        """Finalize the drawing (for freehand or shape drawing) and reset to freehand."""
        self.last_x, self.last_y = None, None
        if self.shape_mode and self.shape_current:
            self.shape_current = None
        self.shape_mode = None

    def set_shape_mode(self, shape):
        self.shape_mode = shape
        self.shape_start_x = self.shape_start_y = None
        self.shape_current = None
