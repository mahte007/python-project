import yaml
import json
from model import Database
from views import ApplicationView

class ApplicationController:
    def __init__(self, yaml_path):
        with open(yaml_path, "r") as yaml_file:
            config = yaml.load(yaml_file, Loader=yaml.FullLoader)

        self.database = Database(config["data_file"], config["table_name"], config["fields"])
        self.view = ApplicationView(config["fields"], self.save_data, self.exit_application)

    def run(self):
        self.view.app.mainloop()

    def save_data(self):
        input_data = self.view.get_input_data()
        self.database.add_data(input_data)
        self.view.show_input_data(input_data)

    def exit_application(self):
        self.database.close()
        self.view.app.destroy()
