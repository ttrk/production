#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

genFrag="Configuration/GenProduction/python/SinglePi0FlatPt10To100_pythia8_cfi.py"
# Gen fragment is prepared after looking up the following two
# https://github.com/cms-sw/cmssw/blob/master/Configuration/Generator/python/SingleGammaFlatPt10To100_pythia8_cfi.py
# https://github.com/cms-sw/cmssw/blob/master/Configuration/Generator/python/SinglePi0E10_pythia8_cfi.py

## src/ directory
# mkdir -p $CMSSW_BASE/src/Configuration/GenProduction/python/
# cp SinglePi0FlatPt10To100_pythia8_cfi.py $CMSSW_BASE/src/Configuration/GenProduction/python/
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

