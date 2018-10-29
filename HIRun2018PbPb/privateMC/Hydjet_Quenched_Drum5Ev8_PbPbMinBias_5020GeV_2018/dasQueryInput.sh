#!/bin/bash

dataset="/Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018/HINPbPbSpring18GS-100X_upgrade2018_realistic_v10_ext1-v1/GEN-SIM"
output="inputFiles_das.txt"
instance="prod/global"
site="T2_US_MIT"

set -x
dasgoclient --query="file dataset=${dataset} instance=${instance} site=${site}" > ${output}

