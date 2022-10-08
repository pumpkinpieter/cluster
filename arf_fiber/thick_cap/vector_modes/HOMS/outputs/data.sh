#!/usr/bin/bash

pull_cluster
wait
for i in {0..2}
	do
	    python3 combine_data.py ${i}
done

