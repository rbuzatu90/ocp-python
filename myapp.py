from flask import Flask
import os
import socket
application = Flask(__name__)

@application.route("/hello")
def hello():
    return "Hello World!"

@application.route("/")
def return_hostname():
    app = os.environ['app']
    if app:
      return "Hostname from app {} is {} \n".format(app, socket.gethostname())
    else:
      return "Hostname {} \n".format(socket.gethostname())

if __name__ == "__main__":
    application.run()
