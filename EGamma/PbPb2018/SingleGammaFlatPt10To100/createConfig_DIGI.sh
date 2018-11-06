#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

# instructions : https://twiki.cern.ch/twiki/bin/view/CMS/HiHighPtTrigger2018?rev=61#Commands_to_generate_private_MC
# software : CMSSW_10_3_0

inputFile="file:step_GEN_SIM.root"
globalTag="103X_upgrade2018_realistic_HI_v7"
step="DIGI:pdigi_hi,L1,DIGI2RAW,HLT:@fake2"
era="Run2_2018_pp_on_AA"
nEvents=50
configFile="step2_DIGI_L1_DIGI2RAW_HLT_PU.py"
outputFile="${configFile/.py/.root}"
logFile="cmsDriver_step2_DIGI_L1_DIGI2RAW_HLT_PU.log"

$runCmd cmsDriver.py step2 --mc --eventcontent RAWSIM --pileup HiMixNoPU --datatier GEN-SIM-RAW --conditions $globalTag --step $step --geometry DB:Extended --era $era --filein $inputFile --fileout file:$outputFile -n $nEvents --no_exec --python_filename $configFile &> $logFile

echo "process.Timing=cms.Service(\"Timing\", summaryOnly = cms.untracked.bool(True), useJobReport = cms.untracked.bool(True))" >> $configFile

configFileLOG="${configFile/.py/.log}"
echo "# run the config via"
echo "myRun cmsRun $configFile &> $configFileLOG &"

## dump the full config
configFileFULL="${configFile/.py/_FULL.py}"
edmConfigDump $configFile > $configFileFULL
echo "# Full config is also created : $configFileFULL"

