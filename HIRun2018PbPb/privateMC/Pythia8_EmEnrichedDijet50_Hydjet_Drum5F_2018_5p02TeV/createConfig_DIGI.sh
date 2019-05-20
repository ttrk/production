#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

# software : CMSSW_10_3_3_patch1

inputDatasetPU="dbs:/MinBias_Hydjet_Drum5F_2018_5p02TeV/HINPbPbAutumn18GS-103X_upgrade2018_realistic_HI_v11-v1/GEN-SIM"
inputFile="file:/afs/cern.ch/work/k/katatar/public/EGamma/CMSSW_10_3_3_patch1/src/Pythia8_EmEnrichedDijet50_Hydjet_Drum5F_2018_5p02TeV/step_GEN_SIM.root"
globalTag="103X_upgrade2018_realistic_HI_v11"
step="DIGI:pdigi_hi,L1,DIGI2RAW,HLT:@fake2"
era="Run2_2018_pp_on_AA"
nEvents=10
configFile="step2_DIGI_L1_DIGI2RAW_HLT_PU.py"
outputFile="${configFile/.py/.root}"
logFile="cmsDriver_step2_DIGI_L1_DIGI2RAW_HLT_PU.log"

# https://twiki.cern.ch/twiki/bin/view/CMS/PbPb5TeV2018OfficialMC?rev=17#cmsDriver_Commands
$runCmd cmsDriver.py step2 --mc --pileup_input $inputDatasetPU --pileup_dasoption="--limit=0" --eventcontent RAWSIM --pileup HiMix --datatier GEN-SIM-DIGI-RAW --conditions $globalTag --step $step --geometry DB:Extended --era $era --filein $inputFile --fileout file:$outputFile -n $nEvents --no_exec --python_filename $configFile &> $logFile

configFileLOG="${configFile/.py/.log}"
echo "# run the config via"
echo "myRun cmsRun $configFile &> $configFileLOG &"

echo "process.Timing=cms.Service(\"Timing\", summaryOnly = cms.untracked.bool(True), useJobReport = cms.untracked.bool(True))" >> $configFile

## dump the full config
configFileFULL="${configFile/.py/_FULL.py}"
edmConfigDump $configFile > $configFileFULL
echo "# Full config is also created : $configFileFULL"

