from controllers import ApplicationController

if __name__ == '__main__':
    app = ApplicationController("config.yml")
    app.run()