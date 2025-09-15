from pollards_rho.pollards_rho import PollardsRho
from CTkToolTip import CTkToolTip
from customtkinter import *
from sympy import isprime
from PIL import Image
from RSA import RSA
import random


class main(CTk):
    def __init__(self):
        super().__init__()
        set_appearance_mode("dark")
        self.geometry("800x400")
        self.title("RSAnalyze")
        self.resizable(False, False)

        self.dir_path = os.path.dirname(os.path.abspath(__file__))

        background_image = CTkImage(light_image=Image.open(os.path.join(self.dir_path, "BG.png")),
                                    dark_image=Image.open(
                                        os.path.join(self.dir_path, "BG.png")),
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
        self.p_entry = CTkEntry(
            self, placeholder_text="Prime 1 (p)", bg_color=self.light_grey, width=150, height=30, font=("Inter", 12))
        self.p_entry.place(x=25, y=75)

        # ENTRY q
        self.q_entry = CTkEntry(
            self, placeholder_text="Prime 2 (q)", bg_color=self.light_grey, width=150, height=30, font=("Inter", 12))
        self.q_entry.place(x=25, y=125)

        # BUTTON auto-generate primes
        auto_primes_button = CTkButton(self, width=150, height=25, bg_color=self.light_grey, text="Randomize",
                                       fg_color=self.purple, hover_color=self.dark_purple, text_color=self.white, font=(
                                           "Inter", 16),
                                       command=self.randomize_primes)

        auto_primes_button.place(x=25, y=175)

        # BUTTON Generate
        Factorize_button = CTkButton(self, width=150, height=30, bg_color=self.light_grey, text="Generate",
                                     fg_color=self.purple, hover_color=self.dark_purple, text_color=self.white, font=(
                                         "Inter", 16),
                                     command=self.calculate_rsa_values)

        Factorize_button.place(x=25, y=350)

        # BUTTON Factorize
        Factorize_button = CTkButton(self, width=150, height=30, bg_color=self.light_grey, text="Factorize",
                                     fg_color=self.purple, hover_color=self.dark_purple, text_color=self.white, font=(
                                         "Inter", 16),
                                     command=self.factorize)

        Factorize_button.place(x=636, y=350)

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

        # SWITCH Fermats Number

    def showErrorWindow(self, message: str, log=None):
        if hasattr(self, "error_box"):
            self.error_box.destroy()

        self.error_box = CTkFrame(
            self, width=300, height=120, fg_color="#2a0000", corner_radius=12, bg_color=self.light_grey)
        self.error_box.place(relx=0.5, rely=0.5, anchor="center")

        error_label = CTkLabel(self.error_box, text=message,
                               text_color="#ffcccc", wraplength=280, font=("", 14))
        error_label.pack(pady=(15, 5), padx=10)

        close_button = CTkButton(self.error_box, text="Close", width=100, fg_color="#ff4c4c",
                                 hover_color="#cc0000", corner_radius=32, command=self.error_box.destroy)
        close_button.pack(pady=(0, 10))

        if log:
            CTkToolTip(error_label, message=log)

    def randomize_primes(self):
        with open(f"{self.dir_path}/primes-to-100k.txt", "r") as f:
            primes = f.read().splitlines()

        pq_distance = 16

        p = random.randint(5, len(primes) - pq_distance - 1)
        q = p + pq_distance  # ensure q is always larger than p by a small margin

        self.p_entry.delete("0", "end")
        self.q_entry.delete("0", "end")

        self.p_entry.insert(0, primes[p])
        self.q_entry.insert(0, primes[q])

    def calculate_rsa_values(self):
        p = self.p_entry.get()
        q = self.q_entry.get()

        if p == q:
            self.showErrorWindow("p and q cannot be the same value")
            return

        try:
            p = int(p)
            q = int(q)

            if not (isprime(p) and isprime(q)):
                self.showErrorWindow("Both p and q must be prime.")
                return

            rsa = RSA(p, q)

            n, phi_n, e, d = rsa.get_values()

        except ValueError:
            self.showErrorWindow(
                "Please enter valid prime integers for p and q.")
            return

        self.rsa_values.configure(state="normal")

        self.rsa_values.delete("0.0", "end")
        self.rsa_values.insert("end", f"n - {n}\n")
        self.rsa_values.insert("end", f"φ(n) - {phi_n}\n")
        self.rsa_values.insert("end", f"e - {e}\n")
        self.rsa_values.insert("end", f"d - {d}\n\n")

        self.rsa_values.insert("end", f"Public Key - {rsa.get_public_key()}\n")
        self.rsa_values.insert("end", f"Private Key - {rsa.get_private_key()}")

        self.rsa_values.configure(state="disabled")

    def factorize(self):
        pass


if __name__ == "__main__":
    app = main()
    app.mainloop()
