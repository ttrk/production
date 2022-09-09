#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"
#runCmd=""

genFragRemote="https://raw.githubusercontent.com/CmsHI/genproductions/master/python/HI/photon_analysis/PbPb/5020GeV/Pythia8_AllQCDPhoton15_TuneCP5_5020GeV_bias_cff.py"
# https://github.com/CmsHI/genproductions/blob/master/python/HI/photon_analysis/PbPb/5020GeV/Pythia8_AllQCDPhoton15_TuneCP5_5020GeV_bias_cff.py
genFrag="Configuration/GenProduction/Pythia8_AllQCDPhoton15_TuneCP5_5020GeV_bias_cff.py"

## src/ directory
# cd $CMSSW_BASE/src
# curl -s -k https://raw.githubusercontent.com/CmsHI/genproductions/master/python/HI/photon_analysis/PbPb/5020GeV/Pythia8_AllQCDPhoton15_TuneCP5_5020GeV_bias_cff.py --retry 3 --create-dirs -o Configuration/GenProduction/python/Pythia8_AllQCDPhoton15_TuneCP5_5020GeV_bias_cff.py
# !! modify the collision energy to sqrt(s) = 5.36 TeV and change bias2SelectionPow from 2 to 4
# scram build -j4

# instructions via HIN HLT mattermost
# software : CMSSW_12_5_0_pre5

globalTag="auto:phase1_2022_realistic"
beamSpot="Realistic25ns13p6TeVEarly2022Collision"
step="GEN,SIM"
era="Run3"
nEvents=2000 # filter efficiency for original bias setting (bias2SelectionPow = 2) was 1.296E-03 as seen from https://twiki.cern.ch/twiki/bin/view/CMS/MCFor2018PbPb5TeV?rev=100
# Filter efficiency for current config is 5.200e-03 (52 out of 10K events passed filter)
configFile="step1_GEN_SIM.py"
#outputDir="/eos/cms/store/group/phys_heavyions_ops/katatar/run3/HLT/sim/pp22/QCDDijet15"
outputDir="./"
outputFile=${outputDir}"/""${configFile/.py/.root}"
logFile="cmsDriver_step1_GEN_SIM.log"

${runCmd} cmsDriver.py ${genFrag} -s ${step} --conditions ${globalTag} --beamspot ${beamSpot} --datatier GEN-SIM --eventcontent FEVTDEBUG --geometry DB:Extended --era ${era} --nThreads 8 --fileout file:$outputFile -n $nEvents --no_exec --python_filename $configFile &> $logFile

#echo "process.Timing=cms.Service(\"Timing\", summaryOnly = cms.untracked.bool(True), useJobReport = cms.untracked.bool(True))" >> $configFile

configFileLOG="${configFile/.py/.log}"
echo "# run the config via"
echo "cmsRun $configFile &> $configFileLOG &"

## dump the full config
configFileFULL="${configFile/.py/_FULL.py}"
edmConfigDump $configFile > $configFileFULL
echo "# Full config is also created : $configFileFULL"

