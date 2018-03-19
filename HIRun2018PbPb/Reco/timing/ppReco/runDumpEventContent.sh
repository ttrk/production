#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

inputFile="step3_RAW2DIGI_L1Reco_RECO_N100.root"
outputFile="edmDEC_"${inputFile/.root/.log}

$runCmd edmDumpEventContent --all $inputFile &> $outputFile

