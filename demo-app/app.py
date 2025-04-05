from flask import Flask
import time 
import sys

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'


if __name__ == "__main__":
    time.sleep(10)
    sys.exit()
    app.run(host='0.0.0.0', port=8000)