#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

## NOTE : Only GENSIM is enough to get numbers for MC request. RECO step is for completeness here.
## Software
# CMSSW_9_4_8
# https://twiki.cern.ch/twiki/bin/view/CMS/PP5TeV2017OfficialMC?rev=10#cmsDriver_Commands
globalTag="94X_mc2017_realistic_forppRef5TeV"
era="Run2_2017_ppRef"
nEvents=100
configFile="step_RECO.py"
outputFile="${configFile/.py/.root}"
inputFile="step_DIGI.root"
logFile="cmsDriver_step_RECO.log"

$runCmd cmsDriver.py step2 --mc --eventcontent AODSIM --datatier AODSIM --conditions $globalTag --step RAW2DIGI,L1Reco,RECO,RECOSIM,EI --nThreads 8 --geometry DB:Extended --era $era --filein file:$inputFile --fileout file:$outputFile -n $nEvents --no_exec --python_filename $configFile &> $logFile

configFileLOG="${configFile/.py/.log}"
echo "# run the config via"
echo "myRun cmsRun $configFile &> $configFileLOG &"

echo "process.Timing=cms.Service(\"Timing\", summaryOnly = cms.untracked.bool(True), useJobReport = cms.untracked.bool(True))" >> $configFile

## dump the full config
configFileFULL="${configFile/.py/_FULL.py}"
edmConfigDump $configFile > $configFileFULL
echo "# Full config is also created : $configFileFULL"

