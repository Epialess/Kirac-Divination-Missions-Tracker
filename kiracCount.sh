#!/bin/bash

extractedData=$(cut -d' ' -f2- kiracList.txt | sort | uniq -c | awk '{printf "%-8s %s\n", $1, substr($0, index($0,$2))}' | tee occurrences.txt)

printf "%s\n" "$extractedData"