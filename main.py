import customtkinter

class main(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x400")
        self.title("RSAnalysis")
        self.resizable(False, False)


if __name__ == "__main__":
    app = main()
    app.mainloop()
