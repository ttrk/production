#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

inputFile="root://cms-xrd-global.cern.ch//store/hidata/XeXeRun2017/HIMinimumBias7/RAW/v1/000/304/899/00000/000AB151-8CAF-E711-A03A-02163E019BA4.root"

# https://twiki.cern.ch/twiki/bin/view/CMS/L1HITaskForce?rev=38#Offline_SW_setup
# https://twiki.cern.ch/twiki/bin/view/CMS/HiHighPtTrigger2018?rev=15#Running_L1Ntuple
$runCmd cmsDriver.py l1Ntuple -s RAW2DIGI --era=Run2_2017_pp_on_XeXe --customise=L1Trigger/Configuration/customiseReEmul.L1TReEmulFromRAW --customise=L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleEMU --customise=L1Trigger/Configuration/customiseUtils.L1TTurnOffUnpackStage2GtGmtAndCalo --customise=FWCore/ParameterSet/MassReplace.massReplaceInputTag --conditions=100X_dataRun2_v1 -n 100 --data --no_exec --no_output --filein=$inputFile &> cmsDriver_l1Ntuple_RAW2DIGI.log

config_l1Ntuple="l1Ntuple_RAW2DIGI.py"
echo "process.caloStage2Params.hiFlag = cms.uint32(1)" >> $config_l1Ntuple
pusType="PhiRingHITower"
echo "process.caloStage2Params.jetPUSType = cms.string('$pusType')" >> $config_l1Ntuple

config_l1Ntuple_LOG="${config_l1Ntuple/.py/.log}"
echo "# run the config via"
echo "myRun cmsRun $config_l1Ntuple &> $config_l1Ntuple_LOG &"

## dump the full config
config_l1Ntuple_FULL="${config_l1Ntuple/.py/_FULL.py}"
edmConfigDump $config_l1Ntuple > $config_l1Ntuple_FULL
echo "# Full config is also created : $config_l1Ntuple_FULL"

