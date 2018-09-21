#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

genFragRemote="https://raw.githubusercontent.com/CmsHI/genproductions/master/python/HI/photon_analysis/PbPb/5020GeV/Pythia8_AllQCDPhoton15_TuneCUETP8M1_5020GeV_cff.py"
genFrag="Configuration/GenProduction/python/Pythia8_AllQCDPhoton15_TuneCUETP8M1_5020GeV_cff.py"

## src/ directory
# mkdir -p Configuration/GenProduction/python/
# wget $genFragRemote -O $genFrag
# scram build -j4

## Software
# CMSSW_9_4_8
# https://twiki.cern.ch/twiki/bin/view/CMS/PP5TeV2017OfficialMC#GEN_SIM
globalTag="94X_mc2017_realistic_forppRef5TeV"
beamSpot="Realistic5TeVppCollision2017"
era="Run2_2017_ppRef"
nEvents=200000
configFile="step_GEN_SIM.py"
outputFile="${configFile/.py/.root}"
logFile="cmsDriver_step_GEN_SIM.log"

$runCmd cmsDriver.py $genFrag --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions $globalTag --beamspot $beamSpot --step GEN,SIM --nThreads 2 --geometry DB:Extended --era $era --fileout file:$outputFile -n $nEvents --no_exec --python_filename $configFile &> $logFile

configFileLOG="${configFile/.py/.log}"
echo "# run the config via"
echo "myRun cmsRun $configFile &> $configFileLOG &"

#echo "process.Timing=cms.Service(\"Timing\", summaryOnly = cms.untracked.bool(False), useJobReport = cms.untracked.bool(True))" >> $configFile
echo "process.Timing=cms.Service(\"Timing\", summaryOnly = cms.untracked.bool(True), useJobReport = cms.untracked.bool(True))" >> $configFile

## dump the full config
configFileFULL="${configFile/.py/_FULL.py}"
edmConfigDump $configFile > $configFileFULL
echo "# Full config is also created : $configFileFULL"

