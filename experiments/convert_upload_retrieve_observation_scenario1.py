import os
import json
import time
from locust import HttpUser, task, between


class LtcTWSC1(HttpUser):
    wait_time = between(1, 5)

    @task()
    def convert_data(self):
        host = 'http://localhost:8081'
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'x-api-key': 'API Key',
            'x-user': 'User',
        }
        payload = {
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

        with open('/app/app/tests/scenarios/Observation-ltc-observation-blood-pressure-example.json', 'r', encoding='utf-8') as f:
            expected_json_str = f.read()

            expected_json = json.loads(expected_json_str)
            del expected_json['text']
            del expected_json['id']

            json_dict = {}
            json_dict['payload'] = payload
            httpx.post(f'{host}/api/v1/ltc_tw_2025_observation_blood_pressure', headers=headers, json=json_dict)

            response_json = response.json()
            observation_id = response_json['data'][0]['id']
            del response_json['data'][0]['id']

            httpx.get(f'{host}/api/v1/retrieve/Observation?_id={observation_id}', headers=headers)
