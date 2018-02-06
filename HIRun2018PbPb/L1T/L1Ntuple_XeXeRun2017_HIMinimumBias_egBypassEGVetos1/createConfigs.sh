#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

inputFile="root://cms-xrd-global.cern.ch//store/hidata/XeXeRun2017/HIMinimumBias8/RAW/v1/000/304/899/00000/02339E6D-94AF-E711-A9FC-02163E0122EE.root"

$runCmd cmsDriver.py l1Ntuple -s RAW2DIGI --era=Run2_2017_pp_on_XeXe --customise=L1Trigger/Configuration/customiseReEmul.L1TReEmulFromRAWCalouGT --customise=L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleEMU --customise=L1Trigger/Configuration/customiseUtils.L1TTurnOffUnpackStage2GtGmtAndCalo --customise=FWCore/ParameterSet/MassReplace.massReplaceInputTag --conditions=94X_dataRun2_v2 -n 100 --data --no_exec --no_output --filein=$inputFile &> cmsDriver_l1Ntuple_RAW2DIGI.log
## do not use --conditions=92X_dataRun2_HLT_XeXe_v1. It gives the exception with following message : No "RPCOMTFLinkMapRcd" record found in the EventSetup for synchronization value

config_l1Ntuple="l1Ntuple_RAW2DIGI.py"
echo "process.caloStage2Params.hiFlag = cms.uint32(0)" >> $config_l1Ntuple
echo "process.caloStage2Params.egBypassEGVetos = cms.uint32(1)" >> $config_l1Ntuple

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
