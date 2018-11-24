#!/bin/bash

dataset="/HIHardProbes/HIRun2018A-PbPbZEE-PromptReco-v1/RAW-RECO"
output="inputFiles_das_FOREST.txt"
instance="prod/global"
site="T2_CH_CERN"

set -x
#dasgoclient --query="file dataset=${dataset} instance=${instance} site=${site}" > ${output}
dasgoclient --query="file dataset=${dataset} instance=${instance}" > ${output}

