from flask import Flask, send_from_directory
import random
import threading
import atexit

idx = 0
load_avg = []
timer = threading.Thread()

def create_app():
    app = Flask(__name__)

    def interrupt():
        global timer
        timer.cancel()

    def get_load():
        import psutil
        global load_avg
        global idx
        
        # print(load_avg)
        load_avg.append(psutil.cpu_percent())

        if len(load_avg) > 100:
            load_avg.pop(0)
            idx += 1

        start()

    def start():
        global timer
        timer = threading.Timer(1.0, get_load, ())
        timer.start()

    start()
    atexit.register(interrupt)
    return app

app = create_app()

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)


@app.route("/rand")
def hello():
    return str(random.randint(0, 100))

@app.route("/get_load")
def get_load():
    import json
    return json.dumps({'time': list(range(idx,idx+len(load_avg))), 'load': load_avg})

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
