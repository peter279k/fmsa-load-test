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


class LtcTWSC5(HttpUser):
    wait_time = constant(0)

    def on_start(self):
        with open('./data/location.json') as f:
            ltc_location_data = f.read()

        self.module_name = 'LocationLtcConverter'
        self.payload = {
            'module_name': self.module_name,
            'original_data': json.loads(ltc_location_data),
        }
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'x-api-key': 'API Key',
            'x-user': 'User',
        }

    @task
    def ltc_tw_sc5(self):
        response_json_data = [{'resourceType': 'Location', 'id': '87293027c23ede8218ae08d8ed741035920fdec629a0ae9518fbf1dc', 'status': 'active', 'name': '王大明', 'description': '日照中心', 'mode': 'instance', 'type': [{'coding': [{'system': 'http://terminology.hl7.org/CodeSystem/v3-RoleCode', 'code': 'PTRES', 'display': "Patient's Residence"}]}], 'address': {'use': 'work', 'type': 'physical', 'text': '新北市中和區安康路二段123號'}, 'position': {'longitude': 121.517, 'latitude': 25.0478, 'altitude': 25.5}}, {'resourceType': 'Location', 'id': '604019bacc73ec8820c23436a181cd0f4ad137d364840779de2f0e71', 'status': 'active', 'name': '李美珍', 'description': '家裡', 'mode': 'instance', 'type': [{'coding': [{'system': 'http://terminology.hl7.org/CodeSystem/v3-RoleCode', 'code': 'PTRES', 'display': "Patient's Residence"}]}], 'address': {'use': 'work', 'type': 'physical', 'text': '新北市中和區安康路二段124號'}, 'position': {'longitude': 121.5654, 'latitude': 25.033, 'altitude': 25.5}}, {'resourceType': 'Location', 'id': '6d8e83e6ee54f894f56556512dc154fc58b651e8694a9613a17ceb97', 'status': 'active', 'name': '陳志豪', 'description': '公園', 'mode': 'instance', 'type': [{'coding': [{'system': 'http://terminology.hl7.org/CodeSystem/v3-RoleCode', 'code': 'PTRES', 'display': "Patient's Residence"}]}], 'address': {'use': 'work', 'type': 'physical', 'text': '新北市中和區安康路二段125號'}, 'position': {'longitude': 121.5773, 'latitude': 25.0796, 'altitude': 25.5}}, {'resourceType': 'Location', 'id': '22322f1572f1fca5b06208077a83eecf072713b9c9ff1ee3c05ceba2', 'status': 'active', 'name': '林淑芬', 'description': '醫院', 'mode': 'instance', 'type': [{'coding': [{'system': 'http://terminology.hl7.org/CodeSystem/v3-RoleCode', 'code': 'PTRES', 'display': "Patient's Residence"}]}], 'address': {'use': 'work', 'type': 'physical', 'text': '新北市中和區安康路二段126號'}, 'position': {'longitude': 121.5397, 'latitude': 25.0173, 'altitude': 25.5}}, {'resourceType': 'Location', 'id': 'fd9521c63b6fb1887ca6e24e0a0e78e4fa208e30c2ad6134f3900c19', 'status': 'active', 'name': '黃俊傑', 'description': '長照機構', 'mode': 'instance', 'type': [{'coding': [{'system': 'http://terminology.hl7.org/CodeSystem/v3-RoleCode', 'code': 'PTRES', 'display': "Patient's Residence"}]}], 'address': {'use': 'work', 'type': 'physical', 'text': '新北市中和區安康路二段127號'}, 'position': {'longitude': 121.5353, 'latitude': 25.0609, 'altitude': 25.5}}, {'resourceType': 'Location', 'id': '51cf972085325a61130acf215e874d85b44d5db2147db641e04f2ba5', 'status': 'active', 'name': '張雅婷', 'description': '社區活動中心', 'mode': 'instance', 'type': [{'coding': [{'system': 'http://terminology.hl7.org/CodeSystem/v3-RoleCode', 'code': 'PTRES', 'display': "Patient's Residence"}]}], 'address': {'use': 'work', 'type': 'physical', 'text': '新北市中和區安康路二段128號'}, 'position': {'longitude': 121.4953, 'latitude': 25.0452, 'altitude': 25.5}}, {'resourceType': 'Location', 'id': '907ea1d1cabf78f57a93cfbae94850ed44eac3771499457cf8d183c9', 'status': 'active', 'name': '吳建國', 'description': '家裡', 'mode': 'instance', 'type': [{'coding': [{'system': 'http://terminology.hl7.org/CodeSystem/v3-RoleCode', 'code': 'PTRES', 'display': "Patient's Residence"}]}], 'address': {'use': 'work', 'type': 'physical', 'text': '新北市中和區安康路二段129號'}, 'position': {'longitude': 121.5601, 'latitude': 25.0891, 'altitude': 25.5}}, {'resourceType': 'Location', 'id': 'f8c4d7e39f3bd1c429852a8b42e7c49f5f09b752afb0d5d5370fcefe', 'status': 'active', 'name': '劉美惠', 'description': '復健診所', 'mode': 'instance', 'type': [{'coding': [{'system': 'http://terminology.hl7.org/CodeSystem/v3-RoleCode', 'code': 'PTRES', 'display': "Patient's Residence"}]}], 'address': {'use': 'work', 'type': 'physical', 'text': '新北市中和區安康路二段130號'}, 'position': {'longitude': 121.5433, 'latitude': 25.0264, 'altitude': 25.5}}, {'resourceType': 'Location', 'id': '0beb2e46f5f1f749344e249f44944759e57e776a0da21de8bf5eb5c1', 'status': 'active', 'name': '蔡文雄', 'description': '老人福利中心', 'mode': 'instance', 'type': [{'coding': [{'system': 'http://terminology.hl7.org/CodeSystem/v3-RoleCode', 'code': 'PTRES', 'display': "Patient's Residence"}]}], 'address': {'use': 'work', 'type': 'physical', 'text': '新北市中和區安康路二段131號'}, 'position': {'longitude': 121.6012, 'latitude': 25.0537, 'altitude': 25.5}}, {'resourceType': 'Location', 'id': 'c12db8f69fd87e9530de393a3820d065b21942b5087733f2efde075d', 'status': 'active', 'name': '周秀蘭', 'description': '家裡', 'mode': 'instance', 'type': [{'coding': [{'system': 'http://terminology.hl7.org/CodeSystem/v3-RoleCode', 'code': 'PTRES', 'display': "Patient's Residence"}]}], 'address': {'use': 'work', 'type': 'physical', 'text': '新北市中和區安康路二段132號'}, 'position': {'longitude': 121.4874, 'latitude': 25.0712, 'altitude': 25.5}}]
        payload = {
            'resource': response_json_data[0],
        }

        with self.client.put(
            '/api/v1/update/Location',
            headers=self.headers,
            json=payload,
            name='PUT /api/v1/update/Location',
            catch_response=True
        ) as response:
            if response.status_code == 201:
                response.success()
            else:
                response.failure(f'Unexpected status code: {response.status_code}')
