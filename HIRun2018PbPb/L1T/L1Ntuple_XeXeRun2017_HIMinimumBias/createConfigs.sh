#!/bin/bash

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

inputFile="root://xrootd.cmsaf.mit.edu//store/hidata/XeXeRun2017/HIMinimumBias8/RAW/v1/000/304/899/00000/02339E6D-94AF-E711-A9FC-02163E0122EE.root"
#inputFile="root://xrootd.cmsaf.mit.edu//store/hidata/XeXeRun2017/HIMinimumBias8/RAW/v1/000/304/875/00000/CA409ED8-58AF-E711-9918-02163E01A3EA.root"
#inputFile="file:CA409ED8-58AF-E711-9918-02163E01A3EA.root"

$runCmd cmsDriver.py l1Ntuple -s RAW2DIGI --era=Run2_2017_pp_on_XeXe --customise=L1Trigger/Configuration/customiseReEmul.L1TReEmulFromRAWCalouGT --customise=L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleEMU --customise=L1Trigger/Configuration/customiseUtils.L1TTurnOffUnpackStage2GtGmtAndCalo --conditions=94X_dataRun2_v2 -n 100 --data --no_exec --no_output --filein=$inputFile &> cmsDriver_l1Ntuple_RAW2DIGI.log
## do not use --conditions=92X_dataRun2_HLT_XeXe_v1. It gives the exception with following message : No "RPCOMTFLinkMapRcd" record found in the EventSetup for synchronization value

config_l1Ntuple="l1Ntuple_RAW2DIGI.py"
config_l1Ntuple_FULL="${config_l1Ntuple/.py/_FULL.py}"
edmConfigDump $config_l1Ntuple > $config_l1Ntuple_FULL

cp $config_l1Ntuple_FULL "${config_l1Ntuple_FULL/.py/.BACKUP.py}"
# replace "rawDataCollector" with "rawDataRepacker"
sed -i "s/rawDataCollector/rawDataRepacker/g" $config_l1Ntuple_FULL

echo "run the configs via"
echo "myRun cmsRun $config_l1Ntuple &> ${config_l1Ntuple/.py/.log} &"
echo "myRun cmsRun $config_l1Ntuple_FULL &> ${config_l1Ntuple_FULL/.py/.log} &"

