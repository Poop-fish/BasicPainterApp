from GT_imports import *
from GT_Editor_Management import *
from GT_CustomStyle import apply_styles , custom_menu_styles 
from GT_Widgets import GTG , CustomColorPicker
#!--------------------------------------------------------------------------------------------------------------------------------


def create_menu(app):
    menu_bar = tk.Menu(app.root)
    
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Save as PNG", command=app.save_as_png)
    file_menu.add_command(label="Load image", command=app.load_image)
    file_menu.add_separator() 
    file_menu.add_command(label="Exit", command=app.root.quit)
    menu_bar.add_cascade(label="File", menu=file_menu)
    
    edit_menu = tk.Menu(menu_bar, tearoff=0)
    edit_menu.add_command(label="Clear", command=app.clear_canvas)
    edit_menu.add_command(label="Toggle Grid Lines", command=app.toggle_grid)
    menu_bar.add_cascade(label="Edit", menu=edit_menu)
    
    
    settings_menu = tk.Menu(menu_bar, tearoff=0)
    def show_speed_slider():
        slider_window = GTG.Toplevel(app.root , enable_hover=False)
        slider_window.title("Adjust Spin Speed")
        slider_window.geometry("300x150")
        slider_window.config(bg="gray") 

        label = GTG.Label(slider_window, text="Spin Speed Setting", fg="black", bg="#b0b0b0", font=("Arial", 12, "bold"), relief="raised" , borderwidth=15)
        label.pack(pady=10)

        speed_slider = GTG.Scale(
        slider_window, from_=1, to=100, orient="horizontal", command=app.update_spin_speed, enable_click_effect=True
        )
        speed_slider.set(app.spin_speed) 
        speed_slider.pack(pady=10)
        speed_slider.set_colors(bg="gray", fg="black", troughcolor="#b0b0b0", hover_bg="#d0d0d0", hover_highlight="#707070", click_bg="gray", click_highlight="#505050")
    
    settings_menu.add_command(label="Adjust Spin Speed", command=show_speed_slider)
    settings_menu.add_separator() 
    settings_menu.add_command(label="Start/Stop Spin", command=app.toggle_spin)  
    menu_bar.add_cascade(label="Settings", menu=settings_menu) 


    Toggle_Theme_menu = tk.Menu(menu_bar, tearoff=0)
    Toggle_Theme_menu.add_command(label="Toggle Theme", command=app.toggle_bg_color)
    menu_bar.add_cascade(label="Toggle Theme", menu=Toggle_Theme_menu)

    custom_menu_styles(file_menu)
    custom_menu_styles(edit_menu)
    custom_menu_styles(settings_menu)
    custom_menu_styles(Toggle_Theme_menu)
    
    app.root.config(menu=menu_bar)

#!--------------------------------------------------------------------------------------------------------------------------------

def create_sidebar(app):
    
    sidebar = GTG.Frame(app.root, width=200, height=600, enable_hover=False)
    sidebar.pack(side="left", fill="y", padx=10, pady=10)
    
    for i, color in enumerate(app.colors):
        angle = i * (360 / len(app.colors))  
        x = app.center_x + app.radius * math.cos(math.radians(angle))  
        y = app.center_y + app.radius * math.sin(math.radians(angle))  

        button = tk.Button(
            sidebar, width=3, height=1, command=lambda c=color: app.change_color(c), 
            relief="ridge" , borderwidth=3, activebackground=(color)
        )
        button.configure(background=color)
        button.place(x=x - 5, y=y - 2)  
        app.color_buttons.append((button, angle)) 

    app.spin_buttons()
                        # (GTG.Button)
    pick_color_button = GTG.Button(sidebar, text="Pre Built Color Palette", command=app.pick_color)
    pick_color_button.pack(pady=5, padx=5, fill="x")
    
    app.custom_color_picker = CustomColorPicker(app.change_color)
    custom_color_picker_button = GTG.Button(
        sidebar,
        text="Custom Color Palette",
        command=app.custom_color_picker.open_picker 
    )
    custom_color_picker_button.pack(pady=5, padx=5, fill="x")
    
    circle_button  = GTG.Button(sidebar, text="Draw Circle",command=lambda: app.set_shape_mode('circle'))
    circle_button.pack(pady=5, padx=5, fill="x")

    square_button = GTG.Button(sidebar, text="Draw Square",command=lambda: app.set_shape_mode('square'))
    square_button .pack(pady=5, padx=5, fill="x")
    
    add_text_button = GTG.Button(sidebar, text="Add Text", command=app.add_text)
    add_text_button.pack(pady=5, padx=5, fill="x")

    toggle_grid_button = GTG.Button(sidebar, text="Toggle Grid", command=app.toggle_grid)
    toggle_grid_button.pack(pady=5, padx=5, fill="x") 

    toggle_spin_button = GTG.Button(sidebar, text="Toggle", command=app.toggle_spin, width=5, height=1)
    toggle_spin_button.pack(pady=90, padx=5)
        
#!--------------------------------------------------------------------------------------------------------------------------------

def create_bottom_toolbar(app):
    toolbar = GTG.Frame(app.root, height=50, enable_hover=False)
    toolbar.pack(side="bottom", fill="x", padx=10, pady=10)

    slider_label = GTG.Label(toolbar, text="Brush Size:" , enable_hover=True)
    slider_label.pack(side="left", padx=5)

    app.brush_size_label = GTG.Label(toolbar, text=f"{app.brush_size}")
    app.brush_size_label.pack(side="left", padx=5)

    app.brush_slider = GTG.Scale(
    toolbar, from_=1, to=100, orient="horizontal", command=app.update_brush_size, enable_click_effect=True , show_value=False
    )
    app.brush_slider.set(app.spin_speed) 
    app.brush_slider.pack(side="left", padx=5)
    app.brush_slider.set_colors(bg="gray", fg="black", troughcolor="#b0b0b0", hover_bg="#d0d0d0", hover_highlight="#707070", click_bg="gray", click_highlight="#505050")

    eraser_button = GTG.Button(toolbar, text="Eraser", command=app.toggle_eraser)
    eraser_button.pack(side="right", padx=10)

    clear_button = GTG.Button(toolbar, text="Clear", command=app.clear_canvas)
    clear_button.pack(side="right", padx=10)
    
#!--------------------------------------------------------------------------------------------------------------------------------

def create_ui_elements(app):
    create_menu(app)
    create_sidebar(app)
    create_bottom_toolbar(app)
