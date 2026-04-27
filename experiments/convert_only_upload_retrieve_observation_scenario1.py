from locust import HttpUser, constant, events, task


@events.test_start.add_listener
def on_test_start(environment):
    parsed = environment.parsed_options
    print(
        f'\n[Config] Target Concurrent users：{parsed.num_users} │ '
        f'Spawn Rate：{parsed.spawn_rate}/s │ '
        f'Executed Time：{parsed.run_time}s\n'
    )


class LtcTWSC1(HttpUser):
    wait_time = constant(20)

    def on_start(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'x-api-key': 'API Key',
            'x-user': 'User',
        }

        self.payload = {
            'resourceType': 'Observation',
            'profile_urls': ['http://ltc-ig.fhir.tw/StructureDefinition/LTCObservationVitalSigns'],
            'status': 'final',
            'category_coding': [{
                'system': 'http://terminology.hl7.org/CodeSystem/observation-category',
                'code': 'vital-signs',
                'display': 'Vital Signs'
            }],
            'code_coding': [{
                'system': 'http://loinc.org',
                'code': '85354-9',
                'display': 'Blood pressure panel with all children optional'
            }],
            'code_text': '血壓',
            'subject': {
                'reference': 'Patient/ltc-patient-chen-ming-hui'
            },
            'effective_datetime': '2024-01-15T09:00:00+08:00',
            'performer': [{
                'reference': 'PractitionerRole/ltc-practitioner-role-nurse-example'
            }],
            'component': [{
                'code': {
                    'coding': [{
                        'system': 'http://loinc.org',
                        'code': '8480-6',
                        'display': 'Systolic blood pressure'
                    }]
                },
                'valueQuantity': {
                    'value': 135,
                    'unit': 'mmHg',
                    'system': 'http://unitsofmeasure.org',
                    'code': 'mm[Hg]'
                }
            },
            {
                'code': {
                    'coding': [{
                        'system': 'http://loinc.org',
                        'code': '8462-4',
                        'display': 'Diastolic blood pressure'
                    }]
                },
                'valueQuantity': {
                    'value': 85,
                    'unit': 'mmHg',
                    'system': 'http://unitsofmeasure.org',
                    'code': 'mm[Hg]'
                }
            }]
        }

    @task
    def ltc_tw_sc1(self):
        json_dict = {}
        json_dict['payload'] = self.payload

        with self.client.post(
            '/api/v1/ltc_tw_2025_observation_blood_pressure',
            headers=self.headers,
            json=json_dict,
            name='POST /api/v1/ltc_tw_2025_observation_blood_pressure',
            catch_response=True
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f'Unexpected status code: {response.status_code}')
