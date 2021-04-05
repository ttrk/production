#!/bin/bash

#runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"
runCmd=""

## fragment on github    : https://github.com/CmsHI/genproductions/blob/master/python/HI/photon_analysis/PbPb/5020GeV/Pythia8_AllQCDPhoton15_TuneCP5_5020GeV_bias_cff.py
## same fragment on PDMV : https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/HIN-HINPbPbAutumn18GSHIMix-00063/0

genFragRemote="https://raw.githubusercontent.com/CmsHI/genproductions/master/python/HI/photon_analysis/PbPb/5020GeV/Pythia8_AllQCDPhoton15_TuneCP5_5020GeV_bias_cff.py"
genFrag="Configuration/GenProduction/python/Pythia8_AllQCDPhoton15_TuneCP5_5020GeV_bias_cff.py"

## src/ directory
# cd $CMSSW_BASE/src
# mkdir -p Configuration/GenProduction/python/
# wget $genFragRemote -O $genFrag
# scram build -j4

# instructions : https://twiki.cern.ch/twiki/bin/view/CMS/PbPb5TeV2018OfficialMC?rev=29#GEN_SIM
# software : CMSSW_10_3_2

globalTag="103X_upgrade2018_realistic_HI_v11"
beamSpot="RealisticPbPbCollision2018"
step="GEN,SIM"
era="Run2_2018_pp_on_AA"
inputPU="dbs:/MinBias_Hydjet_Drum5F_2018_5p02TeV/HINPbPbAutumn18GS-103X_upgrade2018_realistic_HI_v11-v1/GEN-SIM"
inputPULimit="--limit=200"  # limit is the number of files to fetch from the PU dataset, set "--limit=0" to fetch all the files
nEvents=150000
configFile="step1_GEN_SIM.py"
outputFile="${configFile/.py/.root}"
logFile="cmsDriver_step1_GEN_SIM.log"

${runCmd} cmsDriver.py ${genFrag} --mc --pileup HiMixGEN --pileup_input ${inputPU} --pileup_dasoption=${inputPULimit} --eventcontent RAWSIM --datatier GEN-SIM --conditions ${globalTag} --beamspot ${beamSpot} --step ${step} --scenario HeavyIons --geometry DB:Extended --era ${era} --fileout file:$outputFile -n $nEvents --no_exec --python_filename $configFile &> $logFile

echo "process.Timing=cms.Service(\"Timing\", summaryOnly = cms.untracked.bool(True), useJobReport = cms.untracked.bool(True))" >> $configFile

configFileLOG="${configFile/.py/.log}"
echo "# run the config via"
echo "cmsRun $configFile &> $configFileLOG &"

## dump the full config
configFileFULL="${configFile/.py/_FULL.py}"
edmConfigDump $configFile > $configFileFULL
echo "# Full config is also created : $configFileFULL"

