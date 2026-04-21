import json
import httpx
import hashlib
import secrets


class LtcTWSC3:
    def on_start(self):
        with open('./data/medication_administration.json') as f:
            medication_admin_data = f.read()

        self.medication_lists = json.loads(medication_admin_data)['用藥紀錄']
        self.module_name = 'MedicationAdministrationLtcConverter'
        self.payload = {
            'module_name': self.module_name,
            'original_data': self.medication_lists,
        }
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'x-api-key': 'API Key',
            'x-user': 'User',
        }

    def ltc_tw_sc3(self):
        response = httpx.post(
            f'/api/v1/convert',
            headers=self.headers,
            json=self.payload
        )
        assert response.status_code == 200

        response_json = response.json()
        response_json_data = response_json['data'][0]

        medication_admin_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        response_json_data[0]['id'] = medication_admin_id
        payload = {
            'resource': response_json_data[0],
        }
        response = httpx.put(
            f'/api/v1/update/MedicationAdministration',
            headers=self.headers,
            json=payload
        )

        assert response.status_code == 201

        response = httpx.get(
            f'/api/v1/retrieve/MedicationAdministration?_id={medication_admin_id}',
            headers=self.headers
        )
        assert response.status_code == 200
