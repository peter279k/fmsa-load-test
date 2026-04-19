import json
import hashlib
import secrets
from locust import HttpUser, constant, events, task


@events.test_start.add_listener
def on_test_start(environment):
    parsed = environment.parsed_options
    print(
        f'\n[Config] Target Concurrent users：{parsed.num_users} │ '
        f'Spawn Rate：{parsed.spawn_rate}/s │ '
        f'Executed Time：{parsed.run_time}s\n'
    )


class LtcTWSC4(HttpUser):
    wait_time = constant(0)

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

    @task
    def ltc_tw_sc4(self):
        with self.client.post(
            f'/api/v1/analyze',
            headers=self.headers,
            json=self.payload,
            name='POST /api/v1/analyze',
            catch_response=True,
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f'Unexpected status code: {response.status_code}')

        questionnaire_response_id = hashlib.sha3_224(secrets.token_urlsafe(5).encode('utf-8')).hexdigest()
        self.json_data[0]['id'] = questionnaire_response_id
        payload = {
            'resource': self.json_data[0],
        }

        with self.client.put(
            '/api/v1/update/QuestionnaireResponse',
            headers=self.headers,
            json=payload,
            name='PUT /api/v1/update/QuestionnaireResponse',
            catch_response=True
        ) as response:
            if response.status_code == 201:
                response.success()
            else:
                response.failure(f'Unexpected status code: {response.status_code}')

        with self.client.get(
            f'/api/v1/retrieve/QuestionnaireResponse?_id={questionnaire_response_id}',
            headers=self.headers,
            name=f'GET /api/v1/retrieve/QuestionnaireResponse?_id={questionnaire_response_id}',
            catch_response=True
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f'Unexpected status code: {response.status_code}')
