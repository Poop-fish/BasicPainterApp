from GT_imports import *
from GT_Ui_Management import *
import GT_Editor_Management 
from GT_CustomStyle import *
from tkinter import messagebox
from GT_Widgets import GTG 


#! ---------------------------Core Management--------------------------------
class BasicPaint:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Paint")
        self.root.geometry("1000x800")
        self.root.iconbitmap('Assets/Block.ico')
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
        self.radius = 90
        self.center_x = 110
        self.center_y = 600
        self.color_buttons = []
        self.shape_mode = None
        self.spin_speed = 50  
        self.is_spinning = True  
        self.image = None 
        self.tk_image = None  
        self.grid_visible = False 
        self.grid_spacing = 20  
        self.grid_lines = [] 
        root.configure(bg="#2b2b2b")
        
        apply_styles(root)
        create_ui_elements(self)
        
        # \\ Create a frame to act as the border //
        self.frame = GTG.Frame(self.root, bg="#7f7f7f", relief="sunken", borderwidth=10 , highlightbackground="black")
        self.frame.pack(side="top", fill="both", expand=True)
        
        self.canvas = tk.Canvas(self.frame, bg="white", highlightthickness=0 , cursor="cross")  #  \\ i Set highlightthickness to 0 to remove canvas's own border
        self.canvas.pack(fill="both", expand=True)

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)
        self.canvas.bind("<ButtonPress-1>", self.start_shape)
        self.canvas.bind("<Configure>", self.on_resize)

        self.spin_buttons()
    
    def toggle_bg_color(self):
        current_bg = self.root.cget("bg")
        new_bg = "#ffffff" if current_bg == "#2b2b2b" else "#2b2b2b"
        self.root.configure(bg=new_bg)
#! --------------------------- END of Core Management-------------------------------------
    
    def toggle_grid(self):
        """Toggle grid visibility on/off."""
        self.grid_visible = not self.grid_visible
        if self.grid_visible:
            self.toggle_grid_label = "Hide Grid"
            self.draw_grid()
        else:
            self.toggle_grid_label = "Show Grid"
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
            image = Image.new("RGBA", (canvas_width, canvas_height), "white")

        draw = ImageDraw.Draw(image)

        for item in self.canvas.find_all():
            item_type = self.canvas.type(item)
            coords = self.canvas.coords(item)

            if item_type == 'line':
                color = self.canvas.itemcget(item, "fill")
                if color == "white":
                    continue  
                width = int(float(self.canvas.itemcget(item, "width")))
                draw.line(coords, fill=color, width=width)

            elif item_type == 'oval':
                fill_color = self.canvas.itemcget(item, "fill") or None
                outline_color = self.canvas.itemcget(item, "outline") or None
                width = int(float(self.canvas.itemcget(item, "width")))

                draw.ellipse(coords, fill=fill_color, outline=outline_color, width=width)

            elif item_type == 'rectangle':
                fill_color = self.canvas.itemcget(item, "fill") or None
                outline_color = self.canvas.itemcget(item, "outline") or None
                width = int(float(self.canvas.itemcget(item, "width")))

                draw.rectangle(coords, fill=fill_color, outline=outline_color, width=width)

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
        popup = GTG.Toplevel(self.root , enable_hover=False)
        popup.title("Text Customization")
        popup.geometry("300x300")

        popup.columnconfigure(1, weight=1)  

        label_text = GTG.Label(popup, 
            text="Enter text:",
            relief="raised",
            borderwidth=10, 
            background="Gray",
            foreground="black",
        )
        label_text.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        entry_text = GTG.Entry(popup)
        entry_text.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        label_font_size = GTG.Label(popup, 
            text="Font size:",
            relief="raised",
            borderwidth=10, 
            background="Gray",
            foreground="black",
        )
        label_font_size.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        entry_font_size = GTG.Entry(popup)
        entry_font_size.insert(0, "20")  
        entry_font_size.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        def choose_color():
            color = colorchooser.askcolor()[1]
            if color:
                entry_color.delete(0, tk.END)  
                entry_color.insert(0, color)  

        label_font_color = GTG.Label(popup, 
            text="Font color:",
            relief="raised",
            borderwidth=10, 
            background="Gray",
            foreground="black", 
        )
        label_font_color.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        entry_color = GTG.Entry(popup)
        entry_color.insert(0, "black")
        entry_color.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        colors = ["red", "blue", "green", "yellow"] 
        toggle_flash(label_font_color, colors, 0)
        
        def choose_color():
            """Open custom color palette"""
            def on_color_selected(hex_color):
                entry_color.delete(0, tk.END)
                entry_color.insert(0, hex_color)
            color_picker = CustomColorPicker(color_callback=on_color_selected)
            color_picker.open_picker()

        color_button = GTG.Button(popup, text="Open Color Palette", command=choose_color)
        color_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        def on_add():
            text = entry_text.get()
            try:
                font_size = int(entry_font_size.get())
            except ValueError:
                GTG.showerror(popup, "Invalid Font Size", "Please enter a valid integer for the font size.")
                return
            font_color = entry_color.get() if entry_color.get() else "black"

            if not text:
                GTG.showerror(popup, "Empty Text", "Please enter some text.")
                return

            GTG.showinfo(popup, "Success", "Text added successfully!")

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

            popup.destroy() 
        
        add_button = GTG.Button(popup, text="Add Text", command=on_add)
        add_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10, sticky="ew")


#! --------------------------- Core Editor code for Editor Management--------------------------------
    def toggle_eraser(self):
        self.is_eraser = not self.is_eraser
        self.current_color = "white" if self.is_eraser else "black"
        if hasattr(self, 'eraser_button'):
            self.eraser_button.config(text="Drawing" if self.is_eraser else "Eraser")

    def change_color(self, color):
        GT_Editor_Management.change_color(self, color)

    def pick_color(self):
        GT_Editor_Management.pick_color(self)

    def update_brush_size(self, value):
        GT_Editor_Management.update_brush_size(self, value)

    def clear_canvas(self):
        GT_Editor_Management.clear_canvas(self)

    def new_canvas(self):
        GT_Editor_Management.new_canvas(self)

    def toggle_spin(self):
        """Toggle spinning animation."""
        self.is_spinning = not self.is_spinning
        if self.is_spinning:
            self.toggle_spin_label = "Stop Spin"
            self.spin_buttons()  
        else:
            self.toggle_spin_label = "Start Spin"

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
