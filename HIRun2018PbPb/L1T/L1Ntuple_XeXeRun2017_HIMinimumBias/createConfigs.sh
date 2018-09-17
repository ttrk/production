#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

inputFile="root://cms-xrd-global.cern.ch//store/hidata/XeXeRun2017/HIMinimumBias8/RAW/v1/000/304/899/00000/02339E6D-94AF-E711-A9FC-02163E0122EE.root"

## Software
# CMSSW_10_2_1, l1t-integration-v99.0
# This integration contains the new L1 EG bypass flags : https://github.com/cms-l1t-offline/cmssw/pull/708
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideL1TStage2Instructions?rev=140#Environment_Setup_with_Integrati
## Driver
# https://twiki.cern.ch/twiki/bin/view/CMS/L1HITaskForce?rev=50#Offline_SW_setup
ERA="Run2_2017_pp_on_XeXe"
GLOBALTAG="auto:run2_data"
nEvents=100
configPrefix="l1Ntuple"

$runCmd cmsDriver.py $configPrefix -s RAW2DIGI --era=$ERA \
--customise=L1Trigger/Configuration/customiseReEmul.L1TReEmulFromRAW \
--customise=L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleEMU \
--customise=L1Trigger/Configuration/customiseUtils.L1TTurnOffUnpackStage2GtGmtAndCalo \
--customise=FWCore/ParameterSet/MassReplace.massReplaceInputTag \
--customise=L1Trigger/Configuration/customiseSettings.L1TSettingsToCaloStage2Params_v3_3_HI \
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

