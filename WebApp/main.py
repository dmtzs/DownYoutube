try:
    from flask import Flask
except ImportError as eImp:
    print(f"The following import error ocurred: {eImp}")

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__== "__main__":
    try:
        app.run(host= "127.0.0.1", port= 5000, debug= False)
    except Exception as e:
        print(f"The following error ocurred: {e}")