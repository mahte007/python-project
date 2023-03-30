from controllers import ApplicationController

if __name__ == '__main__':
    try:
        app = ApplicationController("../Config/config.yml")
        app.run()
    except:
        print("Error! File not found!")