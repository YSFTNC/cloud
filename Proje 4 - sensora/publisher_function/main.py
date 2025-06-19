import json
import time
import random
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
PROJECT_ID = "sensora-460619"
TOPIC_ID = "iot-sensor-data"
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

def publish_sensor_data(request):
    try:
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
        message_id = future.result()

        return (json.dumps({
            "message_id": message_id,
            "data": data
        }), 200, {'Content-Type': 'application/json'})

    except Exception as e:
        return (json.dumps({"error": str(e)}), 500, {'Content-Type': 'application/json'})
