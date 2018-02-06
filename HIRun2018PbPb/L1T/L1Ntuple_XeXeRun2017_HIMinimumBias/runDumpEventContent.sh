#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

inputFile="root://cms-xrd-global.cern.ch//store/hidata/XeXeRun2017/HIMinimumBias8/RAW/v1/000/304/899/00000/02339E6D-94AF-E711-A9FC-02163E0122EE.root"

$runCmd edmDumpEventContent --all $inputFile &> edmDEC_XeXeRun2017_HIMinimumBias8_RAW.log

