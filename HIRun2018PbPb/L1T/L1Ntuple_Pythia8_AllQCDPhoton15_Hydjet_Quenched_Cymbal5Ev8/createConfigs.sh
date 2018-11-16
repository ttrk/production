#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

# https://twiki.cern.ch/twiki/bin/view/CMS/HiHighPtTrigger2018?rev=88#To%20be%20produced
inputFile="root://xrootd.cmsaf.mit.edu//store/user/rbi/Pythia8_AllQCDPhoton15_bias_Hydjet_Drum5Ev8_5020GeV/crab_Pythia8_AllQCDPhoton15_bias_Hydjet_Drum5Ev8_5020GeV_DIGI2RAW_PU_1030_v1/181030_234244/0001/step1_DIGI_L1_DIGI2RAW_HLT_PU_1652.root"

## Software
# CMSSW_10_3_1, no l1t tag
# This integration contains the new L1 EG bypass flags : https://github.com/cms-l1t-offline/cmssw/pull/708
## Driver
# derived by updating the L1 workflow to match the latest HLT setup. Current L1 setup was probably obsolete
# (probably obsolete) L1 instructions : https://twiki.cern.ch/twiki/bin/view/CMS/L1HITaskForce?rev=42#Offline_SW_setup
# HLT instructions : https://twiki.cern.ch/twiki/bin/view/CMS/HiHighPtTrigger2018?rev=88#Instructions%20as%20of%202018.11.02%20in
ERA="Run2_2018"
GLOBALTAG="103X_upgrade2018_realistic_HI_v7"
nEvents=100
configPrefix="l1Ntuple"

### modify input for calo digi collection
## https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideL1TStage2Instructions?rev=141#Workflows_AN1
#--customise=L1Trigger/Configuration/customiseReEmul.L1TReEmulMCFromRAWSimCalTP
# https://github.com/cms-sw/cmssw/blob/master/L1Trigger/Configuration/python/customiseReEmul.py#L253-L254
# https://github.com/cms-sw/cmssw/blob/71741cd7aea763fce2c07ca50370cd14b7edd261/L1Trigger/Configuration/python/customiseReEmul.py#L253-L254

$runCmd cmsDriver.py $configPrefix -s RAW2DIGI --era=$ERA \
--customise=L1Trigger/Configuration/customiseReEmul.L1TReEmulMCFromRAWSimCalTP \
--customise=L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleEMU \
--customise=L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleGEN \
--customise=L1Trigger/Configuration/customiseUtils.L1TTurnOffUnpackStage2GtGmtAndCalo \
--customise=L1Trigger/Configuration/customiseSettings.L1TSettingsToCaloParams_2018_v1_4 \
--conditions=$GLOBALTAG -n $nEvents --mc --no_exec --no_output --filein=$inputFile &> cmsDriver_l1Ntuple_RAW2DIGI.log

config_l1Ntuple=$configPrefix"_RAW2DIGI.py"

#beamspot customization
echo "" >> $config_l1Ntuple
echo "import CalibTracker.Configuration.Common.PoolDBESSource_cfi" >> $config_l1Ntuple
echo "process.newBS = CalibTracker.Configuration.Common.PoolDBESSource_cfi.poolDBESSource.clone(connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'), toGet = cms.VPSet(cms.PSet(record = cms.string('BeamSpotObjectsRcd'), tag = cms.string('BeamSpotObjects_Realistic25ns_13TeVCollisions_Early2017_v1_mc'))))" >> $config_l1Ntuple
echo "process.prefer_PreferNewBS = cms.ESPrefer('PoolDBESSource', 'newBS')" >> $config_l1Ntuple

echo "process.simTwinMuxDigis.DTDigi_Source = cms.InputTag('bmtfDigis')" >> $config_l1Ntuple
echo "process.simTwinMuxDigis.DTThetaDigi_Source = cms.InputTag('bmtfDigis')" >> $config_l1Ntuple
echo "process.simTwinMuxDigis.RPC_Source = cms.InputTag('muonRPCDigis')" >> $config_l1Ntuple

#Jet customization (via Chris)
echo "" >> $config_l1Ntuple
echo "process.caloStage2Params.hiMode = cms.uint32(1)" >> $config_l1Ntuple

# process.caloStage2Params is somehow not seen. needed to use customiseSettings.L1TSettingsToCaloStage2Params_XXX to make it appear
#echo "process.caloStage2Params.egBypassExtHOverE = cms.uint32(1)" >> $config_l1Ntuple
#echo "process.caloStage2Params.egBypassShape = cms.uint32(1)" >> $config_l1Ntuple
#echo "process.caloStage2Params.egBypassECALFG = cms.uint32(1)" >> $config_l1Ntuple
#echo "process.caloStage2Params.egHOverEcutBarrel = cms.int32(1)" >> $config_l1Ntuple
#echo "process.caloStage2Params.egHOverEcutEndcap = cms.int32(1)" >> $config_l1Ntuple
echo "process.caloStage2Params.egEtaCut = cms.int32(24)" >> $config_l1Ntuple  # ignore all the EGs with ieta > 24

config_l1Ntuple_LOG="${config_l1Ntuple/.py/.log}"
echo "# run the config via"
echo "myRun cmsRun $config_l1Ntuple &> $config_l1Ntuple_LOG &"

## dump the full config
config_l1Ntuple_FULL="${config_l1Ntuple/.py/_FULL.py}"
edmConfigDump $config_l1Ntuple > $config_l1Ntuple_FULL
echo "# Full config is also created : $config_l1Ntuple_FULL"

