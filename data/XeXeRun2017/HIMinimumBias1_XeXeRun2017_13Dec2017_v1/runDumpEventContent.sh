#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

inputFile="root://cms-xrd-global.cern.ch//store/hidata/XeXeRun2017/HIMinimumBias1/AOD/13Dec2017-v1/60000/028E25B7-33E9-E711-B098-3C4A92F8FC10.root"
outputFile="edmDEC_HIMinimumBias1_XeXeRun2017_13Dec2017_v1.log"

$runCmd edmDumpEventContent --all $inputFile &> $outputFile

