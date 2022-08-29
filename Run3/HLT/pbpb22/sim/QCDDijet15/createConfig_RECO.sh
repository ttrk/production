#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"
#runCmd=""

# instructions via email
# software : CMSSW_12_4_0

#inputFile="file:/eos/cms/store/group/phys_heavyions_ops/katatar/run3/HLT/sim/pbpb22/QCDDijet15/step2_DIGI.root"
inputFile="file:step2_DIGI.root"
globalTag="auto:phase1_2022_realistic_hi"
step="RAW2DIGI,L1Reco,RECO"
era="Run3_pp_on_PbPb"
nEvents=50
configFile="step3_RECO.py"
#outputDir="/eos/cms/store/group/phys_heavyions_ops/katatar/run3/HLT/sim/pbpb22/QCDDijet15"
outputDir="./"
outputFile=${outputDir}"/""${configFile/.py/.root}"
logFile="cmsDriver_step3_RECO.log"

${runCmd} cmsDriver.py step3 -s ${step} --conditions ${globalTag} --datatier GEN-SIM-RECO --eventcontent AODSIM --era ${era} --nThreads 8 --filein $inputFile --fileout file:$outputFile -n $nEvents --no_exec --python_filename $configFile &> $logFile

#echo "process.Timing=cms.Service(\"Timing\", summaryOnly = cms.untracked.bool(True), useJobReport = cms.untracked.bool(True))" >> $configFile

configFileLOG="${configFile/.py/.log}"
echo "# run the config via"
echo "cmsRun $configFile &> $configFileLOG &"

## dump the full config
configFileFULL="${configFile/.py/_FULL.py}"
edmConfigDump $configFile > $configFileFULL
echo "# Full config is also created : $configFileFULL"


