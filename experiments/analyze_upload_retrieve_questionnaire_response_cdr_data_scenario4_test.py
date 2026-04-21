import json
import httpx
import hashlib
import secrets


class LtcTWSC4:
    def on_start(self):
        self.module_name = 'CdrStatistics'
        self.json_data = []
        self.cdr_files = [
            'QuestionnaireResponse-ltc-questionnaire-response-cdr-complete-example.json',
            'QuestionnaireResponse-ltc-questionnaire-response-cdr-example.json',
            'QuestionnaireResponse-ltc-questionnaire-response-cdr-moderate-example.json',
        ]
        for cdr_file in self.cdr_files:
            with open(f'./data/{cdr_file}') as f:
                contents = f.read()
                self.json_data += json.loads(contents),

        self.payload = {
            'module_name': self.module_name,
            'data': self.json_data,
            'params': {},
        }

        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'x-api-key': 'API Key',
            'x-user': 'User',
        }
        self.host = 'http://127.0.0.1:8081'

    def ltc_tw_sc4(self):
        response = httpx.post(
            f'{self.host}/api/v1/analyze',
            headers=self.headers,
            json=self.payload
        )
        assert response.status_code == 200

        questionnaire_response_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        self.json_data[0]['id'] = questionnaire_response_id
        payload = {
            'resource': self.json_data[0],
        }

        response = httpx.put(
            f'{self.host}/api/v1/update/QuestionnaireResponse',
            headers=self.headers,
            json=payload
        )
        assert response.status_code == 201

        response = httpx.get(
            f'{self.host}/api/v1/retrieve/QuestionnaireResponse?_id={questionnaire_response_id}',
            headers=self.headers
        )
        assert response.status_code == 200
