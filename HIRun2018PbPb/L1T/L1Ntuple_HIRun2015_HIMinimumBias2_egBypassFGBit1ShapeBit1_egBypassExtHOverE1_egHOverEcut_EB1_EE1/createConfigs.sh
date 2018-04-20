#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

inputFile="root://xrootd.cmsaf.mit.edu//store/hidata/HIRun2015/HIMinimumBias2/RAW/v1/000/263/261/00000/0029C4B7-149B-E511-BEEE-02163E01431C.root"

# https://twiki.cern.ch/twiki/bin/view/CMS/L1HITaskForce?rev=16#Offline_SW_setup
$runCmd cmsDriver.py l1Ntuple -s RAW2DIGI --era=Run2_2017 --customise=L1Trigger/Configuration/customiseReEmul.L1TEventSetupForHF1x1TPs --customise=L1Trigger/Configuration/customiseReEmul.L1TReEmulFromRAW2015 --customise=L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleEMU --customise=L1Trigger/Configuration/customiseUtils.L1TTurnOffUnpackStage2GtGmtAndCalo --customise=FWCore/ParameterSet/MassReplace.massReplaceInputTag --conditions=auto:run1_data -n 100 --data --no_exec --no_output --filein=$inputFile &> cmsDriver_l1Ntuple_RAW2DIGI.log
## do not use --conditions=92X_dataRun2_HLT_XeXe_v1. It gives the exception with following message : No "RPCOMTFLinkMapRcd" record found in the EventSetup for synchronization value

config_l1Ntuple="l1Ntuple_RAW2DIGI.py"
echo "process.simCaloStage2Layer1Digis.hcalToken = cms.InputTag('hcalDigis')" >> $config_l1Ntuple # use the unpacked HCal Trigger Primitive instead of the simulated one
echo "process.caloStage2Params.egBypassFGBit = cms.uint32(1)" >> $config_l1Ntuple
echo "process.caloStage2Params.egBypassShapeBit = cms.uint32(1)" >> $config_l1Ntuple
echo "process.caloStage2Params.egBypassExtHOverE = cms.uint32(1)" >> $config_l1Ntuple
echo "process.caloStage2Params.egHOverEcutBarrel = cms.int32(1)" >> $config_l1Ntuple
echo "process.caloStage2Params.egHOverEcutEndcap = cms.int32(1)" >> $config_l1Ntuple

config_l1Ntuple_LOG="${config_l1Ntuple/.py/.log}"
echo "# run the config via"
echo "myRun cmsRun $config_l1Ntuple &> $config_l1Ntuple_LOG &"

## dump the full config
config_l1Ntuple_FULL="${config_l1Ntuple/.py/_FULL.py}"
edmConfigDump $config_l1Ntuple > $config_l1Ntuple_FULL
echo "# Full config is also created : $config_l1Ntuple_FULL"

#config_l1Ntuple_FULL_LOG="${config_l1Ntuple_FULL/.py/.log}"
#echo "myRun cmsRun $config_l1Ntuple_FULL &> $config_l1Ntuple_FULL_LOG &"
## dump the full config - END
