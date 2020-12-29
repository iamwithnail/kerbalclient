import krpc
import threading
import time
import pusher
import os

PUSHER_APP_ID = os.environ.get("PUSHER_APP_ID")
PUSHER_KEY = os.environ.get("PUSHER_KEY")
PUSHER_SECRET = os.environ.get("PUSHER_SECRET")

pusher_client = pusher.Pusher(
  app_id=PUSHER_APP_ID,
  key=PUSHER_KEY,
  secret=PUSHER_SECRET,
  cluster='eu',
  ssl=True
)

# connect and pick vessel
conn = krpc.connect("Dashboard Script")
vessel = conn.space_center.active_vessel


def send_websocket():
    while True:
        pusher_client.trigger("telemetry", "update", telemetry)
        print(telemetry)
        time.sleep(1)


def apoapsis_altitude(current_value):
    telemetry["apoapsis_altitude"] = round(current_value, 0)


def periapsis_altitude(current_value):
    telemetry["periapsis_altitude"] = round(current_value, 0)


def time_to_periapsis(current_value):
    telemetry["time_to_periapsis"] = round(current_value, 0)


def time_to_apoapsis(current_value):
    telemetry["time_to_apoapsis"] = round(current_value, 0)


def true_air_speed(current_value):
    telemetry["true_air_speed"] = round(current_value, 1)


def g_force(current_value):
    telemetry["g_force"] = round(current_value, 2)


def heading(current_value):
    telemetry["heading"] = round(current_value, 1)


def mean_altitude(current_value):
    telemetry["mean_altitude"] = round(current_value, 0)


def surface_altitude(current_value):
    telemetry["surface_altitude"] = round(current_value, 0)


def velocity(current_value):
    telemetry["velocity"] = current_value


def vertical_speed(current_value):
    telemetry["vertical_speed"] = round(current_value, 1)


def inclination(current_value):
    telemetry["inclination"] = round(current_value, 2)


def speed(current_value):
    telemetry["speed"] = round(current_value, 1)


flight_stats = {
    "g_force": g_force,
    "heading": heading,
    "mean_altitude": mean_altitude,
    "true_air_speed": true_air_speed,
    "surface_altitude": surface_altitude,
    "velocity": velocity,
    "vertical_speed": vertical_speed,
}

orbital_stats = {
    "apoapsis_altitude": apoapsis_altitude,
    "time_to_apoapsis": time_to_apoapsis,
    "periapsis_altitude": periapsis_altitude,
    "time_to_periapsis": time_to_periapsis,
    "inclination": inclination,
    "speed": speed,
}

telemetry = {}

flight_streams = {
    item: conn.add_stream(getattr, vessel.flight(), item) for item in flight_stats
}

orbital_streams = {
    item: conn.add_stream(getattr, vessel.orbit, item) for item in orbital_stats
}

print(flight_streams)
for key, stream in flight_streams.items():
    stream.add_callback(flight_stats[key])
    stream.start()

for key, stream in orbital_streams.items():
    stream.add_callback(orbital_stats[key])
    stream.start()
#
# websocket_thread = threading.Thread(target=send_websocket, args=())
# websocket_thread.start()
while True:
    send_websocket()
