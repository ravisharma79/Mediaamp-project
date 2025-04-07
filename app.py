from flask import Flask
import time

app = Flask(__name__)

def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
    return x

@app.route("/")
def hello():
    return "Hello World! from RAVI SHARMA"

@app.route("/compute")
def compute():
    start = time.time()
    result = fibonacci(10000)
    end = time.time()
    return f"Done in {end - start:.2f}s"
