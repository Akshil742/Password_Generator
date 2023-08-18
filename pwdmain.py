import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import random

ctk.set_appearance_mode("white")
ctk.set_default_color_theme("blue")

class PasswordGeneratorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Password Generator")
        self.resizable(False, False)

        self.upperframe = ctk.CTkFrame(self, corner_radius=7, fg_color="#00D31A")
        self.upperframe.pack(side="top", fill="x", expand=True, pady=15, padx=10)

        self.lable1 = ctk.CTkLabel(self.upperframe, bg_color="#A2FAAD", text="Generated Password", width=40, height=40, font=('Helvetica', 15, 'bold'))
        self.lable1.pack(fill="both", padx=5, pady=5, expand=True)

        self.divide1 = ttk.Separator(self, orient="horizontal")
        self.divide1.pack(side="top", fill="x", padx=10, expand=1)

        self.downframe = ctk.CTkFrame(self, corner_radius=10, fg_color="#A2FAAD")
        self.downframe.pack(side="bottom", fill="both", expand=True, ipadx=20, ipady=25, padx=10, pady=10)

        self.downframe.grid_rowconfigure((0, 1), weight=1)
        self.downframe.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

        self.cheakbox1 = ctk.CTkCheckBox(self.downframe, text="Uppercase", font=('Helvetica', 15, 'bold'), fg_color="lightblue", corner_radius=50)
        self.cheakbox1.grid(row=0, column=0, sticky="w", padx=20)
        self.cheakbox2 = ctk.CTkCheckBox(self.downframe, text="Digits", font=('Helvetica', 15, 'bold'), fg_color="lightblue", corner_radius=50)
        self.cheakbox2.grid(row=1, column=0, sticky="w", padx=20)
        self.cheakbox3 = ctk.CTkCheckBox(self.downframe, text="Lowercase", font=('Helvetica', 15, 'bold'), fg_color="lightblue", corner_radius=50)
        self.cheakbox3.grid(row=0, column=1, sticky="w", padx=20)
        self.cheakbox4 = ctk.CTkCheckBox(self.downframe, text="Special Characters", font=('Helvetica', 15, 'bold'), fg_color="lightblue", corner_radius=50)
        self.cheakbox4.grid(row=1, column=1, sticky="w", padx=20)

        self.divide2 = ttk.Separator(self.downframe, orient="horizontal")
        self.divide2.grid(row=2, columnspan=2, sticky="ew", padx=20, pady=10)

        self.slider = ctk.CTkSlider(self.downframe, from_=0, to=15, button_color="#00D31A")
        self.slider.grid(row=3, columnspan=2, sticky="ew", padx=20, pady=10)

        self.lable2 = ctk.CTkLabel(self.downframe, text="0", width=50, height=1, font=('Helvetica', 15, 'bold'))
        self.lable2.grid(row=4, columnspan=2, sticky="ew", padx=20, pady=10)

        self.btn = ctk.CTkButton(self.downframe, font=('Helvetica', 15), text="Generate Password", width=30, command=self.generatePassword, fg_color="#00D31A")
        self.btn.grid(row=5, columnspan=2, padx=40, pady=(0, 10))

        self.slider.bind("<ButtonRelease-1>", self.update_value)
        self.slider.set(0)

    def update_value(self, event):
        self.lable2.configure(text=f"Length: {int(self.slider.get())}")
        
    def generatePassword(self):
        leng = int(self.slider.get())
        characters = ""
        if self.cheakbox1.get():
            characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if self.cheakbox3.get():
            characters += "abcdefghijklmnopqrstuvwxyz"
        if self.cheakbox4.get():
            characters += "!@#$%^&*()_+[]|;:<>?~"
        if self.cheakbox2.get():
            characters += "0123456789"
            
        if not characters:
            self.lable1.configure(text="Select at least one option")
            return
            
        password = ''.join(random.choice(characters) for _ in range(leng))
        self.lable1.configure(text=password)

if __name__ == "__main__":
    PasswordGeneratorApp().mainloop()
