#!/bin/bash

#runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"
runCmd=""

inputFile="root://xrootd-cms.infn.it//store/himc/HINPbPbSpring21MiniAOD/QCDPhoton_pThat-15_TuneCP5_caloParmStage2v3_HydjetDrumMB_5p02TeV_Pythia8/MINIAODSIM/FixL1CaloGT_112X_upgrade2018_realistic_HI_v9-v1/230000/04db870e-af38-481c-a2c7-0a52fb290868.root"
outputFile="edmDEC_HIRun2018PbPb_MC_MINIAODSIM_HINPbPbSpring21MiniAOD.log"

$runCmd edmDumpEventContent --all $inputFile &> $outputFile

