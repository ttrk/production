#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"
#runCmd="/afs/lns.mit.edu/user/tatar/code/scripts/myRun.sh"

# instructions : https://twiki.cern.ch/twiki/bin/view/CMS/HiHighPtTrigger2018?rev=46#Commands_to_generate_private_MC
# software : CMSSW_10_3_0

inputFile="root://xrootd.cmsaf.mit.edu//store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10_ext1-v1/40001/FE23B1BC-8CA8-E811-861C-AC1F6B23C94A.root,root://xrootd.cmsaf.mit.edu//store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10_ext1-v1/40001/F857A1AA-94A8-E811-8746-A0369FD0B366.root"
globalTag="103X_upgrade2018_realistic_HI_v7"
era="Run2_2018_pp_on_AA"
step="DIGI:pdigi_hi_nogen,L1,DIGI2RAW,HLT:@fake2"
nEvents=50
configFile="step2_DIGI_L1_DIGI2RAW_HLT_PU.py"
outputFile="${configFile/.py/.root}"
logFile="cmsDriver_step2_DIGI_L1_DIGI2RAW_HLT_PU.log"

$runCmd cmsDriver.py step2 --mc --eventcontent RAWSIM --pileup HiMixNoPU --datatier GEN-SIM-DIGI-RAW --conditions $globalTag --step $step --geometry DB:Extended --era $era --filein $inputFile --fileout file:$outputFile -n $nEvents --no_exec --python_filename $configFile &> $logFile

#Fix beamspot
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

