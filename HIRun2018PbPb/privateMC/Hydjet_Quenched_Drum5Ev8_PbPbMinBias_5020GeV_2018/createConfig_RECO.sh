#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

# instructions : https://twiki.cern.ch/twiki/bin/view/CMS/HiHighPtTrigger2018?rev=44#Commands_to_generate_private_MC
# software : CMSSW_10_3_0

inputFile="file:step2_DIGI_L1_DIGI2RAW_HLT_PU.root"
globalTag="103X_upgrade2018_realistic_HI_v7"
era="Run2_2018_pp_on_AA"
step="RAW2DIGI,L1Reco,RECO"
nEvents=50
configFile="step3_RAW2DIGI_L1Reco_RECO.py"
outputFile="${configFile/.py/.root}"
logFile="cmsDriver_step3_RAW2DIGI_L1Reco_RECO.log"

$runCmd cmsDriver.py step3 --mc --eventcontent AODSIM --datatier GEN-SIM-RECO --conditions $globalTag --step $step --geometry DB:Extended --era $era --filein $inputFile --fileout file:$outputFile -n $nEvents --no_exec --python_filename $configFile &> $logFile

#Fixing src for CHS jets (this will be fixed in future CMSSW
echo "process.ak4PFJetsCHS.src = cms.InputTag('particleFlow')" >> $configFile
echo "process.ak8PFJetsCHS.src = cms.InputTag('particleFlow')" >> $configFile
#Match beamspot to HYDJET produced in CMSSW_10_0(1)_X
#echo "import CalibTracker.Configuration.Common.PoolDBESSource_cfi" >> $configFile
#echo "process.newBS = CalibTracker.Configuration.Common.PoolDBESSource_cfi.poolDBESSource.clone(connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'), toGet = cms.VPSet(cms.PSet(record = cms.string('BeamSpotObjectsRcd'), tag = cms.string('BeamSpotObjects_Realistic25ns_13TeVCollisions_Early2017_v1_mc'))))" >> $configFile
#echo "process.prefer_PreferNewBS = cms.ESPrefer('PoolDBESSource', 'newBS')" >> $configFile

configFileLOG="${configFile/.py/.log}"
echo "# run the config via"
echo "myRun cmsRun $configFile &> $configFileLOG &"

## dump the full config
configFileFULL="${configFile/.py/_FULL.py}"
edmConfigDump $configFile > $configFileFULL
echo "# Full config is also created : $configFileFULL"

