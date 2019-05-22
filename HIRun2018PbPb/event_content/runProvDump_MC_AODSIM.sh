#!/bin/bash

#runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"
runCmd=""

inputFile="root://xrootd-cms.infn.it//store/himc/HINPbPbAutumn18DR/QCDPhoton_pThat-15_TuneCP5_PbPb_5p02TeV_pythia8/AODSIM/NoPU_103X_upgrade2018_realistic_HI_v11-v1/90000/F034BBC1-62CB-3C4D-BFDA-8B2529C79A62.root"
outputFile="edmPD_HIRun2018PbPb_MC_AODSIM.log"

$runCmd edmProvDump $inputFile &> $outputFile

