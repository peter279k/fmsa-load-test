# Introduction

- This is the utility for executing the FMSA load tests.
- It's for RQ3 about scaling up/down for the FMSA.

## Prerequisites

- Ensuring the `Docker` engine is installed and the `docker` command is available.
- If the `Docker` engine is not available, it should ensure the `venv` module is available.

## RQ3 Setup

- Running the `python3 -m venv fmsa-load-test-experiments` command to create the virtual environment for the experiment.
- Running the `source fmsa-load-test-experiments/bin/activate` to change the above virtual environment.
- Running the `pip install -r requiremnets.txt` to install required Python packages.
- Executing the `cd experiments/` command to ensure the current working directory is `experiments`.
- Running the `python pre_upload_required_references.py` command to upload and store required reference resources.
- Available load tests are as follows:

    1. analyze_upload_retrieve_questionnaire_response_cdr_data_scenario4.py
    2. convert_upload_retrieve_adverse_event_data_scenario6.py
    3. convert_upload_retrieve_location_data_scenario5.py
    4. convert_upload_retrieve_medication_administration_data_scenario3.py
    5. convert_upload_retrieve_observation_scenario1.py
    6. convert_upload_retrieve_procedure_scenario2.py

- Running the following command to execute the specific load test:

```bash
locust -f {load_test_file.py} --headless \
    --host https://{your-fmsa-host} \
    --users 1000 \
    --spawn-rate 1.11 \
    --run-time 20m
```
