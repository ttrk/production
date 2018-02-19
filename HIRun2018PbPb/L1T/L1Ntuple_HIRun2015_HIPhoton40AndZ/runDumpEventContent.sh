#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

inputFile="root://xrootd.cmsaf.mit.edu//store/hidata/HIRun2015/HIPhoton40AndZ/RAW/v1/000/262/988/00000/0204FF23-9D98-E511-83C2-02163E014411.root"

$runCmd edmDumpEventContent --all $inputFile &> edmDEC_HIRun2015_HIPhoton40AndZ_RAW.log

