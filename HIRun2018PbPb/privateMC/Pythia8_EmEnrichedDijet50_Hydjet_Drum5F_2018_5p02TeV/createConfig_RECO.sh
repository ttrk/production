#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

# software : CMSSW_10_3_3_patch1

inputFile="file:/afs/cern.ch/work/k/katatar/public/EGamma/CMSSW_10_3_3_patch1/src/Pythia8_EmEnrichedDijet50_Hydjet_Drum5F_2018_5p02TeV/step2_DIGI_L1_DIGI2RAW_HLT_PU.root"
globalTag="103X_upgrade2018_realistic_HI_v11"
step="RAW2DIGI,L1Reco,RECO"
era="Run2_2018_pp_on_AA"
nEvents=10
configFile="step3_RAW2DIGI_L1Reco_RECO.py"
outputFile="${configFile/.py/.root}"
logFile="cmsDriver_step3_RAW2DIGI_L1Reco_RECO.log"

# https://twiki.cern.ch/twiki/bin/view/CMS/PbPb5TeV2018OfficialMC?rev=17#cmsDriver_Commands
$runCmd cmsDriver.py step3 --mc --eventcontent AODSIM --datatier GEN-SIM-RECO --conditions $globalTag --step $step --geometry DB:Extended --era $era --filein $inputFile --fileout file:$outputFile -n $nEvents --no_exec --python_filename $configFile &> $logFile

configFileLOG="${configFile/.py/.log}"
echo "# run the config via"
echo "myRun cmsRun $configFile &> $configFileLOG &"

echo "process.Timing=cms.Service(\"Timing\", summaryOnly = cms.untracked.bool(True), useJobReport = cms.untracked.bool(True))" >> $configFile

## dump the full config
configFileFULL="${configFile/.py/_FULL.py}"
edmConfigDump $configFile > $configFileFULL
echo "# Full config is also created : $configFileFULL"

