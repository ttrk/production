#!/bin/bash

set -x

forestBranch="forest_CMSSW_9_4_1"

cd $CMSSW_BASE/src/

fileList=(
"HeavyIonsAnalysis/EventAnalysis/src/TriggerObjectAnalyzer.cc"
"HeavyIonsAnalysis/EventAnalysis/BuildFile.xml"
"HeavyIonsAnalysis/EventAnalysis/python/hltobject_PbPb_cfi.py"
);

arrayIndices=${!fileList[*]}
for i1 in $arrayIndices
do
    filePath=${fileList[i1]}
    fileDir=$(dirname ${filePath})
    mkdir -p $fileDir
    wget https://raw.githubusercontent.com/CmsHI/cmssw/${forestBranch}/${filePath} -O ${filePath}
done

scram build clean
scram build -j4

