from GT_imports import *
def apply_styles(root):
    style = ttk.Style(root)
    style.configure("TFrame", relief="solid", borderwidth=2)
    style.configure("TButton", relief="raised", padding=6, font=("Arial", 10))
