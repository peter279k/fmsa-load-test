import json
import httpx


def upload_required_references():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    with open('./data/Practitioner-ltc-practitioner-physician-aa12-example.json')as f:
        json_str = f.read()

    json_dict = json.loads(json_str)
    del json_dict['meta']
    del json_dict['text']

    payload = {
        'resource': json_dict,
    }
    response = httpx.put('http://localhost:8081/api/v1/update/Practitioner', headers=headers, json=payload)

    assert response.status_code == 201 or response.status_code == 200


    with open('./data/Practitioner-ltc-practitioner-nurse-example.json') as f:
        json_str = f.read()

    json_dict = json.loads(json_str)
    del json_dict['meta']
    del json_dict['text']

    payload = {
        'resource': json_dict,
    }
    response = httpx.put('http://localhost:8081/api/v1/update/Practitioner', headers=headers, json=payload)

    assert response.status_code == 201 or response.status_code == 200

    with open('./data/Organization-ltc-organization-example.json') as f:
        json_str = f.read()

    json_dict = json.loads(json_str)
    del json_dict['meta']
    del json_dict['text']

    payload = {
        'resource': json_dict,
    }
    response = httpx.put('http://localhost:8081/api/v1/update/Organization', headers=headers, json=payload)

    assert response.status_code == 201 or response.status_code == 200

    with open('./data/PractitionerRole-ltc-practitioner-role-nurse-example.json') as f:
        json_str = f.read()

    json_dict = json.loads(json_str)
    del json_dict['meta']
    del json_dict['text']

    payload = {
        'resource': json_dict,
    }
    response = httpx.put('http://localhost:8081/api/v1/update/PractitionerRole', headers=headers, json=payload)

    assert response.status_code == 201 or response.status_code == 200

    with open('./data/Patient-ltc-patient-chen-ming-hui.json') as f:
        json_str = f.read()

    json_dict = json.loads(json_str)
    del json_dict['meta']
    del json_dict['text']

    payload = {
        'resource': json_dict,
    }
    response = httpx.put('http://localhost:8081/api/v1/update/Patient', headers=headers, json=payload)

    assert response.status_code == 201 or response.status_code == 200

    with open('./data/Practitioner-ltc-practitioner-example.json') as f:
        json_str = f.read()

    json_dict = json.loads(json_str)
    del json_dict['meta']
    del json_dict['text']

    payload = {
        'resource': json_dict,
    }
    response = httpx.put('http://localhost:8081/api/v1/update/Practitioner', headers=headers, json=payload)

    assert response.status_code == 201 or response.status_code == 200

    with open('./data/Location-ltc-location-example.json') as f:
        json_str = f.read()

    json_dict = json.loads(json_str)
    del json_dict['meta']
    del json_dict['text']

    payload = {
        'resource': json_dict,
    }
    response = httpx.put('http://localhost:8081/api/v1/update/Location', headers=headers, json=payload)

    assert response.status_code == 201 or response.status_code == 200


if __name__ == '__main__':
    print('Uploading required references before executing FMSA Load Test')
    upload_required_references()
    print('Uploading has been done')
