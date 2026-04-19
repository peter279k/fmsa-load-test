#!/bin/bash

echo "Executing Load Test is started!"

host=$1
path="scenarios.txt"

if [[ ! -f "$path" ]]; then
    echo "$path file is not found."
    exit 1;
fi;

for file_name in $(cat $path)
do
    csv_result=$(echo $file_name | awk '{split($1,a,"."); print a[1]}')
    locust -f $file_name --headless \
        --host "http://$host" \
        --users 1000 \
        --spawn-rate 1.11 \
        --run-time 20m \
        --csv="$csv_result"

    sleep(300)
done;

echo "Executing Load Test is done!"
