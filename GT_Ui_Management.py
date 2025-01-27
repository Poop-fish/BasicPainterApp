from GT_imports import *
from GT_Widgets_Editor import *
from GT_CustomStyle import apply_styles 
#!--------------------------------------------------------------------------------------------------------------------------------


def create_menu(app):
    menu_bar = tk.Menu(app.root)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="New", command=app.new_canvas)
    file_menu.add_command(label="Exit", command=app.root.quit)
    file_menu.add_command(label="Save as PNG", command=app.save_as_png)
    menu_bar.add_cascade(label="File", menu=file_menu)

    edit_menu = tk.Menu(menu_bar, tearoff=0)
    edit_menu.add_command(label="Clear", command=app.clear_canvas)
    menu_bar.add_cascade(label="Edit", menu=edit_menu)

    
    settings_menu = tk.Menu(menu_bar, tearoff=0)
    settings_menu.add_command(
        label="Toggle Spin",
        command=app.toggle_spin
    )

    def show_speed_slider():
        slider_window = tk.Toplevel(app.root)
        slider_window.title("Adjust Spin Speed")
        slider_window.geometry("300x150")
        slider_window.config(bg="gray") 

        label = tk.Label(slider_window, text="Spin Speed Setting", fg="#1aff00", bg="Black", font=("Arial", 12, "bold"), relief="raised" , borderwidth=15)
        label.pack(pady=10)

    
        speed_slider = ttk.Scale(
            slider_window, from_=10, to=200, orient="horizontal", command=app.update_spin_speed, style="TScale"
        )
        speed_slider.set(app.spin_speed)
        speed_slider.pack(pady=10)

    settings_menu.add_command(label="Adjust Spin Speed", command=show_speed_slider)

    menu_bar.add_cascade(label="Settings", menu=settings_menu)

    app.root.config(menu=menu_bar)

#!--------------------------------------------------------------------------------------------------------------------------------

def create_sidebar(app):
    
    sidebar = ttk.Frame(app.root, width=200, height=600)
    sidebar.pack(side="left", fill="y", padx=10, pady=10)

    for i, color in enumerate(app.colors):
        angle = i * (360 / len(app.colors))  
        x = app.center_x + app.radius * math.cos(math.radians(angle))  
        y = app.center_y + app.radius * math.sin(math.radians(angle))  

        button = tk.Button(
            sidebar, width=3, height=1, command=lambda c=color: app.change_color(c)
        )
        button.configure(background=color)
        button.place(x=x - 5, y=y - 2)  
        app.color_buttons.append((button, angle)) 

    app.spin_buttons()
    
    pick_color_button = ttk.Button(sidebar, text="Pre Built Color Palette", command=app.pick_color)
    pick_color_button.pack(pady=5, padx=5, fill="x")
    
    app.custom_color_picker = CustomColorPicker(app.change_color)
    custom_color_picker_button = ttk.Button(
        sidebar,
        text="Custom Color Palette",
        command=app.custom_color_picker.open_picker 
    )
    custom_color_picker_button.pack(pady=5, padx=5, fill="x")
    
#!--------------------------------------------------------------------------------------------------------------------------------

def create_bottom_toolbar(app):
    toolbar = ttk.Frame(app.root, height=50)
    toolbar.pack(side="bottom", fill="x", padx=10, pady=10)

    slider_label = ttk.Label(toolbar, text="Brush Size:")
    slider_label.pack(side="left", padx=5)

    app.brush_size_label = ttk.Label(toolbar, text=f"{app.brush_size}")
    app.brush_size_label.pack(side="left", padx=5)

    app.brush_slider = ttk.Scale(toolbar, from_=1, to=20, orient="horizontal", command=app.update_brush_size)
    app.brush_slider.set(app.brush_size)
    app.brush_slider.pack(side="left", padx=5)

    eraser_button = ttk.Button(toolbar, text="Eraser", command=app.toggle_eraser)
    eraser_button.pack(side="right", padx=10)

    clear_button = ttk.Button(toolbar, text="Clear", command=app.clear_canvas)
    clear_button.pack(side="right", padx=10)

    circle_button = ttk.Button(toolbar, text="Circle", command=lambda: app.set_shape_mode('circle'))
    circle_button.pack(side="right", padx=10)

    square_button = ttk.Button(toolbar, text="Square", command=lambda: app.set_shape_mode('square'))
    square_button.pack(side="right", padx=10)
#!--------------------------------------------------------------------------------------------------------------------------------

def create_ui_elements(app):
    create_menu(app)
    create_sidebar(app)
    create_bottom_toolbar(app)


