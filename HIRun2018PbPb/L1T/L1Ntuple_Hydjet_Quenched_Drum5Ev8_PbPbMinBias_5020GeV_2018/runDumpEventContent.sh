#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

inputFile="root://cms-xrd-global.cern.ch//store/himc/HINPbPbSpring18DR/Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM-RAW/NoPU_100X_upgrade2018_realistic_v10_ext1-v1/00001/FE243EFA-6DAB-E811-BFDE-9CB654AD72EC.root"

$runCmd edmDumpEventContent --all $inputFile &> edmDEC_Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018_GEN_SIM_RAW.log

