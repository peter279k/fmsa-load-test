#!/bin/bash


host=$1
file_name=$2

csv_result=$(echo $file_name | awk '{split($1,a,"."); print a[1]}')
./fmsa-load-test-experiments/bin/locust -f $file_name --headless \
    --host "http://$host" \
    --users 1000 \
    --spawn-rate 1.11 \
    --run-time 20m \
    --csv="$csv_result"
