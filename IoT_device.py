import paho.mqtt.client as mqtt
import ssl
from dotenv import load_dotenv
import random
import time
import json
import os

load_dotenv()
# AWS IoT Core endpoint configuration
broker = "a29uuva9web2cu-ats.iot.us-east-1.amazonaws.com"
port = 8883
client_id = "temperature_sensor_1"
topic = "iot/sensor/temperature"

# Paths to certificates
ca_path = os.getenv("AWS_CA_PATH")
cert_path = os.getenv("AWS_CERT_PATH")
key_path = os.getenv("AWS_KEY_PATH")

# MQTT client setup
client = mqtt.Client(client_id, protocol=mqtt.MQTTv311)

client.tls_set(ca_certs=ca_path, certfile=cert_path, keyfile=key_path, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2)

# Connect to the broker
client.connect(broker, port)
client.loop_start()
# Function to publish temperature data
def publish_data():
    while True:
        temperature = round(random.uniform(20.0, 25.0), 2)
        payload = json.dumps({"temperature": temperature})
        client.publish(topic, payload)
        print(f"Published {payload} to {topic}")
        time.sleep(10)

# Run the simulation
publish_data()
