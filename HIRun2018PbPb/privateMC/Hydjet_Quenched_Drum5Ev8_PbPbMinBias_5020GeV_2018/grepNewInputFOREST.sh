#!/bin/bash

file1="inputFiles_das_FOREST_181107.txt"
file2="inputFiles_das_FOREST_181108.txt"
fileNewInput="inputFiles_das_FOREST_new.txt"

set -x
grep -v -f ${file1} ${file2} > ${fileNewInput}

