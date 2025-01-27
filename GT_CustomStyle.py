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
    
 
