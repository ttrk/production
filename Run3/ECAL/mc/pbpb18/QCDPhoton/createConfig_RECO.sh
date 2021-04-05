#!/bin/bash

#runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"
runCmd=""

# instructions : https://twiki.cern.ch/twiki/bin/view/CMS/PbPb5TeV2018OfficialMC?rev=29#DIGI_RECO
# software : CMSSW_10_3_2

inputFile="file:step2_DIGI.root"
globalTag="103X_upgrade2018_realistic_HI_v11"
step="RAW2DIGI,L1Reco,RECO"
era="Run2_2018_pp_on_AA"
nEvents=10
configFile="step3_RECO.py"
outputFile="${configFile/.py/.root}"
logFile="cmsDriver_step3_RECO.log"

## from https://cms-pdmv.cern.ch/mcm/campaigns?prepid=HINPbPbAutumn18DR&page=0&shown=8255
${runCmd} cmsDriver.py step3 --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions ${globalTag} --step ${step} --nThreads 8 --era ${era} --filein $inputFile --fileout file:$outputFile -n $nEvents --no_exec --python_filename $configFile &> $logFile

## does NOT work
#${runCmd} cmsDriver.py step3 --mc --eventcontent AODSIM --datatier GEN-SIM-RECO --conditions ${globalTag} --step ${step} --nThreads 4 --scenario HeavyIons --geometry DB:Extended --era ${era} --filein $inputFile --fileout file:$outputFile -n $nEvents --no_exec --python_filename $configFile &> $logFile

echo "process.Timing=cms.Service(\"Timing\", summaryOnly = cms.untracked.bool(True), useJobReport = cms.untracked.bool(True))" >> $configFile

configFileLOG="${configFile/.py/.log}"
echo "# run the config via"
echo "cmsRun $configFile &> $configFileLOG &"

## dump the full config
configFileFULL="${configFile/.py/_FULL.py}"
edmConfigDump $configFile > $configFileFULL
echo "# Full config is also created : $configFileFULL"
