# fmsa-load-test

## Introduction

Using the Locust do the load testing for FMSA.

## Usage

- Cloning the repository with the `git clone` command.
- Using the `docker build -t fmsa-load-test . --no-cache` command to build the Docker image.
- Running the `docker run -p 8089:8089 -it -v ./data:/opt/data -v ./locustfile.py:/opt/data/locustfile.py fmsa-load-test bash` command to be the interactive Docker container.
- In the interactive Docker container, running the `locust -f ./data/` command to start the web interface.
