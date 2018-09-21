#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

## NOTE : Only GENSIM is enough to get numbers for MC request. DIGI step is for completeness here.
## Software
# CMSSW_9_4_8
# https://twiki.cern.ch/twiki/bin/view/CMS/PP5TeV2017OfficialMC?rev=10#cmsDriver_Commands
inputPU="dbs:/MinBias_TuneCUETP8M1_2017_5p02TeV-pythia8/RunIIpp5Spring18GS-94X_mc2017_realistic_v10For2017G_v3-v2/GEN-SIM"
configPU="E7TeV_AVE_2_BX2808"
globalTag="94X_mc2017_realistic_forppRef5TeV"
beamSpot="Realistic5TeVppCollision2017"
era="Run2_2017_ppRef"
nEvents=100
configFile="step_DIGI.py"
outputFile="${configFile/.py/.root}"
inputFile="step_GEN_SIM.root"
logFile="cmsDriver_step_DIGI.log"

$runCmd cmsDriver.py step1 --pileup_input $inputPU --mc --eventcontent RAWSIM --pileup $configPU --datatier GEN-SIM-RAW --conditions $globalTag --beamspot $beamSpot --step DIGI,L1,DIGI2RAW,HLT:PRef --nThreads 8 --geometry DB:Extended --era $era --filein file:$inputFile --fileout file:$outputFile -n $nEvents --no_exec --python_filename $configFile &> $logFile

configFileLOG="${configFile/.py/.log}"
echo "# run the config via"
echo "myRun cmsRun $configFile &> $configFileLOG &"

echo "process.Timing=cms.Service(\"Timing\", summaryOnly = cms.untracked.bool(True), useJobReport = cms.untracked.bool(True))" >> $configFile

## dump the full config
configFileFULL="${configFile/.py/_FULL.py}"
edmConfigDump $configFile > $configFileFULL
echo "# Full config is also created : $configFileFULL"

