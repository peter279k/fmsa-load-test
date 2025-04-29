import os
import json
import time
from locust import HttpUser, task, between

class FHIRConverterConvertUser(HttpUser):
    wait_time = between(1, 5)

    @task()
    def convert_data(self):
        json_file = '/opt/data/sport.raw_data_goldensmarthome_20241212.json'
        if os.path.isfile(json_file) is False:
            raise Exception(f'The {json_file} file is missed.')

        with open(json_file, 'r') as f:
            golden_smart_home_data = f.read()

        module_name = 'GoldenSmartHomeConverter'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        payload = {
            'module_name': module_name,
            'original_data': json.loads(golden_smart_home_data),
        }

        self.client.post('/api/v1/convert', json=payload, headers=headers)
        time.sleep(1)
