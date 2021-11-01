from flask import Flask, render_template
app = Flask(__name__)

USERNAME = "<INSERT YOUR NAME HERE>"

@app.route('/')
def hello_world():
    #Return simple string for home page
    return 'Hello World'

@app.route('/index')
def homepage():
    #Render html page with value set for the user variable
    return render_template("index.html", user = USERNAME)

if __name__ == '__main__':
    #Run app on port 5000 in debug mode. Host is specified as Flask needs you to give a host for apps that would
    #need to be externally visible - in this case, from outside the container
    app.run(debug=True, host='0.0.0.0', port=5000)