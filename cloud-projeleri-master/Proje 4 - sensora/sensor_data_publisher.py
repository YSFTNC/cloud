import json
import time
import random
from google.cloud import pubsub_v1
import os

project_id = "sensora-460619"
topic_id = "iot-sensor-data"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

print(f"Data will be sent to topic '{topic_id}' in project '{project_id}'.")
print(f"Environment variable GOOGLE_APPLICATION_CREDENTIALS: {os.getenv('GOOGLE_APPLICATION_CREDENTIALS')}")

def publish_sensor_data():
    temperature = round(random.uniform(20.0, 30.0), 2)
    humidity = round(random.uniform(40.0, 60.0), 2)
    device_id = "sensor-001"
    timestamp = int(time.time())

    data = {
        "temperature": temperature,
        "humidity": humidity,
        "device_id": device_id,
        "timestamp": timestamp
    }

    data_json = json.dumps(data).encode("utf-8")
    future = publisher.publish(topic_path, data_json)
    print(f"Published message ID: {future.result()} - Data: {data}")

if __name__ == "__main__":
    print("Sensor data publisher started. Press Ctrl+C to stop.")
    try:
        while True:
            publish_sensor_data()
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nSensor data publisher stopped.")
