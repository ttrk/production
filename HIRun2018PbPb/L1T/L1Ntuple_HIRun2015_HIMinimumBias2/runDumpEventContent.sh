#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

inputFile="root://xrootd.cmsaf.mit.edu//store/hidata/HIRun2015/HIMinimumBias2/RAW/v1/000/263/261/00000/0029C4B7-149B-E511-BEEE-02163E01431C.root"

$runCmd edmDumpEventContent --all $inputFile &> edmDEC_HIRun2015_HIMinimumBias2_RAW.log

