#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

# instructions : https://twiki.cern.ch/twiki/bin/view/CMS/HiHighPtRecoValidation2018?rev=83#CMSSW_10_3_0_pre5_DIGI_Recipes_f
# software : CMSSW_10_3_0_pre5

inputFile="root://xrootd.cmsaf.mit.edu//store/user/clindsey/Pythia8_EmEnrichedDijet30_Hydjet_Quenched_Cymbal5Ev8/GEN_SIM_20180629/180629_154627/0000/Pythia8_EmEnrichedDijet30_TuneCUETP8M1_5020GeV_SingleParticleFilter_cff_py_GEN_SIM_PU_100.root"
globalTag="103X_upgrade2018_realistic_HI_v4"
era="Run2_2018_pp_on_AA"
step="DIGI:pdigi_hi_nogen,L1,DIGI2RAW,HLT:@fake2"
nEvents=10
configFile="step2_DIGI_L1_DIGI2RAW_HLT_PU.py"
outputFile="${configFile/.py/.root}"
logFile="cmsDriver_step2_DIGI_L1_DIGI2RAW_HLT_PU.log"

$runCmd cmsDriver.py step2 --mc --pileup_input dbs:/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV_2018/HINPbPbSpring18GS-100X_upgrade2018_realistic_v10-v1/GEN-SIM --eventcontent RAWSIM --pileup HiMix --pileup_dasoption="--limit=0" --datatier GEN-SIM-DIGI-RAW --conditions $globalTag --step $step --scenario HeavyIons --geometry DB:Extended --era $era --filein $inputFile --fileout file:$outputFile -n $nEvents --no_exec --python_filename $configFile &> $logFile

#Fix beamspot
echo "import CalibTracker.Configuration.Common.PoolDBESSource_cfi" >> $configFile
echo "process.newBS = CalibTracker.Configuration.Common.PoolDBESSource_cfi.poolDBESSource.clone(connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'), toGet = cms.VPSet(cms.PSet(record = cms.string('BeamSpotObjectsRcd'), tag = cms.string('BeamSpotObjects_Realistic25ns_13TeVCollisions_Early2017_v1_mc'))))" >> $configFile
echo "process.prefer_PreferNewBS = cms.ESPrefer('PoolDBESSource', 'newBS')" >> $configFile

configFileLOG="${configFile/.py/.log}"
echo "# run the config via"
echo "myRun cmsRun $configFile &> $configFileLOG &"

## dump the full config
configFileFULL="${configFile/.py/_FULL.py}"
edmConfigDump $configFile > $configFileFULL
echo "# Full config is also created : $configFileFULL"

