#!/bin/bash

dataset="/Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018/katatar-HINPbPbSpring18GS_103X_upgrade2018_realistic_HI_v7_RAW2DIGI_L1Reco_RECO-021581694253bdfb10a34312cf24d4c7/USER"
output="inputFiles_das_FOREST.txt"
instance="prod/phys03"

set -x
dasgoclient --query="file dataset=${dataset} instance=${instance}" > ${output}

