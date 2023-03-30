import tkinter
import customtkinter

class ApplicationView:
    def __init__(self, fields, save_callback, exit_callback):
        self.fields = fields
        self.save_callback = save_callback
        self.exit_callback = exit_callback
        self.input_vars = ()
        self.input_data_list = []

        
        self.app = customtkinter.CTk()
        self.app.geometry("720x480")
        self.app.title("Python Homework")
        self.app.protocol("WM_WINDOW_DELETE", self.exit_callback)

        
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")


        self.title = customtkinter.CTkLabel(self.app, text="Table Name")
        self.title.pack(padx=10, pady=10)


        for field in self.fields:
            label = customtkinter.CTkLabel(self.app, text=field["label"])
            input_var = tkinter.StringVar()
            input = customtkinter.CTkEntry(self.app, width=350, height=40, textvariable=input_var)
            label.pack()
            input.pack()
            self.input_vars[fields["field_name"]] = input_var

        
        self.save_button = customtkinter.CTkButton(self.app, text="Mentés", command=self.save_callback)
        self.exit_button = customtkinter.CTkButton(self.app, text="Kilépés", command=self.exit_callback)
        self.save_button.pack(pady=10)
        self.exit_button.pack()

    def get_input_data(self):
        input_data = {}
        for field in self.fields:
            field_name = field["field_name"]
            user_input = self.input_vars[field_name].get()
            input_data[field_name] = user_input
            self.input_vars[field_name].set("")
        return input_data
    
    def show_input_data(self, data):
        self.input_data_list.append(data)
        print(self.input_data_list)
