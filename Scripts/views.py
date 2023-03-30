import customtkinter as tk

class ApplicationView:
    def __init__(self, fields, save_callback, exit_callback):
        # Create app frame
        self.app = tk.CTk()
        self.app.geometry("720x480")
        self.app.title("Homework")
        self.app.protocol('WM_DELETE_WINDOW', exit_callback)

        # Set system settings
        tk.set_appearance_mode("System")
        tk.set_default_color_theme("blue")

        # Create title label
        self.title = tk.CTkLabel(self.app, text="")
        self.title.pack(padx=10, pady=10)

        # Create input fields
        self.input_vars = {}
        for field in fields:
            label = tk.CTkLabel(self.app, text=field['label'])
            input_var = tk.StringVar()
            link = tk.CTkEntry(self.app, width=350, height=40, textvariable=input_var)
            label.pack()
            link.pack()
            self.input_vars[field['field_name']] = input_var

        # Create buttons
        self.save_button = tk.CTkButton(self.app, text="Mentés", command=save_callback)
        self.exit_button = tk.CTkButton(self.app, text="Kilépés", command=exit_callback)
        self.save_button.pack(pady=10)
        self.exit_button.pack()

    def get_input(self, field_name):
        return self.input_vars[field_name].get()

    def clear_input(self, field_name):
        self.input_vars[field_name].set("")

    def close(self):
        self.app.destroy()

    def run(self):
        self.app.mainloop()
