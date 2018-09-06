#!/bin/bash

set -x

forestBranch="forest_CMSSW_9_4_1"

cd $CMSSW_BASE/src/
mkdir -p HeavyIonsAnalysis/EventAnalysis/src/
wget https://raw.githubusercontent.com/CmsHI/cmssw/${forestBranch}/HeavyIonsAnalysis/EventAnalysis/src/TriggerObjectAnalyzer.cc -O HeavyIonsAnalysis/EventAnalysis/src/TriggerObjectAnalyzer.cc

wget https://raw.githubusercontent.com/CmsHI/cmssw/${forestBranch}/HeavyIonsAnalysis/EventAnalysis/BuildFile.xml -O HeavyIonsAnalysis/EventAnalysis/BuildFile.xml

mkdir -p HeavyIonsAnalysis/EventAnalysis/python/
wget https://raw.githubusercontent.com/CmsHI/cmssw/${forestBranch}/HeavyIonsAnalysis/EventAnalysis/python/hltobject_PbPb_cfi.py -O HeavyIonsAnalysis/EventAnalysis/python/hltobject_PbPb_cfi.py

scram build clean
scram build -j4
