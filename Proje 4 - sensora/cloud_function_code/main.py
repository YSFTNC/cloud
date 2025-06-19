import base64
import json
from google.cloud import firestore
import datetime
import functions_framework
from google.cloud import bigquery

db = firestore.Client()
bq_client = bigquery.Client()
dataset_id = 'sensora_dataset'
table_id = 'sensor_readings'
table_ref = bq_client.dataset(dataset_id).table(table_id)

def changed(old, new):
    """Değişiklik %5'ten büyükse True döner"""
    if old is None or old == 0:
        return True
    diff = abs(new - old) / abs(old) * 100
    return diff >= 5

def save_to_bigquery(data):
    """Veriyi BigQuery'ye kaydet"""
    try:
        timestamp_value = data.get("timestamp")
        if timestamp_value:
            timestamp_dt = datetime.datetime.utcfromtimestamp(timestamp_value)
        else:
            timestamp_dt = datetime.datetime.utcnow()

        rows_to_insert = [
            {
                "temperature": data.get("temperature"),
                "humidity": data.get("humidity"),
                "device_id": data.get("device_id"),
                "timestamp": timestamp_dt.isoformat()
            }
        ]
        
        errors = bq_client.insert_rows_json(table_ref, rows_to_insert)
        if errors:
            print(f"BigQuery insert errors: {errors}")
            return False
        else:
            print("Data inserted into BigQuery successfully.")
            return True
    except Exception as e:
        print(f"BigQuery insert exception: {e}")
        return False

@functions_framework.cloud_event
def process_sensor_data(cloud_event):
    """Pub/Sub mesajını işle ve Firestore + BigQuery'ye kaydet"""
    try:
        if 'message' in cloud_event.data and 'data' in cloud_event.data['message']:
            pubsub_message_data = base64.b64decode(cloud_event.data['message']['data']).decode('utf-8')
            sensor_data = json.loads(pubsub_message_data)

            print(f"Received message: {sensor_data}")

            timestamp_value = sensor_data.get('timestamp')
            if timestamp_value is not None:
                timestamp_dt = datetime.datetime.fromtimestamp(timestamp_value)
            else:
                timestamp_dt = datetime.datetime.now()
                print("Warning: 'timestamp' not found or invalid in message. Using current time.")

            device_id = sensor_data.get('device_id')
            if not device_id:
                print("Warning: 'device_id' not found. Skipping data.")
                return
            
            collection_name = 'sensor_readings'
            docs = db.collection(collection_name).where('device_id', '==', device_id).order_by('timestamp', direction=firestore.Query.DESCENDING).limit(1).stream()
            
            last_doc = None
            for doc in docs:
                last_doc = doc.to_dict()

            if last_doc:
                last_temp = last_doc.get('temperature')
                last_humidity = last_doc.get('humidity')

                if not (changed(last_temp, sensor_data.get('temperature')) or 
                       changed(last_humidity, sensor_data.get('humidity'))):
                    print("Değişiklik %5 altında, veri yazılmadı.")
                    return

            doc_data = {
                'temperature': sensor_data.get('temperature'),
                'humidity': sensor_data.get('humidity'),
                'device_id': device_id,
                'timestamp': timestamp_dt
            }

            doc_ref = db.collection(collection_name).document()
            doc_ref.set(doc_data)
            print(f"Data saved to Firestore. Document ID: {doc_ref.id}")

            save_to_bigquery(sensor_data)

        else:
            print("No data or message found in Pub/Sub cloud event.")
            raise ValueError("No data or message found in Pub/Sub cloud event.")
            
    except Exception as e:
        print(f"Error processing sensor data: {e}")
        raise