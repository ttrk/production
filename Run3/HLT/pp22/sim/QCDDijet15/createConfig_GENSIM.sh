#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"
#runCmd=""

genFragRemote="https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/HIN-HINPbPbAutumn18GSHIMix-00075"
# same as https://github.com/CmsHI/genproductions/blob/master/python/HI/dijet_analysis/pp/Pythia8_Dijet15_pp_TuneCP5_5020GeV_cff.py
genFrag="Configuration/GenProduction/HIN-HINPbPbAutumn18GSHIMix-00075-fragment.py"

## src/ directory
# cd $CMSSW_BASE/src
# curl -s -k https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/HIN-HINPbPbAutumn18GSHIMix-00075 --retry 3 --create-dirs -o Configuration/GenProduction/python/HIN-HINPbPbAutumn18GSHIMix-00075-fragment.py
# !! modify the collision energy to sqrt(s) = 5.36 TeV
# scram build -j4

# instructions via HIN HLT mattermost
# software : CMSSW_12_5_0_pre5

globalTag="auto:phase1_2022_realistic"
beamSpot="Realistic25ns13p6TeVEarly2022Collision"
step="GEN,SIM"
era="Run3"
nEvents=10
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

