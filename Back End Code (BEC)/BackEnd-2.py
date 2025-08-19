from flask import Flask, request
import socket

app = Flask(__name__)

TELLO_IP = '192.168.10.1'
TELLO_PORT = 8889
LOCAL_PORT = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', LOCAL_PORT))
sock.settimeout(5)

@app.route('/send')
def send():
    command = request.args.get('command')
    try:
        sock.sendto(command.encode('utf-8'), (TELLO_IP, TELLO_PORT))
        response, _ = sock.recvfrom(1024)
        return response.decode('utf-8')
    except socket.timeout:
        return "Timeout: No response from drone."
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
