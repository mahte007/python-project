import tkinter
import customtkinter
import yaml
import json
import sqlite3

class Application:
    def __init__(self, yaml_path):
        with open(yaml_path, "r") as f:
            data = yaml.safe_load(f)

        self.fields = data['fields']
        self.json_file_path = data['output_file']
        self.database_file_path = data['data_file']
        self.table_name = data['table_name']
        self.input_data_list = []

        # Create app frame
        self.app = customtkinter.CTk()
        self.app.geometry("720x480")
        self.app.title("Homework")
        self.app.protocol('WM_DELETE_WINDOW', self.exit_application)

        # Set system settings
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")

        # Create title label
        self.title = customtkinter.CTkLabel(self.app, text=self.table_name)
        self.title.pack(padx=10, pady=10)

        # Create input fields
        self.input_vars = {}
        for field in self.fields:
            label = customtkinter.CTkLabel(self.app, text=field['label'])
            input_var = tkinter.StringVar()
            link = customtkinter.CTkEntry(self.app, width=350, height=40, textvariable=input_var)
            label.pack()
            link.pack()
            self.input_vars[field['field_name']] = input_var

        # Create buttons
        self.save_button = customtkinter.CTkButton(self.app, text="Mentés", command=self.save_data)
        self.exit_button = customtkinter.CTkButton(self.app, text="Kilépés", command=self.exit_application)
        self.save_button.pack(pady=10)
        self.exit_button.pack()

    def save_data(self):
        input_data = {}

        for field in self.fields:
            field_name = field['field_name']
            user_input = self.input_vars[field_name].get()
            input_data[field_name] = user_input
            self.input_vars[field_name].set("")

        self.input_data_list.append(input_data)
        print(self.input_data_list)

    def export_data(self):
        with open(self.json_file_path, 'w') as f:
            json.dump(self.input_data_list, f)

        connection = sqlite3.connect(self.database_file_path)
        cursor = connection.cursor()

        column_names = [field['field_name'] for field in self.fields]
        create_table_sql = f"CREATE TABLE IF NOT EXISTS {self.table_name} (id INTEGER PRIMARY KEY, {', '.join(column_names)})"
        cursor.execute(create_table_sql)

        for data in self.input_data_list:
            values = tuple(data[column_name] for column_name in column_names)
            insert_sql = f"INSERT INTO {self.table_name} ({', '.join(column_names)}) VALUES ({', '.join(['?']*len(column_names))})"
            cursor.execute(insert_sql, values)

        connection.commit()
        connection.close()

    def exit_application(self):
        self.export_data()
        self.app.quit()

    def run(self):
        self.app.mainloop()

if __name__ == '__main__':
    app = Application("config.yml")
    app.run()
