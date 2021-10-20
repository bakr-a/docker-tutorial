from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/index')
def homepage():
    return app.send_static_file("index.html")

if __name__ == '__main__':
    #Run app on port 5000 in debug mode. Host is specified as Flask needs you to give a host for apps that would
    #need to be externally visible - in this case, from outside the container
    app.run(debug=True, host='0.0.0.0', port=5000)