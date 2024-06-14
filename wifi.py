from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

def scan_wifi():
    """Scans for available Wi-Fi networks and returns a list of SSIDs."""
    try:
        result = subprocess.run(['sudo', 'iwlist', 'wlo1', 'scan'], capture_output=True, text=True, check=True)
        networks = []
        for line in result.stdout.split('\n'):
            if "ESSID" in line:
                ssid = line.split(":")[1].strip().strip('"')
                if ssid:
                    networks.append(ssid)
        return networks
    except subprocess.CalledProcessError as e:
        print(f"Error scanning for Wi-Fi networks: {e}")
        return []

def connect_to_wifi(ssid, password):
    """Connects to a Wi-Fi network with the given SSID and password."""
    wpa_conf = f"""
    network={{
        ssid="{ssid}"
        psk="{password}"
    }}
    """
    try:
        with open("/etc/wpa_supplicant/wpa_supplicant.conf", "a") as f:
            f.write(wpa_conf)
        subprocess.run(['sudo', 'wpa_cli', '-i', 'wlo1', 'reconfigure'], check=True)
    except Exception as e:
        print(f"Error connecting to Wi-Fi network: {e}")

@app.route('/')
def index():
    networks = scan_wifi()
    return render_template('wifi.html', networks=networks)

@app.route('/connect', methods=['POST'])
def connect():
    ssid = request.form['ssid']
    password = request.form['password']
    connect_to_wifi(ssid, password)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

