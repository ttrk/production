#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"
#runCmd=""

# instructions via HIN HLT mattermost
# software : CMSSW_12_5_0_pre5

inputFile="file:step2_DIGI.root"
globalTag="auto:phase1_2022_realistic"
step="RAW2DIGI,L1Reco,RECO,RECOSIM,PAT"
era="Run3"
nEvents=10
configFile="step3_RECO.py"
outputDir="./"
outputFile=${outputDir}"/""${configFile/.py/.root}"
logFile="cmsDriver_step3_RECO.log"

${runCmd} cmsDriver.py step3 -s ${step} --conditions ${globalTag} --datatier GEN-SIM-RECO,MINIAODSIM --eventcontent AODSIM,MINIAODSIM --geometry DB:Extended --era ${era} --nThreads 8 --filein $inputFile --fileout file:$outputFile -n $nEvents --no_exec --python_filename $configFile &> $logFile

#echo "process.Timing=cms.Service(\"Timing\", summaryOnly = cms.untracked.bool(True), useJobReport = cms.untracked.bool(True))" >> $configFile

configFileLOG="${configFile/.py/.log}"
echo "# run the config via"
echo "cmsRun $configFile &> $configFileLOG &"

## dump the full config
configFileFULL="${configFile/.py/_FULL.py}"
edmConfigDump $configFile > $configFileFULL
echo "# Full config is also created : $configFileFULL"


