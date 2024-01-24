from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import paho.mqtt.client as mqtt
import json
import datetime

app = Flask(__name__)
cors = CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")
# InfluxDB Configuration
token = "hioQscqfx9RGYXsr7i23J6F_RkYZeC44ykEsmBEuhoyi0SmcQweL4wcpfITfK_Gfggsh97Gb_YQhfmJwd6_K9Q=="
org = "FTN"
url = "http://localhost:8086"
bucket = "iot-smart-home"
influxdb_client = InfluxDBClient(url=url, token=token, org=org)


alarm_clock = None

# MQTT Configuration
mqtt_client = mqtt.Client()
mqtt_client.connect("localhost", 1883, 60)
mqtt_client.loop_start()

def on_connect(client, userdata, flags, rc):
    with open("../settings.json", 'r') as f:
        settings = json.load(f)
        for topic in settings.keys():
            client.subscribe(topic)
mqtt_client.on_connect = on_connect
mqtt_client.on_message = lambda client, userdata, msg: save_to_db(json.loads(msg.payload.decode('utf-8')))


def save_to_db(data):
    write_api = influxdb_client.write_api(write_options=SYNCHRONOUS)
    current_time = datetime.datetime.now().time()
    if alarm_clock is not None:
        if current_time > alarm_clock:
            mqtt_client.publish("PI3/commands", "TurnOnBlinking")
            socketio.emit('message_from_server', "alarmClock")
            print("Turn On Alarm clock")
    if (data["measurement"] == "Motion") and (data["value"] is True) and data["name"] == "DPIR1":
        mqtt_client.publish("PI1/commands", "TurnOnDL")
        print("TurnOnDL")
    if (data["measurement"] == "Temperature") and data["name"] == "GDHT":
        mqtt_client.publish("PI2/commands", "GLCD-T:" + str(data["value"]))
    if (data["measurement"] == "Humidity") and data["name"] == "GDHT":
        mqtt_client.publish("PI2/commands", "GLCD-H:" + str(data["value"]))

    point = (
        Point(data["measurement"])
        .tag("simulated", data["simulated"])
        .tag("runs_on", data["runs_on"])
        .tag("name", data["name"])
        .field("measurement", data["value"])
    )
    write_api.write(bucket=bucket, org=org, record=point)


# Route to store dummy data
@app.route('/store_data', methods=['POST'])
def store_data():
    try:
        data = request.get_json()
        store_data(data)
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


def handle_influx_query(query):
    try:
        query_api = influxdb_client.query_api()
        tables = query_api.query(query, org=org)

        container = []
        for table in tables:
            for record in table.records:
                container.append(record.values)

        return jsonify({"status": "success", "data": container})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


@app.route('/simple_query', methods=['GET'])
def retrieve_simple_data():
    query = f"""from(bucket: "{bucket}")
    |> range(start: -10m)"""
    return handle_influx_query(query)

@app.route('/TEST', methods=['POST'])
def turn_on_dl():
    socketio.emit('message_from_server', "TEST")
    return jsonify({"status": "success", "message:": "TEST"})

@app.route('/turnOnBlinking', methods=['POST'])
def turn_on_blinking():
    mqtt_client.publish("PI3/commands", "TurnOnBlinking")
    return jsonify({"status": "success", "message": "Blinking turned on"})
@app.route('/turnOffBlinking', methods=['POST'])
def turn_off_blinking():
    global alarm_clock
    alarm_clock = None
    mqtt_client.publish("PI3/commands", "TurnOffBlinking")
    return jsonify({"status": "success", "message": "Blinking turned off"})

@app.route('/rgbcolor/<color>', methods=['POST'])
def rgb_color(color):
    mqtt_client.publish("PI3/commands", f"RGB_{color}")
    return jsonify({"message": f"RGB color set to {color}"})


@app.route('/set_alarm', methods=['POST'])
def set_alarmclock():
    global alarm_clock
    try:
        data = request.get_json()
        alarm_time = data.get('alarm_time')
        if alarm_time:
            alarm_clock = datetime.datetime.strptime(alarm_time, "%H:%M:%S").time()
            return jsonify({"status": "success", "message": f"Alarm set at {alarm_time}"})
        else:
            return jsonify({"status": "error", "message": "Invalid alarm time"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/aggregate_query', methods=['GET'])
def retrieve_aggregate_data():
    query = f"""from(bucket: "{bucket}")
    |> range(start: -10m)
    |> filter(fn: (r) => r._measurement == "Humidity")
    |> mean()"""
    return handle_influx_query(query)


@socketio.on('message_from_client')
def handle_message(message):
    print('Received message:', message)
    socketio.emit('message_from_server', message)



if __name__ == '__main__':
    socketio.run(app, allow_unsafe_werkzeug=True)
