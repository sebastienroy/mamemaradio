from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/confirmation')
def confirmation():
    render_template('confirmation.html')  # Ajoutez une page de confirmation


@app.route('/update_wifi', methods=['POST'])
def update_wifi():
    ssid = request.form['ssid']
    password = request.form['password']

    # Utilisez subprocess pour modifier les identifiants WiFi
    # (Remplacez la commande en fonction de votre système d'exploitation)
    #subprocess.run(['sudo', 'wpa_passphrase', ssid, password, '>>', '/etc/wpa_supplicant/wpa_supplicant.conf'])

    # confirmation()
    
    # Arrêter le serveur Flask proprement
    shutdown = request.environ.get('werkzeug.server.shutdown')
    if shutdown is not None:
        print("hello")
        # shutdown()

    # Redémarrez le service wpa_supplicant pour prendre en compte les modifications
    # subprocess.run(['sudo', 'systemctl', 'restart', 'wpa_supplicant'])

    #return "Identifiants WiFi mis à jour avec succès !"
    return render_template('confirmation.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')