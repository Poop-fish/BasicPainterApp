from GT_imports import *

class GTG:
    
    class Button(tk.Button): 
        def __init__(self, parent, enable_hover=True, bg=None, fg=None, hover_bg=None, hover_fg=None, frame=None, **kwargs):
            super().__init__(parent, **kwargs)
            
            # Default styles
            self.default_bg = "#7f7f7f"
            self.default_fg = "Black"
            self.default_hover_bg = "light gray"
            self.default_hover_fg = "white"
            self.default_frame = "ridge"  
            
            self.bg = bg if bg is not None else self.default_bg
            self.fg = fg if fg is not None else self.default_fg
            self.hover_bg = hover_bg if hover_bg is not None else self.default_hover_bg
            self.hover_fg = hover_fg if hover_fg is not None else self.default_hover_fg
            self.frame = frame if frame is not None else self.default_frame
            
            self.enable_hover = enable_hover
        
            self.configure(
                bg=self.bg,  
                fg=self.fg,   
                relief=self.frame, 
                font=("Arial", 12, "bold"), 
                activebackground="darkgray",  
                activeforeground="white",  
                borderwidth=10,
                highlightthickness=0, 
                pady=5, padx=10 
            )
            
            # Bind hover events if enabled
            if self.enable_hover:
                self.bind("<Enter>", self.on_hover) 
                self.bind("<Leave>", self.on_leave)

        def on_hover(self, event):
            """Change button appearance on hover."""
            if self.enable_hover:
                self.configure(bg=self.hover_bg, fg=self.hover_fg, relief="raised", borderwidth=10)  

        def on_leave(self, event):
            """Revert button appearance when not hovering."""
            if self.enable_hover:
                self.configure(bg=self.bg, fg=self.fg, relief=self.frame, borderwidth=10)  
        
        def toggle_text(self, new_text):
            """Change the button's text."""
            self.config(text=new_text)

    
    
    class Label(tk.Label):
        def __init__(self, parent, enable_hover=True, bg=None, fg=None, **kwargs):
            super().__init__(parent, **kwargs)
            
            self.default_bg = "#7f7f7f"
            self.default_fg = "Black"
            self.bg = bg if bg is not None else self.default_bg
            self.fg = fg if fg is not None else self.default_fg
            
            self.enable_hover = enable_hover
            self.configure(
                bg=self.bg,  
                fg=self.fg,  
                font=("Arial", 12),  
                borderwidth=5,  
                relief="sunken",  
                padx=10, pady=5  
            )
            
            if self.enable_hover:
                self.bind("<Enter>", self.on_hover)
                self.bind("<Leave>", self.on_leave)

        def on_hover(self, event):
            if self.enable_hover:
                self.configure(bg="#e0e0e0")  

        def on_leave(self, event):
            if self.enable_hover:
                self.configure(bg=self.bg)   
    
    
    class Frame(tk.Frame):
        def __init__(self, parent, enable_hover=True, bg=None, highlightbackground=None, **kwargs):
            super().__init__(parent, **kwargs)
            self.default_bg = "#d9d9d9"  
            self.default_highlight = "#a0a0a0"  

            self.enable_hover = enable_hover
            self.bg_color = bg if bg else self.default_bg
            self.highlight_color = highlightbackground if highlightbackground else self.default_highlight

            self.configure(
                bg=self.bg_color,
                relief="ridge",
                borderwidth=5,
                highlightthickness=2,
                highlightbackground=self.highlight_color
            )

            if self.enable_hover:
                self.bind("<Enter>", self.on_hover)
                self.bind("<Leave>", self.on_leave)

        def on_hover(self, event):
            if self.enable_hover:
                self.configure(bg="#c0c0c0", highlightbackground="#808080")

        def on_leave(self, event):
            if self.enable_hover:
                self.configure(bg=self.bg_color, highlightbackground=self.highlight_color)

    
    class Canvas(tk.Canvas):
        def __init__(self, parent, enable_hover=True, **kwargs):
            super().__init__(parent, **kwargs)
            self.enable_hover = enable_hover
            self.configure(
                bg="#d9d9d9",  
                bd=5,           
                relief="ridge", 
                width=300,      
                height=200      
            )
            if self.enable_hover:
                self.bind("<Enter>", self.on_hover)
                self.bind("<Leave>", self.on_leave)
        
        def on_hover(self, event):
            if self.enable_hover:
                self.configure(bg="#c0c0c0")  

        def on_leave(self, event):
            if self.enable_hover:
                self.configure(bg="#d9d9d9")  

        def draw_rectangle(self, x1, y1, x2, y2, **kwargs):
            """Draws a rectangle on the canvas."""
            return self.create_rectangle(x1, y1, x2, y2, **kwargs)

        def draw_text(self, x, y, text, **kwargs):
            """Draws text on the canvas."""
            return self.create_text(x, y, text=text, **kwargs)
    
    
    class Entry(tk.Entry):
        def __init__(self, parent, enable_hover=True, **kwargs):
            super().__init__(parent, **kwargs)
            self.enable_hover = enable_hover
            self.configure(
                bg="white",  
                fg="black",  
                font=("Arial", 12),  
                borderwidth=5,  
                relief="sunken",  
                insertbackground="black",  
                highlightthickness=2,  
                highlightbackground="#a0a0a0",  
                highlightcolor="#808080"  
            )
            if self.enable_hover:
                self.bind("<Enter>", self.on_hover)
                self.bind("<Leave>", self.on_leave)

        def on_hover(self, event):
            if self.enable_hover:
                self.configure(highlightbackground="#808080", highlightcolor="#505050")  

        def on_leave(self, event):
            if self.enable_hover:
                self.configure(highlightbackground="#a0a0a0", highlightcolor="#808080") 
    
    
    class Toplevel(tk.Toplevel):
        def __init__(self, parent, enable_hover=True, **kwargs):
            super().__init__(parent, **kwargs)

            self.default_bg = "#7f7f7f"
            self.default_highlight = "#a0a0a0"
            
            self.configure(
                bg=self.default_bg, 
                relief="ridge", 
                borderwidth=10, 
                highlightthickness=2,
                highlightbackground=self.default_highlight
            )

            self.enable_hover = enable_hover

            if self.enable_hover:
                self.bind("<Enter>", self.on_hover)
                self.bind("<Leave>", self.on_leave)

        def on_hover(self, event):
            """Hover effect: Change background color on mouse enter"""
            if self.enable_hover:
                self.configure(bg="#e0e0e0", highlightbackground="#808080")

        def on_leave(self, event):
            """Reset background color when mouse leaves"""
            if self.enable_hover:
                self.configure(bg=self.default_bg, highlightbackground=self.default_highlight)



    class Scale(tk.Scale):
        def __init__(self, parent, enable_hover=True, enable_click_effect=True, show_value=True, **kwargs):
            super().__init__(parent, **kwargs)

            self.default_bg = "#d9d9d9"
            self.default_fg = "black"
            self.default_highlight = "#a0a0a0"
            self.hover_bg = "#e0e0e0"
            self.hover_highlight = "#808080"
            self.click_bg = "#c0c0c0"
            self.click_highlight = "#606060"

            self.configure(
                bg=self.default_bg,
                fg=self.default_fg,
                relief="ridge",
                troughcolor="#cccccc",
                highlightthickness=2,
                highlightbackground=self.default_highlight,
                font=("Arial", 12),
                sliderrelief="raised",
                sliderlength=20,
                orient=tk.HORIZONTAL,
                showvalue=show_value  
            )

            self.enable_hover = enable_hover
            self.enable_click_effect = enable_click_effect

            if self.enable_hover:
                self.bind("<Enter>", self.on_hover)
                self.bind("<Leave>", self.on_leave)

            if self.enable_click_effect:
                self.bind("<ButtonPress-1>", self.on_click)
                self.bind("<ButtonRelease-1>", self.on_release)

        def on_hover(self, event):
            self.configure(bg=self.hover_bg, highlightbackground=self.hover_highlight)

        def on_leave(self, event):
            self.configure(bg=self.default_bg, highlightbackground=self.default_highlight)

        def on_click(self, event):
            self.configure(bg=self.click_bg, highlightbackground=self.click_highlight)

        def on_release(self, event):
            if self.enable_hover:
                self.configure(bg=self.hover_bg, highlightbackground=self.hover_highlight)
            else:
                self.configure(bg=self.default_bg, highlightbackground=self.default_highlight)

        def set_orientation(self, orientation):
            """Set the orientation of the Scale (horizontal or vertical)"""
            self.configure(orient=orientation)

        def set_colors(self, bg=None, fg=None, troughcolor=None, hover_bg=None, hover_highlight=None, click_bg=None, click_highlight=None):
            """Customize the colors of the Scale"""
            if bg:
                self.default_bg = bg
                self.configure(bg=bg)
            if fg:
                self.default_fg = fg
                self.configure(fg=fg)
            if troughcolor:
                self.configure(troughcolor=troughcolor)
            if hover_bg:
                self.hover_bg = hover_bg
            if hover_highlight:
                self.hover_highlight = hover_highlight
            if click_bg:
                self.click_bg = click_bg
            if click_highlight:
                self.click_highlight = click_highlight

        def toggle_value_display(self, show_value):
            """Toggle the display of the slider's value"""
            self.configure(showvalue=show_value)


    class MessageBox(tk.Toplevel):
        def __init__(self, parent, title, message, message_type="info", buttons=["OK"], **kwargs):
            super().__init__(parent, **kwargs)
            self.parent = parent
            self.title(title)
            self.message = message
            self.message_type = message_type
            self.buttons = buttons

            self.configure(bg="#7f7f7f", padx=20, pady=20)
            self.resizable(False, False)

            self.create_widgets()

        def create_widgets(self):
            message_label = GTG.Label(self, text=self.message, bg="#7f7f7f", fg="red", font=("Arial", 12))
            message_label.pack(pady=10)

            button_frame = GTG.Frame(self, bg="#7f7f7f" , enable_hover=False)
            button_frame.pack(pady=10)

            for button_text in self.buttons:
                button = GTG.Button(button_frame, text=button_text, command=lambda bt=button_text: self.on_button_click(bt) ,bg="red")
                button.pack(side=tk.LEFT, padx=5)

        def on_button_click(self, button_text):
            """Handle button clicks and close the message box."""
            self.destroy()
            return button_text

    # Helper methods for common message box types
    @staticmethod
    def showinfo(parent, title, message):
        """Display an info message box."""
        dialog = GTG.MessageBox(parent, title, message, message_type="info")
        parent.wait_window(dialog)

    @staticmethod
    def showerror(parent, title, message):
        """Display an error message box."""
        dialog = GTG.MessageBox(parent, title, message, message_type="error")
        parent.wait_window(dialog)

    @staticmethod
    def showwarning(parent, title, message):
        """Display a warning message box."""
        dialog = GTG.MessageBox(parent, title, message, message_type="warning")
        parent.wait_window(dialog)

    @staticmethod
    def askyesno(parent, title, message):
        """Display a yes/no confirmation dialog."""
        dialog = GTG.MessageBox(parent, title, message, buttons=["Yes", "No"])
        return dialog.on_button_click("Yes") if dialog.on_button_click("Yes") else False

    @staticmethod
    def askokcancel(parent, title, message):
        """Display an OK/Cancel confirmation dialog."""
        dialog = GTG.MessageBox(parent, title, message, buttons=["OK", "Cancel"])
        return dialog.on_button_click("OK") if dialog.on_button_click("OK") else False



    class Menu(tk.Menu):
        def __init__(self, parent, enable_hover=True, bg=None, fg=None, hover_bg=None, hover_fg=None, **kwargs):
            super().__init__(parent, **kwargs)

            self.default_bg = "#7f7f7f"
            self.default_fg = "Black"
            self.default_hover_bg = "light gray"
            self.default_hover_fg = "white"

            self.bg = bg if bg is not None else self.default_bg
            self.fg = fg if fg is not None else self.default_fg
            self.hover_bg = hover_bg if hover_bg is not None else self.default_hover_bg
            self.hover_fg = hover_fg if hover_fg is not None else self.default_hover_fg

            self.enable_hover = enable_hover

            self.configure(
                bg=self.bg,
                fg=self.fg,
                activebackground=self.hover_bg,
                activeforeground=self.hover_fg,
                relief="raised",
                font=("Arial", 12)
            )

            if self.enable_hover:
                self.bind("<Enter>", self.on_hover)
                self.bind("<Leave>", self.on_leave)

        def on_hover(self, event):
            if self.enable_hover:
                self.configure(bg=self.hover_bg, fg=self.hover_fg)

        def on_leave(self, event):
            if self.enable_hover:
                self.configure(bg=self.bg, fg=self.fg)

        def add_command(self, label, command=None, **kwargs):
            """Add a command to the menu."""
            super().add_command(label=label, command=command, **kwargs) 

        def add_cascade(self, label, menu=None, **kwargs):
            """Add a cascade menu."""
            super().add_cascade(label=label, menu=menu, **kwargs)  

        def add_separator(self):
            """Add a separator to the menu."""
            super().add_separator()  

        def add_checkbutton(self, label, command=None, **kwargs):
            """Add a checkbutton to the menu."""
            super().add_checkbutton(label=label, command=command, **kwargs)  

        def add_radiobutton(self, label, command=None, **kwargs):
            """Add a radiobutton to the menu."""
            super().add_radiobutton(label=label, command=command, **kwargs) 
    
    
    class Scrollbar(tk.Scrollbar):
        def __init__(self, parent, **kwargs):
            super().__init__(parent, **kwargs)
            self.configure(
                bg="#a0a0a0",
                troughcolor="#d9d9d9",
                relief="flat",
                borderwidth=2
        )
    
    
    class Listbox(tk.Listbox):
        def __init__(self, parent, enable_hover=True, bg=None, fg=None, **kwargs):
            super().__init__(parent, **kwargs)

            self.default_bg = "#ffffff"
            self.default_fg = "black"

            self.bg = bg if bg is not None else self.default_bg
            self.fg = fg if fg is not None else self.default_fg

            self.enable_hover = enable_hover

            self.configure(
                bg=self.bg,
                fg=self.fg,
                font=("Arial", 12),
                selectbackground="gray",
                selectforeground="white",
                relief="sunken",
                borderwidth=5
            )

            if self.enable_hover:
                self.bind("<Enter>", self.on_hover)
                self.bind("<Leave>", self.on_leave)

        def on_hover(self, event):
            if self.enable_hover:
                self.configure(bg="#f0f0f0")

        def on_leave(self, event):
            if self.enable_hover:
                self.configure(bg=self.bg)
    

    class Text(tk.Text):
        def __init__(self, parent, enable_hover=True, **kwargs):
            super().__init__(parent, **kwargs)
            self.enable_hover = enable_hover

            self.configure(
                bg="white",
                fg="black",
                font=("Arial", 12),
                wrap="word",
                borderwidth=5,
                relief="sunken",
                insertbackground="black",
                highlightthickness=2,
                highlightbackground="#a0a0a0",
                highlightcolor="#808080"
            )

            if self.enable_hover:
                self.bind("<Enter>", self.on_hover)
                self.bind("<Leave>", self.on_leave)

        def on_hover(self, event):
            if self.enable_hover:
                self.configure(highlightbackground="#808080", highlightcolor="#505050")

        def on_leave(self, event):
            if self.enable_hover:
                self.configure(highlightbackground="#a0a0a0", highlightcolor="#808080") 
    
    
    class StringVar(tk.StringVar):
        def __init__(self, value="", callback=None, **kwargs):
            super().__init__(**kwargs)
            self.set(value)
            self.callback = callback
            self.trace_add("write", self.on_change)

        def on_change(self, *args):
            if self.callback:
                self.callback(self.get())

        def bind_to_widget(self, widget):
            widget.configure(textvariable=self)

        def get_value(self):
            return self.get()

        def set_value(self, new_value):
            self.set(new_value)
    
    
    class BooleanVar(tk.BooleanVar):
        def __init__(self, value=False, callback=None, **kwargs):
            super().__init__(**kwargs)
            self.set(value)
            self.callback = callback
            self.trace_add("write", self.on_change)

        def on_change(self, *args):
            if self.callback:
                self.callback(self.get())

        def bind_to_widget(self, widget):
            widget.configure(variable=self)

        def get_value(self):
            return self.get()

        def set_value(self, new_value):
            self.set(bool(new_value))

#! -----------------------------------------------------------------------------------

class CustomColorPicker:
    def __init__(self, color_callback):
        self.color_callback = color_callback  
        self.current_color = (0, 0, 0)  
        self.shaded_color = (0, 0, 0)  
        self.color_display_label = None  
        self.crosshair_dot = None 

    def open_picker(self):
        """Open the custom color picker in a new window."""
        picker_window = tk.Toplevel()
        picker_window.title("Custom Color Picker")
        picker_window.geometry("500x600")
        picker_window.resizable(False, False)
        picker_window.configure(bg="#2b2b2b")
        color_frame = tk.Frame(picker_window, bd=10, relief="sunken", background="black")
        color_frame.pack(side="top", padx=20, pady=10)

        color_canvas = tk.Canvas(color_frame, width=200, height=200, bg="white", cursor="cross")
        color_canvas.pack()

        self.draw_color_square(color_canvas)
        self.crosshair_dot = color_canvas.create_oval(0, 0, 10, 10, fill="black")

        color_canvas.bind("<Button-1>", lambda event: self.on_color_pick(event, color_canvas))
        color_canvas.bind("<B1-Motion>", lambda event: self.on_drag(event, color_canvas))

        shade_label = GTG.Label(picker_window, text="Shade" , enable_hover=False)
        shade_label.pack(side="top", padx=20)

        shade_slider = GTG.Scale(picker_window, from_=0, to_=100, orient="horizontal", command=self.on_shade_change)
        shade_slider.set(100)
        shade_slider.pack(side="top", padx=20, pady=10)
        shade_slider.set_colors(bg="gray", fg="black", troughcolor="#b0b0b0", hover_bg="#d0d0d0", hover_highlight="#707070", click_bg="gray", click_highlight="#505050")

        self.color_display_label = ttk.Label(picker_window, text="Selected Color: #000000", font=("Helvetica", 10))
        self.color_display_label.pack(side="top", padx=20, pady=5)

        
        scrollable_frame = tk.Frame(picker_window,relief='sunken', borderwidth=10, background="black")
        scrollable_frame.pack(side="top", padx=75, pady=20, fill="both", expand=True)
        canvas = tk.Canvas(scrollable_frame)
        scrollbar = tk.Scrollbar(scrollable_frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y") 
        canvas.pack(side="left", fill="both", expand=True)

        button_frame = GTG.Frame(canvas)
        canvas.create_window((0, 0), window=button_frame, anchor="nw")

        header_label = GTG.Label(button_frame, text="Predefined Colors", font=("Helvetica", 12, "bold"), relief="sunken", borderwidth=10 , enable_hover=False)
        header_label.grid(row=0, column=0, columnspan=5, pady=10)

        predefined_colors = [
            ("#FF0000", "Red"), ("#00FF00", "Lime Green"), ("#0000FF", "Blue"),
            ("#FFFF00", "Yellow"), ("#FFA500", "Orange"), ("#800080", "Purple"),
            ("#FFC0CB", "Pink"), ("#008080", "Teal"), ("#000000", "Black"),
            ("#A52A2A", "Brown"),
            ("#8A2BE2", "BlueViolet"), ("#A52A2A", "Brown"), ("#DEB887", "BurlyWood"),
            ("#5F9EA0", "CadetBlue"), ("#7FFF00", "Chartreuse"), ("#D2691E", "Chocolate"),
            ("#FF7F50", "Coral"), ("#6495ED", "CornflowerBlue"), ("#DC143C", "Crimson"),
            ("#00FFFF", "Cyan"), ("#00008B", "DarkBlue"), ("#008B8B", "DarkCyan"),
            ("#B8860B", "DarkGoldenRod"), ("#A9A9A9", "DarkGray"), ("#006400", "DarkGreen"),
            ("#BDB76B", "DarkKhaki"), ("#8B008B", "DarkMagenta"), ("#556B2F", "DarkOliveGreen"),
            ("#FF8C00", "DarkOrange"), ("#9932CC", "DarkOrchid"), ("#8B0000", "DarkRed"),
            ("#E9967A", "DarkSalmon"), ("#8FBC8F", "DarkSeaGreen"), ("#483D8B", "DarkSlateBlue"),
            ("#2F4F4F", "DarkSlateGray"), ("#00CED1", "DarkTurquoise"), ("#9400D3", "DarkViolet"),
            ("#FF1493", "DeepPink"), ("#00BFFF", "DeepSkyBlue"), ("#696969", "DimGray"),
            ("#1E90FF", "DodgerBlue"), ("#B22222", "FireBrick"), ("#228B22", "ForestGreen"),
            ("#DCDCDC", "Gainsboro"), ("#FFD700", "Gold"), ("#DAA520", "GoldenRod"),
            ("#808080", "Gray"), ("#008000", "Green"), ("#ADFF2F", "GreenYellow"),
            ("#F0FFF0", "HoneyDew"), ("#FF69B4", "HotPink"), ("#CD5C5C", "IndianRed"),
            ("#4B0082", "Indigo"), ("#F0E68C", "Khaki"), ("#E6E6FA", "Lavender"),
            ("#7CFC00", "LawnGreen"), ("#FFFACD", "LemonChiffon"), ("#ADD8E6", "LightBlue"),
            ("#F08080", "LightCoral"), ("#D3D3D3", "LightGray"), ("#90EE90", "LightGreen"),
            ("#FFB6C1", "LightPink"), ("#FFA07A", "LightSalmon"), ("#20B2AA", "LightSeaGreen"),
            ("#87CEFA", "LightSkyBlue"), ("#778899", "LightSlateGray"), ("#B0C4DE", "LightSteelBlue"),
            ("#32CD32", "LimeGreen"), ("#FF00FF", "Magenta"), ("#800000", "Maroon"),
            ("#66CDAA", "MediumAquaMarine"), ("#0000CD", "MediumBlue"), ("#BA55D3", "MediumOrchid"),
            ("#9370DB", "MediumPurple"), ("#3CB371", "MediumSeaGreen"), ("#7B68EE", "MediumSlateBlue"),
            ("#00FA9A", "MediumSpringGreen"), ("#48D1CC", "MediumTurquoise"), ("#C71585", "MediumVioletRed"),
            ("#191970", "MidnightBlue"), ("#F5FFFA", "MintCream"), ("#FFE4E1", "MistyRose"),
            ("#FFDEAD", "NavajoWhite"), ("#000080", "Navy"), ("#808000", "Olive"),
            ("#6B8E23", "OliveDrab"), ("#FF6347", "Tomato"), ("#EE82EE", "Violet"),
            ("#D2691E", "Chocolate"), ("#FF4500", "OrangeRed"), 
            ("#8B0000", "DarkRed"), ("#4682B4", "SteelBlue")
        ]

        row, col = 1, 0
        for color_code, color_name in predefined_colors:
            color_button = tk.Button(button_frame, bg=color_code, text="", width=5, height=2,
                                     command=lambda color=color_code: self.on_color_pick_predefined(color))
            color_button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            if col > 4:
                col = 0
                row += 4

        button_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        close_button = GTG.Button(picker_window, text="Close", command=picker_window.destroy)
        close_button.pack(side="bottom", pady=10)

    def draw_color_square(self, canvas):
        """Draw a color square with a gradient.""" 
        for i in range(200):
            for j in range(200):
                r, g, b = self.get_color_for_square(i, j)
                canvas.create_line(i, j, i+1, j+1, fill=f"#{r:02x}{g:02x}{b:02x}", width=1)

    def get_color_for_square(self, x, y):
        """Simulate HSV-to-RGB color values for the square.""" 
        hue = x / 200.0
        saturation = y / 200.0
        value = 1.0  
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
            self.current_color = self.get_color_for_square(x, y)
            self.shaded_color = self.current_color  
            self.update_color_display()
            self.update_crosshair_position(x, y, canvas)

    def on_color_pick_predefined(self, color):
        """Handle selection from predefined colors.""" 
        self.current_color = self.hex_to_rgb(color)
        self.shaded_color = self.current_color  
        self.update_color_display()

    def on_shade_change(self, value):
        """Adjust shade based on slider value.""" 
        if isinstance(self.current_color, tuple):
            value = float(value)
            r, g, b = self.current_color
            factor = value / 100.0
            r, g, b = int(r * factor), int(g * factor), int(b * factor)
            self.shaded_color = (r, g, b)
            self.update_color_display()

    def hex_to_rgb(self, hex_code):
        """Convert HEX to RGB.""" 
        hex_code = hex_code.lstrip('#')
        return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

    def update_color_display(self):
        """Update the label to show the selected and shaded color.""" 
        if self.color_display_label:  
            hex_color = f"#{self.shaded_color[0]:02x}{self.shaded_color[1]:02x}{self.shaded_color[2]:02x}"
            self.color_display_label.config(text=f"Selected Color: {hex_color}")
            self.color_display_label.config(background=hex_color)  
            self.color_callback(hex_color)  

    def update_crosshair_position(self, x, y, canvas):
        """Update the position of the crosshair dot.""" 
        canvas.coords(self.crosshair_dot, x-5, y-5, x+5, y+5)  #  \\ Adjust to center the dot on the click position

    def on_drag(self, event, canvas):
        """Handle dragging the crosshair dot.""" 
        x, y = event.x, event.y
        if x < 200 and y < 200:
            self.update_crosshair_position(x, y, canvas)
            self.on_color_pick(event, canvas) 

