from pollards_rho.pollards_rho import PollardsRho
from CTkToolTip import CTkToolTip
from customtkinter import *
from logic import Logic
from PIL import Image


class main(CTk):
    def __init__(self):
        super().__init__()
        set_appearance_mode("dark")
        self.geometry("800x400")
        self.title("RSAnalyze")
        self.resizable(False, False)

        dir_path = os.path.dirname(os.path.abspath(__file__))

        background_image = CTkImage(light_image=Image.open(os.path.join(dir_path, "BG.png")),
                                    dark_image=Image.open(
                                        os.path.join(dir_path, "BG.png")),
                                    size=(800, 400))
        CTkLabel(self, image=background_image, text="").place(x=0, y=0)

        # colors
        self.purple = "#7b00ff"
        self.dark_purple = "#6100c9"
        self.light_grey = "#2f2f2f"
        self.dark_grey = "#222222"
        self.white = "#ffffff"
        self.black = "#000000"

        # ENTRY p
        p_entry = CTkEntry(
            self, placeholder_text="Prime 1 (p)", bg_color=self.light_grey, width=150, height=30, font=("Inter", 12))
        p_entry.place(x=25, y=75)

        # ENTRY q
        q_entry = CTkEntry(
            self, placeholder_text="Prime 2 (q)", bg_color=self.light_grey, width=150, height=30, font=("Inter", 12))
        q_entry.place(x=25, y=125)

        # BUTTON auto-generate primes
        auto_primes_button = CTkButton(self, width=150, height=25, bg_color=self.light_grey, text="Randomize",
                                       fg_color=self.purple, hover_color=self.dark_purple, text_color=self.white, font=("Inter", 16))

        auto_primes_button.place(x=25, y=175)

        # BUTTON Factorize
        Factorize_button = CTkButton(self, width=150, height=30, bg_color=self.light_grey, text="Generate",
                                     fg_color=self.purple, hover_color=self.dark_purple, text_color=self.white, font=("Inter", 16))

        Factorize_button.place(x=25, y=350)

        # TEXTBOX RSA Values
        self.rsa_values = CTkTextbox(
            self, width=400, height=125, font=("Inter", 16), bg_color=self.light_grey, corner_radius=0, fg_color=self.light_grey)
        self.rsa_values.place(x=220, y=78)
        self.rsa_values.configure(state="disabled")

        # TEXTBOX Factorization (Pollard's Rho)
        self.Factorization = CTkTextbox(
            self, width=400, height=125, font=("Inter", 16), bg_color=self.light_grey, corner_radius=0, fg_color=self.light_grey)
        self.Factorization.place(x=220, y=245)
        self.Factorization.configure(state="disabled")


if __name__ == "__main__":
    app = main()
    app.mainloop()
