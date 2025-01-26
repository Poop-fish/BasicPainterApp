from GT_imports import *

def apply_styles(root):
    style = ttk.Style(root)
    style.theme_use("alt")

    #* \\ Frame Style \\
    style.configure("TFrame", relief="solid", borderwidth=2)

     #* \\ Button Style \\
    style.configure("TButton", background="Gray", foreground="Black", font=("Arial", 14) ,relief="ridge", borderwidth=10)
    style.map("TButton", background=[("active", "darkgray")])
    
