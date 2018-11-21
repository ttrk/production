#!/bin/bash

jsonFile="/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/HI/DCSOnly/json_DCSONLY_HI.txt"
hltPath="HLT_HIGEDPhoton40_EB_v1"
output="brilcalc_lumi_Collisions18_json_DCSONLY_HI_"$hltPath".log"

set -x
brilcalc lumi -i $jsonFile --hltpath $hltPath &> $output
set +x
