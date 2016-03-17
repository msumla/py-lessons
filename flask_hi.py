import os
from flask import Flask
from jinja2 import Environment, FileSystemLoader
from flask import request

def humanize(bytes):
    if bytes < 1024:
        return "%.2f B" % bytes
    elif bytes < 1024 ** 2:
        return "%.2f kB" % (bytes / 1024.0)
    elif bytes < 1024 ** 3:
        return "%.2f MB" % (bytes / 1024.0 ** 2)
    else:
        return "%.2f GB" % (bytes / 1024.0 ** 3)

env = Environment(loader=FileSystemLoader("templates"), trim_blocks=True)

app = Flask(__name__)

def list_log_files(): # generator has yield statement
    for filename in os.listdir("/media/margus/SSD/Dokumendid/2. semester/Python/py-lessons/logs"):
        if filename.endswith(".log"):
            yield filename
        if filename.endswith(".gz"):
            yield filename

#@app.route("/report/")
#def report():
    #return env.get_template("report.html").render(humanize = humanize(("whoever", 500),))

@app.route("/")
def hello():
    return env.get_template("index.html").render(log_files=list_log_files())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")