from GT_imports import *
def apply_styles(root):
    style = ttk.Style(root)
    style.theme_use("alt")
    
    style.configure("TFrame", relief="solid", borderwidth=2)

     #* \\ Button Style \\
    style.configure("TButton", background="#7f7f7f", foreground="Black", font=("Arial", 14) ,relief="ridge", borderwidth=10)
    style.map("TButton", background=[("active", "darkgray")])
    
    style.configure("TScale", background="black", sliderlength=25, troughcolor="#7f7f7f")
    
        # * \\ Label Style \\ *
    style.configure("TLabel", background="#7f7f7f", foreground="black", font=("Arial", 12, "bold"), anchor="center")
        #* \\ Scrollbar Style \\
    style.configure("TScrollbar", background="black", troughcolor="#444444", arrowcolor="#00db00" )
        #* \\ Entry Widget Style \\
    style.configure("TEntry", fieldbackground="#444444", foreground="#00db00", font=("Arial", 14))
    
    
def custom_menu_styles(menu):
    menu.configure(
        bg="gray",
        fg="black",
        font=("Arial", 12),
        relief="ridge",
        borderwidth=3,
        activebackground="#c8c8c8",
        activeforeground="#1aff00",
        disabledforeground="gray"
    ) 

    menu.bind("<Enter>", lambda event: menu.configure(bf="lightgray"))
    menu.bind("<Leave>", lambda event: menu.configure(bf="darkgray"))
