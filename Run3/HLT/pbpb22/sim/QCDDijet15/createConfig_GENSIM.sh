#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"
#runCmd=""

genFragRemote="https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/HIN-HINPbPbAutumn18GSHIMix-00075"
genFrag="Configuration/GenProduction/HIN-HINPbPbAutumn18GSHIMix-00075-fragment.py"

## src/ directory
# cd $CMSSW_BASE/src
# curl -s -k https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/HIN-HINPbPbAutumn18GSHIMix-00075 --retry 3 --create-dirs -o Configuration/GenProduction/python/HIN-HINPbPbAutumn18GSHIMix-00075-fragment.py
# scram build -j4

# instructions via email
# software : CMSSW_12_4_0

globalTag="auto:phase1_2022_realistic_hi"
beamSpot="Run3RoundOptics25ns13TeVLowSigmaZ"
step="GEN,SIM"
era="Run3_pp_on_PbPb"
nEvents=50
configFile="step1_GEN_SIM.py"
#outputDir="/eos/cms/store/group/phys_heavyions_ops/katatar/run3/HLT/sim/pbpb22/QCDDijet15"
outputDir="./"
outputFile=${outputDir}"/""${configFile/.py/.root}"
logFile="cmsDriver_step1_GEN_SIM.log"

${runCmd} cmsDriver.py ${genFrag} --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions ${globalTag} --step ${step} --scenario HeavyIons --geometry DB:Extended --era ${era} --beamspot ${beamSpot} --nThreads 8 --fileout file:$outputFile -n $nEvents --no_exec --python_filename $configFile &> $logFile

#echo "process.Timing=cms.Service(\"Timing\", summaryOnly = cms.untracked.bool(True), useJobReport = cms.untracked.bool(True))" >> $configFile

configFileLOG="${configFile/.py/.log}"
echo "# run the config via"
echo "cmsRun $configFile &> $configFileLOG &"

## dump the full config
configFileFULL="${configFile/.py/_FULL.py}"
edmConfigDump $configFile > $configFileFULL
echo "# Full config is also created : $configFileFULL"

