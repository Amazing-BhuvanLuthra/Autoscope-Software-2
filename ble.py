
from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

def discover_devices():
    try:
        nearby_devices = subprocess.check_output(["hcitool", "scan"]).decode("utf-8")
        return [line.split("\t") for line in nearby_devices.split("\n") if len(line) > 0]
    except Exception as e:
        print("Error:", e)
        return []

@app.route('/')
def index():
    nearby_devices = discover_devices()
    return render_template('ble.html', nearby_devices=nearby_devices)

@app.route('/connect/<address>')
def connect(address):
    return f"Connecting to {address}..."

@app.route('/keyboard')
def keyboard():
    subprocess.Popen(["matchbox-keyboard"])
    return 'Keyboard opened.'

@app.route('/keyboard/close')
def close_keyboard():
    subprocess.Popen(["pkill", "matchbox-keyboard"])
    return 'Keyboard closed.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8080)
