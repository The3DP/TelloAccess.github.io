from flask import Flask, request, jsonify
from djitellopy import Tello

app = Flask(__name__)

# Initialize Tello drone
drone = Tello()
drone.connect()

@app.route('/command', methods=['POST'])
def command():
    data = request.get_json()
    cmd = data.get('command')

    try:
        if cmd == "takeoff":
            drone.takeoff()
        elif cmd == "land":
            drone.land()
        elif cmd == "up":
            drone.move_up(30)
        elif cmd == "down":
            drone.move_down(30)
        elif cmd == "left":
            drone.move_left(30)
        elif cmd == "right":
            drone.move_right(30)
        elif cmd == "forward":
            drone.move_forward(30)
        elif cmd == "back":
            drone.move_back(30)
        elif cmd == "cw":
            drone.rotate_clockwise(90)
        elif cmd == "ccw":
            drone.rotate_counter_clockwise(90)
        elif cmd == "battery":
            battery = drone.get_battery()
            return jsonify({'response': f'Battery: {battery}%'})
        else:
            return jsonify({'response': 'Unknown command'}), 400

        return jsonify({'response': 'Command executed'})
    except Exception as e:
        return jsonify({'response': f'Error: {str(e)}'}), 500

@app.route('/')
def index():
    return 'Tello Drone Flask Server is running.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
