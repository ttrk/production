#!/bin/bash

#runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"
runCmd=""

inputFile="root://xrootd.cmsaf.mit.edu//store/hidata/HIRun2018A/HIMinimumBias2/RAW/v1/000/327/402/00000/BF49D3F3-CA0C-264E-8384-3D2BECD313EB.root"
outputFile="edmDEC_HIRun2018PbPb_DATA_RAW.log"

$runCmd edmDumpEventContent --all $inputFile &> $outputFile

