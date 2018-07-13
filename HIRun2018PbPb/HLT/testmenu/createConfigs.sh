#!/bin/bash

# instructions : https://twiki.cern.ch/twiki/bin/view/CMS/HIRunPreparations2018HLT
# software : CMSSW_10_1_2
# L1 tag : cms-l1t-offline:l1t-integration-v97.27.1-CMSSW_10_1_2

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

#inputFile="root://xrootd.cmsaf.mit.edu//store/hidata/XeXeRun2017/HIMinimumBias8/RAW/v1/000/304/906/00000/FC95A847-B2AF-E711-8313-02163E012830.root"
inputFile="root://xrootd.cmsaf.mit.edu//store/hidata/XeXeRun2017/HIMinimumBias8/RAW/v1/000/304/898/00000/A0E925FB-89AF-E711-8C82-02163E0144E9.root"
#inputFile="root://xrootd.cmsaf.mit.edu//store/data/Run2017G/HighEGJet/RAW/v1/000/306/631/00000/281345C7-8CC9-E711-9D41-02163E01A257.root"

#menu="/users/chenyi/PbPb2018/DefaultMenu/V4"
#menu="/users/katatar/HI2018PbPb/hltTestEgamma/V12"
menu="/users/chenyi/PbPb2018/HighPTJetsPbPb2018/V8"
#configMenu="menu_hltTestEgamma_v12_Run304898.py"
configMenu="menu_HighPTJetsPbPb2018_v8_Run304898.py"
nEvents="100"

hltGetConfiguration $menu --globaltag 100X_dataRun2_v1 --input $inputFile --customise HLTrigger/Configuration/customizeHLTforCMSSW.customiseFor2017DtUnpacking --setup /dev/CMSSW_10_1_0/GRun --customise L1Trigger/Configuration/customiseReEmul.L1TReEmulFromRAW --customise L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleEMU --customise L1Trigger/Configuration/customiseUtils.L1TTurnOffUnpackStage2GtGmtAndCalo --customise FWCore/ParameterSet/MassReplace.massReplaceInputTag --process MyHLT --full --offline --data --unprescale --l1-emulator Full --max-events $nEvents > $configMenu
# --l1-emulator Full : runs full L1 emulator, avoids L1 prescales

#echo '' >> $configMenu
#echo 'process.load("HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi")' >> $configMenu
#echo 'process.hltbitanalysis.HLTProcessName = cms.string("MyHLT")' >> $configMenu
#echo 'process.hltbitanalysis.hltresults = cms.InputTag( "TriggerResults","","MyHLT" )' >> $configMenu
#echo 'process.hltbitanalysis.l1GtReadoutRecord = cms.InputTag("simGtDigis","","MyHLT")' >> $configMenu
#echo 'process.hltbitanalysis.l1GctHFBitCounts = cms.InputTag("gctDigis","","MyHLT")' >> $configMenu
#echo 'process.hltbitanalysis.l1GctHFRingSums = cms.InputTag("gctDigis","","MyHLT")' >> $configMenu
#echo 'process.hltbitanalysis.UseTFileService = cms.untracked.bool(True)' >> $configMenu
#echo 'process.hltBitAnalysis = cms.EndPath(process.hltbitanalysis)' >> $configMenu
#echo 'process.TFileService = cms.Service("TFileService",' >> $configMenu
#echo '                                  fileName=cms.string("openHLT.root"))' >> $configMenu

configMenuLOG="${configMenu/.py/.log}"
echo "# run the config via"
echo "myRun cmsRun $configMenu &> $configMenuLOG &"
#echo "myRun cmsRun $configMenu 2>&1 | tee $configMenuLOG &"

## dump the full config
configMenuFULL="${configMenu/.py/_FULL.py}"
edmConfigDump $configMenu > $configMenuFULL
echo "# Full config is also created : $configMenuFULL"

cp $configMenuFULL "${configMenuFULL/.py/.BACKUP.py}"
## need to use the modified FULL config if "--l1-emulator Full" option is used
# replace "rawDataCollector" with "rawDataRepacker"
sed -i "s/rawDataCollector/rawDataRepacker/g" $configMenuFULL
sed -i "s/L1T INFO/#L1T INFO/g" $configMenuFULL
sed -i "s/process.hgcalTriggerPrimitives = cms.Sequence/#process.hgcalTriggerPrimitives = cms.Sequence/g" $configMenuFULL
sed -i "s/process.hgcalTriggerPrimitives_reproduce = cms.Sequence/#process.hgcalTriggerPrimitives_reproduce = cms.Sequence/g" $configMenuFULL

configMenuFULLLOG="${configMenuFULL/.py/.log}"
echo "# run the FULL config via"
echo "myRun cmsRun $configMenuFULL &> $configMenuFULLLOG &"

