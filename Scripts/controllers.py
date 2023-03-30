from tkinter import StringVar
import views
import model

class ApplicationController:
    def __init__(self, yaml_path):
        data = model.load_yaml(yaml_path)

        self.fields = data['fields']
        self.json_file_path = data['output_file']
        self.database_file_path = data['data_file']
        self.table_name = data['table_name']
        self.input_data_list = []

        self.view = views.ApplicationView(self.fields, self.save_data, self.exit_application)

    def save_data(self):
        input_data = {}

        for field in self.fields:
            field_name = field['field_name']
            user_input = self.view.get_input(field_name)
            input_data[field_name] = user_input
            self.view.clear_input(field_name)

        self.input_data_list.append(input_data)
        print(self.input_data_list)

    def export_data(self):
        model.save_json(self.json_file_path, self.input_data_list)
        model.save_data_to_db(self.database_file_path, self.table_name, self.fields, self.input_data_list)

    def exit_application(self):
        self.export_data()
        self.view.close()

    def run(self):
        self.view.run()
