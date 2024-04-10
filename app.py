from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")
    # return 'Hello, World!'

@app.route('/newendpoint')
def create_new_endpoint():
    return 'I created new endpoint by making new function in app.route'


if __name__ == "__main__":
    app.run(debug=True)