#!/bin/bash

file1="inputFiles_das.txt"
file2="inputFiles_das_v2.txt"
fileNewInput="inputFiles_das_v2_new.txt"

set -x
grep -v -f ${file1} ${file2} > ${fileNewInput}

