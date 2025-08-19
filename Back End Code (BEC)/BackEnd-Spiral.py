from flask import Flask, request, jsonify
from djitellopy import Tello
import time

app = Flask(__name__)

# Spiral flight settings
RADIUS_INCREMENT = 10     # cm
ANGLE_INCREMENT = 10      # degrees
NUM_LOOPS = 36
FORWARD_DISTANCE = 30     # cm

@app.route('/spiral', methods=['POST'])
def spiral_flight():
    tello = Tello()
    try:
        tello.connect()
        tello.takeoff()

        for i in range(NUM_LOOPS):
            radius = RADIUS_INCREMENT * i
            angle = ANGLE_INCREMENT * i

            tello.move_forward(FORWARD_DISTANCE)
            tello.rotate_clockwise(angle)

            time.sleep(1)

        tello.land()
        return jsonify({'response': 'Spiral flight completed.'})
    except Exception as e:
        tello.land()
        return jsonify({'response': f'Error: {str(e)}'}), 500
    finally:
        tello.end()

@app.route('/')
def index():
    return "Tello Spiral Drone Server is running."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
