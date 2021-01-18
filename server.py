from flask import Flask, send_from_directory, request
import random
import threading
import atexit

app = Flask(__name__)

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


def runs_test(l):
    import math
    import statistics

    l_median = statistics.median(l)
    runs, n1, n2 = 0, 0, 0

    # Checking for start of new run
    for i in range(len(l)):

        # no. of runs
        if (l[i] >= l_median and l[i - 1] < l_median) or \
                (l[i] < l_median and l[i - 1] >= l_median):
            runs += 1

            # no. of positive values
        if (l[i]) >= l_median:
            n1 += 1

            # no. of negative values
        else:
            n2 += 1

    runs_exp = ((2 * n1 * n2) / (n1 + n2)) + 1
    stan_dev = math.sqrt((2 * n1 * n2 * (2 * n1 * n2 - n1 - n2)) / \
                         (((n1 + n2) ** 2) * (n1 + n2 - 1)))

    z = (runs - runs_exp) / stan_dev

    return z

@app.route("/runs", methods=['GET', 'POST'])
def get_runs():
    import json

    data = request.json

    return json.dumps({
        'runs': runs_test(data['value']),
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
