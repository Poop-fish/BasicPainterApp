from GT_imports import *
from GT_Ui_Management import *
import GT_Widgets_Editor 
from GT_CustomStyle import *

class BasicPaint:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint App")
        self.root.geometry("800x600")
        self.current_color = "black" 
        self.brush_size = 5
        self.last_x, self.last_y = None, None
        self.is_eraser = False
        self.colors = ["black", "red", "green", "blue", "yellow", "orange", "pink", "purple", "brown", "gray"]
        self.current_angle = 0  
        self.radius = 60
        self.center_x = 85  
        self.center_y = 400 
        self.color_buttons = []  
        
        apply_styles(root) 
        create_ui_elements(self)
        
        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(side="top", fill="both", expand=True)

        self.canvas.bind("<B1-Motion>", lambda event: GT_Widgets_Editor.paint(self, event))
        self.canvas.bind("<ButtonRelease-1>", lambda event: GT_Widgets_Editor.reset(self, event))
                

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
    
#! ---------------------File Operation Management --------------------   
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

#! ---------------------Spin Buttons Management --------------------   
    def spin_buttons(self):
        """Update button positions for spinning animation."""
        for i, (button, angle) in enumerate(self.color_buttons):
            new_angle = angle + 5  
            x = self.center_x + self.radius * math.cos(math.radians(new_angle))  
            y = self.center_y + self.radius * math.sin(math.radians(new_angle))  
            button.place(x=x - 15, y=y - 2)  
            self.color_buttons[i] = (button, new_angle)
        self.root.after(50, self.spin_buttons)
