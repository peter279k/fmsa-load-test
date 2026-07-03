#!/bin/bash

echo "Executing Load Test is started!"

host=$1
export SSHPASS=$2
host_name=$3

# Prerequisite
# ssh "$USER@$host_name"
# Run: cd ~/fmsa

#if [[ ! -d ./fmsa-venv ]]; then
#    python3 -m venv fmsa-venv
#fi;

#./fmsa-venv/bin/pip install -r api_gateway/requirements.txt
#./fmsa-venv/bin/pip install -r api_gateway/requirements-dev.txt

cd ~/fmsa-load-test/experiments

if [[ ! -d ./fmsa-load-test-experiments ]]; then
    python3 -m venv fmsa-load-test-experiments
fi;

./fmsa-load-test-experiments/bin/pip install -r ../requirements.txt


path="scenarios.txt"

if [[ ! -f "$path" ]]; then
    echo "$path file is not found."
    exit 1;
fi;

for file_name in $(cat $path)
do
    sshpass -e ssh -o StrictHostKeyChecking=no "$USER@$host_name" 'cd fmsa && docker compose down'
    sleep 300

    sshpass -e ssh -o StrictHostKeyChecking=no "$USER@$host_name" 'cd fmsa && docker volume rm $(docker volume ls | grep fmsa | awk "{print $2}")'
    sshpass -e ssh -o StrictHostKeyChecking=no "$USER@$host_name" 'cd fmsa && docker compose up -d'

    sleep 600

    cd ~/fmsa-load-test/experiments
    for _ in $(seq 1 5)
    do
        host_name=$host ./fmsa-load-test-experiments/bin/python pre_upload_required_references.py
        host_name=$3
    done;

    csv_result=$(echo $file_name | awk '{split($1,a,"."); print a[1]}')
    ./fmsa-load-test-experiments/bin/locust -f $file_name --headless \
        --host "http://$host" \
        --users 1000 \
        --spawn-rate 1.11 \
        --run-time 20m \
        --csv="real_mono_$csv_result"
done;

echo "Executing Load Test is done!"
