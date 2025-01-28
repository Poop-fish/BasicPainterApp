from GT_imports import *
from GT_Ui_Management import *
import GT_Widgets_Editor 
from GT_CustomStyle import *
from tkinter import messagebox

#! ---------------------------Core Management--------------------------------
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
        self.center_x = 110
        self.center_y = 400
        self.color_buttons = []
        self.shape_mode = None
        self.spin_speed = 50  
        self.is_spinning = True  
        self.image = None 
        self.tk_image = None  
        self.grid_visible = False 
        self.grid_spacing = 20  
        self.grid_lines = [] 
        
        apply_styles(root)
        create_ui_elements(self)
        
        # \\ Create a frame to act as the border //
        self.frame = tk.Frame(self.root, bg="black", relief="sunken", borderwidth=10)
        self.frame.pack(side="top", fill="both", expand=True)
        self.canvas = tk.Canvas(self.frame, bg="white", highlightthickness=0)  #  \\ i Set highlightthickness to 0 to remove canvas's own border
        self.canvas.pack(fill="both", expand=True)

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)
        self.canvas.bind("<ButtonPress-1>", self.start_shape)
        self.canvas.bind("<Configure>", self.on_resize)


        self.spin_toggle_button = tk.Button(self.root, text="Stop Spin", command=self.toggle_spin)
        self.spin_toggle_button.pack(side="left", padx=5)
        
        self.grid_button = tk.Button(self.root, text="Show Grid", command=self.toggle_grid)
        self.grid_button.pack(side="left", padx=5)
        
        
        self.spin_buttons()
    
#! --------------------------- END of Core Management-------------------------------------
    def toggle_grid(self):
        """Toggle grid visibility on/off."""
        self.grid_visible = not self.grid_visible
        if self.grid_visible:
            self.grid_button.config(text="Hide Grid")
            self.draw_grid()
        else:
            self.grid_button.config(text="Show Grid")
            self.clear_grid()

    def draw_grid(self):
        """Draw grid lines on the canvas."""
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        self.clear_grid()

        for x in range(0, canvas_width, self.grid_spacing):
            line = self.canvas.create_line(x, 0, x, canvas_height, fill="#767676", dash=(4, 2))
            self.grid_lines.append(line)
        
        for y in range(0, canvas_height, self.grid_spacing):
            line = self.canvas.create_line(0, y, canvas_width, y, fill="#767676", dash=(4, 2))
            self.grid_lines.append(line)

    def clear_grid(self):
        """Clear all grid lines from the canvas."""
        for line in self.grid_lines:
            self.canvas.delete(line)
        self.grid_lines.clear()

    def on_resize(self, event):
        """Handle window resizing and adjust grid."""
        if self.grid_visible:
            self.clear_grid() 
            self.draw_grid()  


#! --------------------------- File Operations Management --------------------------------
    def load_image(self):
        """Load an image and display it on the canvas."""
        file_path = filedialog.askopenfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        
        if file_path:
            self.image = Image.open(file_path)
            self.image = self.image.convert("RGBA") 
            self.tk_image = ImageTk.PhotoImage(self.image)
            
            self.canvas.create_image(0, 0, anchor="nw", image=self.tk_image)
            
            print(f"Image loaded: {file_path}")


    def save_as_png(self):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        if self.image:
            image = self.image.copy()
        else:
            image = Image.new("RGB", (canvas_width, canvas_height), "white")

        draw = ImageDraw.Draw(image)

        for item in self.canvas.find_all():
            item_type = self.canvas.type(item)

            if item_type == 'line':
                coords = self.canvas.coords(item)
                color = self.canvas.itemcget(item, "fill")
                if color == "white":
                    continue  
                width = self.canvas.itemcget(item, "width")
                width = int(float(width))
                draw.line(coords, fill=color, width=width)

            elif item_type == 'oval' or item_type == 'rectangle':
                coords = self.canvas.coords(item)
                fill_color = self.canvas.itemcget(item, "fill")
                outline_color = self.canvas.itemcget(item, "outline")
                width = self.canvas.itemcget(item, "width")
                width = int(float(width))

                draw.line(coords[:2] + coords[2:], fill=outline_color, width=width)
                draw.rectangle([coords[0], coords[1], coords[2], coords[3]], outline=outline_color, fill=fill_color)

        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

        if file_path:
            try:
                image.save(file_path)
                print(f"Image saved as {file_path}")
            except Exception as e:
                print(f"Error saving image: {e}")
    
#! ---------------------------END of File Operations ------------------------------------------------
    def add_text(self):
        """Add text to the canvas with a customized pop-up."""
        popup = tk.Toplevel(self.root)
        popup.title("Text Customization")
        popup.geometry("300x300")

        label_text = tk.Label(popup, text="Enter text:")
        label_text.pack(pady=5)
        entry_text = tk.Entry(popup)
        entry_text.pack(pady=5)

        label_font_size = tk.Label(popup, text="Font size:")
        label_font_size.pack(pady=5)
        entry_font_size = tk.Entry(popup)
        entry_font_size.insert(0, "20")  
        entry_font_size.pack(pady=5)

        def choose_color():
            color = colorchooser.askcolor()[1]
            if color:
                entry_color.delete(0, tk.END)  
                entry_color.insert(0, color)  

        label_font_color = tk.Label(popup, text="Font color:")
        label_font_color.pack(pady=5)
        entry_color = tk.Entry(popup)
        entry_color.pack(pady=5)

        color_button = tk.Button(popup, text="Pick Color", command=choose_color)
        color_button.pack(pady=5)

        def on_add():
            text = entry_text.get()
            try:
                font_size = int(entry_font_size.get())
            except ValueError:
                messagebox.showerror("Invalid Font Size", "Please enter a valid integer for the font size.")
                return
            font_color = entry_color.get() if entry_color.get() else "black"
            
            if not text:
                messagebox.showerror("Empty Text", "Please enter some text.")
                return

            x = self.canvas.winfo_width() / 2
            y = self.canvas.winfo_height() / 2
            text_id = self.canvas.create_text(x, y, text=text, font=("Arial", font_size), fill=font_color)

            offset_x, offset_y = 0, 0

            def on_press(event):
                nonlocal offset_x, offset_y
                bbox = self.canvas.bbox(text_id)
                offset_x = event.x - bbox[0]
                offset_y = event.y - bbox[1]

            def on_drag(event):
                self.canvas.coords(text_id, event.x - offset_x, event.y - offset_y)

            self.canvas.tag_bind(text_id, "<ButtonPress-3>", on_press)
            self.canvas.tag_bind(text_id, "<B3-Motion>", on_drag)

            popup.destroy()  # Close the popup after adding text
        
        add_button = tk.Button(popup, text="Add Text", command=on_add)
        add_button.pack(pady=10)


#! --------------------------- Core Editor code for Editor Management--------------------------------
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
#! --------------------------- END --------------------------------
