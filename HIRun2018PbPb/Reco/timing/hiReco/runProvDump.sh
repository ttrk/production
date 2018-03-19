#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

inputFile="hiReco_RAW2DIGI_L1Reco_RECO_N100.root"
outputFile="edmPD_"${inputFile/.root/.log}

$runCmd edmProvDump $inputFile &> $outputFile

