#!/bin/bash

echo "Executing Load Test is started!"

cd ~/fmsa
if [[ ! -d ./fmsa-venv ]]; then
    python3 -m venv fmsa-venv
fi;

./fmsa-venv/bin/pip install -r api_gateway/requirements.txt
./fmsa-venv/bin/pip install -r api_gateway/requirements-dev.txt

cd ~/fmsa-load-test/experiments

if [[ ! -d ./fmsa-load-test-experiments ]]; then
    python3 -m venv fmsa-load-test-experiments
fi;

./fmsa-load-test-experiments/bin/pip install -r ../requirements.txt


host=$1
index=$2
path="scenarios.txt"

if [[ ! -f "$path" ]]; then
    echo "$path file is not found."
    exit 1;
fi;

for file_name in $(cat $path)
do
    docker stack rm fmsa
    sleep 300
    docker volume rm $(docker volume ls | grep fmsa | awk '{print $2}')

    cd ~/fmsa

    set -a && source .env && set +a && docker stack deploy --compose-file docker-compose.yml fmsa

    cd ~/swarm-auto-scaler/scaler
    ./deploy.sh

    sleep 600

    cd ~/fmsa-load-test/experiments
    for _ in $(seq 1 5)
    do
        ./fmsa-load-test-experiments/bin/python pre_upload_required_references.py
    done;

    csv_result=$(echo $file_name | awk '{split($1,a,"."); print a[1]}')
    ./fmsa-load-test-experiments/bin/locust -f $file_name --headless \
        --host "http://$host" \
        --users 1000 \
        --spawn-rate 1.11 \
        --run-time 20m \
        --csv="$csv_result"
done;

echo "Executing Load Test is done!"
