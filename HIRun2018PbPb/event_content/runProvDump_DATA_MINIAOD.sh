#!/bin/bash

#runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"
runCmd=""

inputFile="root://xrootd-cms.infn.it//store/hidata/HIRun2018A/HIHardProbes/MINIAOD/PbPb18_MiniAODv1-v1/00000/034807c1-0ae5-4540-bb81-80ab2f3bc01d.root"
outputFile="edmPD_HIRun2018PbPb_DATA_MINIAOD.log"

$runCmd edmProvDump $inputFile &> $outputFile

