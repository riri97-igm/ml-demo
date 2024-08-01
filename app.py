from flask import Flask

app = Flask(__name__) #changes

@app.route('/')
def index():
    return "Index"

@app.route('/hello')
def hello():
    return "Hello World"

if __name__ == "__main__":
    app.run()
