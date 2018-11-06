#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

genFragRemote="https://raw.githubusercontent.com/cms-sw/cmssw/master/Configuration/Generator/python/SingleGammaFlatPt10To100_pythia8_cfi.py"
genFrag="Configuration/GenProduction/python/SingleGammaFlatPt10To100_pythia8_cfi.py"

## src/ directory
# cd $CMSSW_BASE/src
# mkdir -p Configuration/GenProduction/python/
# wget $genFragRemote -O $genFrag
# scram build -j4

# instructions : https://twiki.cern.ch/twiki/bin/view/CMS/HiHighPtTrigger2018?rev=61#Commands_to_generate_private_MC
# software : CMSSW_10_3_0

globalTag="103X_upgrade2018_realistic_HI_v7"
#globalTag="auto:phase1_2018_realistic_hi"
beamSpot="Realistic25ns13TeVEarly2017Collision"
step="GEN,SIM"
era="Run2_2018_pp_on_AA"
nEvents=50
configFile="step_GEN_SIM.py"
outputFile="${configFile/.py/.root}"
logFile="cmsDriver_step_GEN_SIM.log"

$runCmd cmsDriver.py $genFrag --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions $globalTag --beamspot $beamSpot --step $step --geometry DB:Extended --era $era --fileout file:$outputFile -n $nEvents --no_exec --python_filename $configFile &> $logFile

echo "process.Timing=cms.Service(\"Timing\", summaryOnly = cms.untracked.bool(True), useJobReport = cms.untracked.bool(True))" >> $configFile

configFileLOG="${configFile/.py/.log}"
echo "# run the config via"
echo "myRun cmsRun $configFile &> $configFileLOG &"

## dump the full config
configFileFULL="${configFile/.py/_FULL.py}"
edmConfigDump $configFile > $configFileFULL
echo "# Full config is also created : $configFileFULL"

