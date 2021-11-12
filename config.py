from flask import Flask, render_template, request
import os, pathlib
import subprocess

app = Flask(__name__)

hpage = "Home Page"

path = pathlib.Path("state/") # Folder where the text file is whitch controls if the led is on or off

@app.route("/", methods = ['POST','GET'])
def home_page():
    if request.method == "POST":
        if "on" in request.form:
            set_active(True)
            color = "color:green;"
            return render_template("index.html", result=read_state(), color=color)
        elif "off" in request.form:
            set_active(False)
            color = "color:red;"
            return render_template("index.html", result=read_state(),color=color)
    if read_state() == "on":
        color = "color:green;"
    else:
        color = "color:red;"
    return render_template("index.html", result=read_state(),color=color)

def set_active(x):
    uinput = x
    if uinput == False:
        write_state(False)
    elif uinput == True:
        write_state(True)
    else:
        print("How did you even get here?")

def write_state(x):
    if x == False:
        if read_state() == "off":
            print("its already off")
        elif read_state() == "on":
            os.rename(f"{path}/1.txt", f"{path}/0.txt")
    elif x == True:
        if read_state() == "on":
            print("its already on")
        elif read_state() == "off":
            os.rename(f"{path}/0.txt", f"{path}/1.txt")

def read_state():
    value = os.listdir(path)
    for item in value:
        if item == "0.txt":
            return "off"
        elif item == "1.txt":
            return "on"

if __name__ == "__main__":
    subprocess.call("start python controller.py", shell=True)
    app.run(host='0.0.0.0', debug=True) # Remove