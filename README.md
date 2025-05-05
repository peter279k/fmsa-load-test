# fmsa-load-test

## Introduction

Using the Locust to do the load testing for FMSA.

## Usage

- Cloning the repository with the `git clone` command.
- Using the `docker build -t fmsa-load-test . --no-cache` command to build the Docker image.
- Running the following command and it will enter into the interactive Docker container:

```bash
docker run -it -p 8089:8089 \
    -v ./data:/opt/data \
    -v ./locustfile.py:/opt/data/locustfile.py \
    -v ./sport.raw_data_goldensmarthome_20241212.json:/opt/data/sport.raw_data_goldensmarthome_20241212.json \
    fmsa-load-test bash
```

- In the interactive Docker container, running the `locust -f ./data/` command to start the web interface.
