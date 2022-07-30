#!/usr/bin/bash

pull_cluster
wait
for i in {0..1}
	do
	    python3 combine_data.py ${i}
done

