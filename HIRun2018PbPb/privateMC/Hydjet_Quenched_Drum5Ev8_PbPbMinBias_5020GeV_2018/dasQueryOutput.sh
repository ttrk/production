#!/bin/bash

dataset="/Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018/katatar-HINPbPbSpring18GS_103X_upgrade2018_realistic_HI_v7_DIGI_L1_DIGI2RAW_HLT_PU-1c389861083a146d75ac332e7b4016f6/USER"
output="outputFiles_das.txt"
instance="prod/phys03"

set -x
dasgoclient --query="file dataset=${dataset} instance=${instance}" > ${output}

