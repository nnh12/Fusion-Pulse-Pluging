#!/bin/bash
for i in {1..100}
do
    python3 ../single_query.py &

done
wait

