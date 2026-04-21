import json
import httpx
import hashlib
import secrets


class LtcTWSC2():
    def on_start(self):
        with open('./data/procedure.json') as f:
            self.procedure_data = f.read()

        self.module_name = 'ProcedureLtcConverter'
        self.payload = {
            'module_name': self.module_name,
            'original_data': json.loads(self.procedure_data),
        }
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'x-api-key': 'API Key',
            'x-user': 'User',
        }
        self.host = 'http://127.0.0.1:8081'

    def ltc_tw_sc2(self):
        response = httpx.post(
            f'{self.host}/api/v1/convert',
            headers=self.headers,
            json=self.payload,
        )
        response_json = response.json()
        response_json_data = response_json['data'][0]

        assert response.status_code == 200

        procedure_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        response_json_data[0]['id'] = procedure_id
        payload = {
            'resource': response_json_data[0],
        }

        response = httpx.put(
            f'{self.host}/api/v1/update/Procedure',
            headers=self.headers,
            json=payload,
        )
        assert response.status_code == 201

        response = httpx.get(
            f'{self.host}/api/v1/retrieve/Procedure?_id={procedure_id}',
            headers=self.headers
        )
        assert response.status_code == 200


if __name__ == '__main__':
    sc2 = LtcTWSC2
    sc2.on_start()
    sc2.ltc_tw_sc2()
