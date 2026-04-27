import json
from locust import HttpUser, constant, events, task


@events.test_start.add_listener
def on_test_start(environment):
    parsed = environment.parsed_options
    print(
        f'\n[Config] Target Concurrent users：{parsed.num_users} │ '
        f'Spawn Rate：{parsed.spawn_rate}/s │ '
        f'Executed Time：{parsed.run_time}s\n'
    )


class LtcTWSC3(HttpUser):
    wait_time = constant(20)

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

    @task
    def ltc_tw_sc3(self):
        with self.client.post(
            f'/api/v1/convert',
            headers=self.headers,
            json=self.payload,
            name='POST /api/v1/convert',
            catch_response=True
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f'Unexpected status code: {response.status_code}')
