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
    wait_time = constant(10)

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
        response_json_data = [{'resourceType': 'Procedure', 'id': '441b992ffcecf6aef9522574f4cc856403f9439a9fe115504139285b', 'status': 'completed', 'code': {'coding': [{'system': 'http://snomed.info/sct', 'code': '225964003', 'display': 'Assisting with personal hygiene'}], 'text': '個人衛生協助'}, 'subject': {'reference': 'Patient/ltc-patient-chen-ming-hui'}, 'performedDateTime': '2025-03-01T08:00+08:00', 'performer': [{'actor': {'reference': 'PractitionerRole/ltc-practitioner-role-nurse-example'}}], 'note': [{'time': '2025-03-01T08:00+08:00', 'text': '合作度佳，情緒穩定'}]}, {'resourceType': 'Procedure', 'id': '9efde6760da197c595a7e868f944c12448f56fc772dfda2efa786372', 'status': 'completed', 'code': {'coding': [{'system': 'http://snomed.info/sct', 'code': '226010006', 'display': 'Assisting with eating and drinking'}], 'text': '進食協助'}, 'subject': {'reference': 'Patient/ltc-patient-chen-ming-hui'}, 'performedDateTime': '2025-03-01T09:30+08:00', 'performer': [{'actor': {'reference': 'PractitionerRole/ltc-practitioner-role-nurse-example'}}], 'note': [{'time': '2025-03-01T09:30+08:00', 'text': '食慾尚可，吞嚥速度較慢'}]}, {'resourceType': 'Procedure', 'id': 'dd0cd9e66d1584f84b52aaf7e90c86b0a383f0c62ebfeb961c9a239a', 'status': 'completed', 'code': {'coding': [{'system': 'http://snomed.info/sct', 'code': '713138001', 'display': 'Assistance with mobility in bed'}], 'text': '床上移動協助'}, 'subject': {'reference': 'Patient/ltc-patient-chen-ming-hui'}, 'performedDateTime': '2025-03-02T10:00+08:00', 'performer': [{'actor': {'reference': 'PractitionerRole/ltc-practitioner-role-nurse-example'}}], 'note': [{'time': '2025-03-02T10:00+08:00', 'text': '皮膚完整，無紅疹或壓瘡'}]}, {'resourceType': 'Procedure', 'id': '08a28a5172789e56fe172e81cbfb38dc82b765689888b1dd7b39ac20', 'status': 'completed', 'code': {'coding': [{'system': 'http://snomed.info/sct', 'code': '223454002', 'display': 'Escorting subject to toilet'}], 'text': '如廁協助'}, 'subject': {'reference': 'Patient/ltc-patient-chen-ming-hui'}, 'performedDateTime': '2025-03-02T14:00+08:00', 'performer': [{'actor': {'reference': 'PractitionerRole/ltc-practitioner-role-nurse-example'}}], 'note': [{'time': '2025-03-02T14:00+08:00', 'text': '排尿量正常，顏色清澈'}]}, {'resourceType': 'Procedure', 'id': 'cab4ddd3086c61c2492995eeb4e7c18237ae8ceb78ec3b53102febf1', 'status': 'completed', 'code': {'coding': [{'system': 'http://snomed.info/sct', 'code': '710803000', 'display': 'Assistance with mobility'}], 'text': '移位/移動協助'}, 'subject': {'reference': 'Patient/ltc-patient-chen-ming-hui'}, 'performedDateTime': '2025-03-03T09:00+08:00', 'performer': [{'actor': {'reference': 'PractitionerRole/ltc-practitioner-role-nurse-example'}}], 'note': [{'time': '2025-03-03T09:00+08:00', 'text': '移位過程配合度良好，無跌倒風險'}]}, {'resourceType': 'Procedure', 'id': '4d330e64256e0feb3e64a8d6b7612bed6f0a75c454a34a316dc5d4c9', 'status': 'completed', 'code': {'coding': [{'system': 'http://snomed.info/sct', 'code': '733923007', 'display': 'Change of diaper'}], 'text': '更換尿布'}, 'subject': {'reference': 'Patient/ltc-patient-chen-ming-hui'}, 'performedDateTime': '2025-03-03T16:00+08:00', 'performer': [{'actor': {'reference': 'PractitionerRole/ltc-practitioner-role-nurse-example'}}], 'note': [{'time': '2025-03-03T16:00+08:00', 'text': '皮膚無紅疹，狀況良好'}]}, {'resourceType': 'Procedure', 'id': 'f452756d6f44bfff3fe6cef85bd962609a001593a123dfb50c23888a', 'status': 'completed', 'code': {'coding': [{'system': 'http://snomed.info/sct', 'code': '60369001', 'display': 'Bathing patient'}], 'text': '沐浴/擦澡'}, 'subject': {'reference': 'Patient/ltc-patient-chen-ming-hui'}, 'performedDateTime': '2025-03-04T11:00+08:00', 'performer': [{'actor': {'reference': 'PractitionerRole/ltc-practitioner-role-nurse-example'}}], 'note': [{'time': '2025-03-04T11:00+08:00', 'text': '皮膚乾燥，已塗抹乳液保濕'}]}, {'resourceType': 'Procedure', 'id': 'ba4ee2b99943ea32024d1df95bbf800e22783651c3682b79181403c3', 'status': 'completed', 'code': {'coding': [{'system': 'http://snomed.info/sct', 'code': '313332003', 'display': 'Dressing patient'}], 'text': '穿衣'}, 'subject': {'reference': 'Patient/ltc-patient-chen-ming-hui'}, 'performedDateTime': '2025-03-04T15:30+08:00', 'performer': [{'actor': {'reference': 'PractitionerRole/ltc-practitioner-role-nurse-example'}}], 'note': [{'time': '2025-03-04T15:30+08:00', 'text': '情緒配合，右肩活動度略受限'}]}, {'resourceType': 'Procedure', 'id': 'e7e3391a79051a6e056af6fd296c938d9ab9b79e905ee0cccb29d4c9', 'status': 'completed', 'code': {'coding': [{'system': 'http://snomed.info/sct', 'code': '313420001', 'display': 'Assisting with toileting'}], 'text': '陪同到廁所'}, 'subject': {'reference': 'Patient/ltc-patient-chen-ming-hui'}, 'performedDateTime': '2025-03-05T07:30+08:00', 'performer': [{'actor': {'reference': 'PractitionerRole/ltc-practitioner-role-nurse-example'}}], 'note': [{'time': '2025-03-05T07:30+08:00', 'text': '步態穩定，可自行如廁'}]}, {'resourceType': 'Procedure', 'id': 'd6f4ad06a6b7dee47b757bc3ac4ede821895dc5b52abf868037c4a5e', 'status': 'completed', 'code': {'coding': [{'system': 'http://snomed.info/sct', 'code': '225964003', 'display': 'Assisting with personal hygiene'}], 'text': '個人衛生協助'}, 'subject': {'reference': 'Patient/ltc-patient-chen-ming-hui'}, 'performedDateTime': '2025-03-05T19:00+08:00', 'performer': [{'actor': {'reference': 'PractitionerRole/ltc-practitioner-role-nurse-example'}}], 'note': [{'time': '2025-03-05T19:00+08:00', 'text': '情緒平靜，表示願意休息'}]}]
        payload = {
            'resource': response_json_data[0],
        }

        with self.client.put(
            f'/api/v1/update/Procedure',
            headers=self.headers, json=payload,
            name='PUT /api/v1/update/Procedure',
            catch_response=True,
        ) as response:
            if response.status_code in (200, 201):
                response.success()
            else:
                response.failure(f'Unexpected status code: {response.status_code}')
