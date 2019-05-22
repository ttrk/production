#!/bin/bash

#runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"
runCmd=""

inputFile="root://eoscms.cern.ch//eos/cms/store/hidata/HIRun2018A/HIHardProbes/AOD/04Apr2019-v1/260005/E3BABD06-60D0-9845-8FCE-F9FAF45B57A8.root"
outputFile="edmPD_HIRun2018PbPb_DATA_AOD.log"

$runCmd edmProvDump $inputFile &> $outputFile

