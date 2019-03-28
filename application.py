from flask import Flask
application = Flask(__name__)
application.debug=True

@application.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
	application.run(host='54.71.104.154', port=80)