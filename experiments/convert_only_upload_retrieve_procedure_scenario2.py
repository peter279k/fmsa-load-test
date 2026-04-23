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


class LtcTWSC2(HttpUser):
    wait_time = constant(0)

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

    @task
    def ltc_tw_sc2(self):
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
