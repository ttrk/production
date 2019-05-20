#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

genFrag="Configuration/GenProduction/python/Pythia8_EmEnrichedDijet50_TuneCP5_5020GeV_SingleParticleFilter_cff.py"
# Gen fragment
# https://github.com/CmsHI/genproductions/blob/master/python/HI/photon_analysis/PbPb/5020GeV/Pythia8_EmEnrichedDijet50_TuneCP5_5020GeV_SingleParticleFilter_cff.py

## src/ directory
# mkdir -p $CMSSW_BASE/src/Configuration/GenProduction/python/
# cp Pythia8_EmEnrichedDijet50_TuneCP5_5020GeV_SingleParticleFilter_cff.py $CMSSW_BASE/src/Configuration/GenProduction/python/
# scram build -j4

# software : CMSSW_10_3_3_patch1

inputDatasetPU="dbs:/MinBias_Hydjet_Drum5F_2018_5p02TeV/HINPbPbAutumn18GS-103X_upgrade2018_realistic_HI_v11-v1/GEN-SIM"
globalTag="103X_upgrade2018_realistic_HI_v11"
beamSpot="MatchHI"
step="GEN,SIM"
era="Run2_2018_pp_on_AA"
nDesired=10
effCorr=30  # effCorr = 1/eff, eff = 0.03463
nEvents=$(( ${nDesired} * ${effCorr} ))
configFile="step_GEN_SIM.py"
outputFile="${configFile/.py/.root}"
logFile="cmsDriver_step_GEN_SIM.log"

# https://twiki.cern.ch/twiki/bin/view/CMS/PbPb5TeV2018OfficialMC?rev=17#cmsDriver_Commands_AN1
$runCmd cmsDriver.py $genFrag --mc --pileup HiMixGEN --pileup_input $inputDatasetPU --pileup_dasoption="--limit=0" --eventcontent RAWSIM --datatier GEN-SIM --conditions $globalTag --beamspot $beamSpot --step $step --scenario HeavyIons --geometry DB:Extended --era $era --fileout file:$outputFile -n $nEvents --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring --python_filename $configFile &> $logFile

echo "process.Timing=cms.Service(\"Timing\", summaryOnly = cms.untracked.bool(True), useJobReport = cms.untracked.bool(True))" >> $configFile

configFileLOG="${configFile/.py/.log}"
echo "# run the config via"
echo "myRun cmsRun $configFile &> $configFileLOG &"

## dump the full config
configFileFULL="${configFile/.py/_FULL.py}"
edmConfigDump $configFile > $configFileFULL
echo "# Full config is also created : $configFileFULL"

