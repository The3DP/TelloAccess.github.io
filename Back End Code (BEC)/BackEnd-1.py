from flask import Flask
from djitellopy import Tello

app = Flask(__name__)
drone = Tello()
drone.connect()

@app.route('/takeoff', methods=['POST'])
def takeoff():
    drone.takeoff()
    return "Drone took off!"

@app.route('/land', methods=['POST'])
def land():
    drone.land()
    return "Drone landed."

# Add more endpoints as needed...

if __name__ == '__main__':
    app.run(debug=True)
