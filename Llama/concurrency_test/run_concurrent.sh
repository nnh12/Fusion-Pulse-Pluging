#!/bin/bash
for i in {1..50}
do
    python3 ../single_query.py &

done
wait

