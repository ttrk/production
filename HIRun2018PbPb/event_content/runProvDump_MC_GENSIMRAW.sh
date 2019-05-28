#!/bin/bash

#runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"
runCmd=""

inputFile="root://xrootd-cms.infn.it//store/himc/HINPbPbAutumn18DR/MinBias_Hydjet_Drum5F_2018_5p02TeV/GEN-SIM-RAW/NoPU_103X_upgrade2018_realistic_HI_v11-v1/50000/0142EF73-4794-C541-985F-33D27816F357.root"
outputFile="edmPD_HIRun2018PbPb_MC_GENSIMRAW.log"

$runCmd edmProvDump $inputFile &> $outputFile

