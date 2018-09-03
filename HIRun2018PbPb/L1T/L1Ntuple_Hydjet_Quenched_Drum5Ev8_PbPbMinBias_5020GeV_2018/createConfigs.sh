#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

#https://twiki.cern.ch/twiki/bin/view/CMS/PbPb5TeV2018OfficialMC?rev=15#Available_Samples_AN1
inputFile="/store/himc/HINPbPbSpring18DR/Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM-RAW/NoPU_100X_upgrade2018_realistic_v10_ext1-v1/00001/FE243EFA-6DAB-E811-BFDE-9CB654AD72EC.root"

## Software
# CMSSW_10_2_1, l1t-integration-v99.0
# This integration contains the new L1 EG bypass flags : https://github.com/cms-l1t-offline/cmssw/pull/708
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideL1TStage2Instructions?rev=140#Environment_Setup_with_Integrati
## Driver
# https://twiki.cern.ch/twiki/bin/view/CMS/L1HITaskForce?rev=42#Offline_SW_setup
ERA="Run2_2018"
GLOBALTAG="101X_upgrade2018_realistic_v7"
nEvents=500
configPrefix="l1Ntuple"

### modify input for calo digi collection
## https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideL1TStage2Instructions?rev=141#Workflows_AN1
#--customise=L1Trigger/Configuration/customiseReEmul.L1TReEmulMCFromRAWSimCalTP
# https://github.com/cms-sw/cmssw/blob/master/L1Trigger/Configuration/python/customiseReEmul.py#L253-L254
# https://github.com/cms-sw/cmssw/blob/71741cd7aea763fce2c07ca50370cd14b7edd261/L1Trigger/Configuration/python/customiseReEmul.py#L253-L254

$runCmd cmsDriver.py $configPrefix -s RAW2DIGI --era=Run2_2018 \
--customise=L1Trigger/Configuration/customiseReEmul.L1TReEmulMCFromRAWSimCalTP \
--customise=L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleEMU \
--customise=L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleGEN \
--customise=L1Trigger/Configuration/customiseUtils.L1TTurnOffUnpackStage2GtGmtAndCalo \
--customise=L1Trigger/Configuration/customiseSettings.L1TSettingsToCaloParams_2018_v1_2 \
--customise_commands="process.simTwinMuxDigis.DTDigi_Source = cms.InputTag('bmtfDigis')\n process.simTwinMuxDigis.DTThetaDigi_Source = cms.InputTag('bmtfDigis')\n process.simTwinMuxDigis.RPC_Source = cms.InputTag('muonRPCDigis')\n" \
--conditions=$GLOBALTAG -n $nEvents --mc --no_exec --no_output --filein=$inputFile &> cmsDriver_l1Ntuple_RAW2DIGI.log

config_l1Ntuple=$configPrefix"_RAW2DIGI.py"

# process.caloStage2Params is somehow not seen. needed to use customiseSettings.L1TSettingsToCaloStage2Params_XXX to make it appear
echo "process.caloStage2Params.egBypassExtHOverE = cms.uint32(1)" >> $config_l1Ntuple
echo "process.caloStage2Params.egBypassShape = cms.uint32(1)" >> $config_l1Ntuple
echo "process.caloStage2Params.egBypassECALFG = cms.uint32(1)" >> $config_l1Ntuple
echo "process.caloStage2Params.egHOverEcutBarrel = cms.int32(1)" >> $config_l1Ntuple
echo "process.caloStage2Params.egHOverEcutEndcap = cms.int32(1)" >> $config_l1Ntuple
echo "process.caloStage2Params.egEtaCut = cms.int32(24)" >> $config_l1Ntuple  # ignore all the EGs with ieta > 24

config_l1Ntuple_LOG="${config_l1Ntuple/.py/.log}"
echo "# run the config via"
echo "myRun cmsRun $config_l1Ntuple &> $config_l1Ntuple_LOG &"

## dump the full config
config_l1Ntuple_FULL="${config_l1Ntuple/.py/_FULL.py}"
edmConfigDump $config_l1Ntuple > $config_l1Ntuple_FULL
echo "# Full config is also created : $config_l1Ntuple_FULL"

