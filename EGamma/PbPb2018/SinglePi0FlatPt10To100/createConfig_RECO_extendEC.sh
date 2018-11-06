#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

# instructions : https://twiki.cern.ch/twiki/bin/view/CMS/HiHighPtTrigger2018?rev=61#Commands_to_generate_private_MC
# software : CMSSW_10_3_0

inputFile="file:step2_DIGI_L1_DIGI2RAW_HLT_PU.root"
globalTag="103X_upgrade2018_realistic_HI_v7"
step="RAW2DIGI,L1Reco,RECO"
era="Run2_2018_pp_on_AA"
nEvents=50
configFile="step3_RAW2DIGI_L1Reco_RECO_extendEC.py"
outputFile="${configFile/.py/.root}"
logFile="cmsDriver_step3_RAW2DIGI_L1Reco_RECO_extendEC.log"

$runCmd cmsDriver.py step3 --mc --eventcontent AODSIM --datatier GEN-SIM-RECO --conditions $globalTag --step $step --geometry DB:Extended --era $era --filein $inputFile --fileout file:$outputFile -n $nEvents --no_exec --python_filename $configFile &> $logFile

cat step3ExtraLines.txt >> $configFile

echo "process.Timing=cms.Service(\"Timing\", summaryOnly = cms.untracked.bool(True), useJobReport = cms.untracked.bool(True))" >> $configFile

configFileLOG="${configFile/.py/.log}"
echo "# run the config via"
echo "myRun cmsRun $configFile &> $configFileLOG &"

## dump the full config
configFileFULL="${configFile/.py/_FULL.py}"
edmConfigDump $configFile > $configFileFULL
echo "# Full config is also created : $configFileFULL"
