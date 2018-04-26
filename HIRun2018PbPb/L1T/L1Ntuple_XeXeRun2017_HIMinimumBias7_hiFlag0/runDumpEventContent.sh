#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

inputFile="root://cms-xrd-global.cern.ch//store/hidata/XeXeRun2017/HIMinimumBias7/RAW/v1/000/304/899/00000/000AB151-8CAF-E711-A03A-02163E019BA4.root"

$runCmd edmDumpEventContent --all $inputFile &> edmDEC_XeXeRun2017_HIMinimumBias7_RAW.log

