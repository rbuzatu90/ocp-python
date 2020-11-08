from flask import Flask
import socket
application = Flask(__name__)

@application.route("/hello")
def hello():
    return "Hello World!"

@application.route("/")
def return_hostname():
    return "Hostname {} \n".format(socket.gethostname())

if __name__ == "__main__":
    application.run()
