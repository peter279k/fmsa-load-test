# fmsa-load-test

## Introduction

Using the Locust to do the load testing for FMSA.

## Prerequisite

- Ensuring the Docker Swarm Cluster has been deployed.
- Ensuring the FMSA has been deployed with the Docker Stack mode in the Swarm Cluster.
- Ensuring the Swarm Automatic Scaler has been deployed in the Swarm CLuster.
  - It can run these following commands to complete this step:

```bash
$ wget https://github.com/AMEST/swarm-autoscaler/raw/refs/heads/master/swarm-deploy.yml
$ docker stack deploy -c swarm-deploy.yml ascaler
```

## Usage (for Single Cluster)

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

## Usage (for Docker Swarm Clusters)

- Please refer this [README](experiments/README.md).
