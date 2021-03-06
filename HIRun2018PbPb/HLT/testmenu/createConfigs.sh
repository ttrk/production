#!/bin/bash

# instructions : https://twiki.cern.ch/twiki/bin/view/CMS/HIRunPreparations2018HLT?rev=11
# software : CMSSW_10_1_2
# L1 tag : cms-l1t-offline:l1t-integration-v97.27.1-CMSSW_10_1_2

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

#inputFile="root://xrootd.cmsaf.mit.edu//store/hidata/XeXeRun2017/HIMinimumBias8/RAW/v1/000/304/906/00000/FC95A847-B2AF-E711-8313-02163E012830.root"
inputFile="root://xrootd.cmsaf.mit.edu//store/hidata/XeXeRun2017/HIMinimumBias8/RAW/v1/000/304/898/00000/A0E925FB-89AF-E711-8C82-02163E0144E9.root"
#inputFile="root://xrootd.cmsaf.mit.edu//store/hidata/XeXeRun2017/HIMinimumBias8/RAW/v1/000/304/906/00000/FC95A847-B2AF-E711-8313-02163E012830.root"
#inputFile="root://xrootd.cmsaf.mit.edu//store/data/Run2017G/HighEGJet/RAW/v1/000/306/631/00000/281345C7-8CC9-E711-9D41-02163E01A257.root"

#menu="/users/chenyi/PbPb2018/DefaultMenu/V4"

menu="/users/katatar/HI2018PbPb/hltTestEgamma/V24"
#menu="/users/davidlw/HLT_PbPb2018_FullTrackv2/V23"
#menu="/users/chenyi/PbPb2018/HighPTJetsPbPb2018/V8"
configMenu="menu_hltTestEgamma_v24_Run304898.py"
#configMenu="menu_HLT_PbPb2018_FullTrackv2_v23_Run304898.py"
#configMenu="menu_HighPTJetsPbPb2018_v8_Run304898.py"
nEvents="3000"
customizations="HLTrigger/Configuration/customizeHLTforCMSSW.customiseFor2017DtUnpacking,FWCore/ParameterSet/MassReplace.massReplaceInputTag"

hltGetConfiguration $menu --globaltag 100X_dataRun2_v1 --input $inputFile --setup /dev/CMSSW_10_1_0/GRun --customise $customizations --process MyHLT --full --offline --data --unprescale --l1-emulator Full --max-events $nEvents > $configMenu
# --l1-emulator Full : runs full L1 emulator, avoids L1 prescales

## need to do the following changes if "--l1-emulator Full" option is used
# https://twiki.cern.ch/twiki/bin/view/CMS/HIRunPreparations2018HLT?rev=10#Testing_new_paths
sed -i "s/process = massReplaceInputTag(process)/#process = massReplaceInputTag(process)/g" $configMenu
# replace "rawDataCollector" with "rawDataRepacker"
echo 'process = massReplaceInputTag(process, "rawDataCollector", "rawDataRepacker", False, True)' >> $configMenu
echo 'process.rawDataRepacker = process.rawDataCollector.clone()' >> $configMenu
echo 'process.SimL1Emulator.replace(process.rawDataCollector, process.rawDataRepacker)' >> $configMenu

# Add hltBitAnalyzer
echo '' >> $configMenu
echo 'process.load("HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi")' >> $configMenu
echo 'process.hltbitanalysis.HLTProcessName = cms.string("MyHLT")' >> $configMenu
echo 'process.hltbitanalysis.hltresults = cms.InputTag("TriggerResults", "", "MyHLT")' >> $configMenu
echo 'process.hltbitanalysis.l1results = cms.InputTag("hltGtStage2Digis", "", "MyHLT")' >> $configMenu
echo 'process.hltbitanalysis.UseTFileService = cms.untracked.bool(True)' >> $configMenu
echo 'process.hltbitanalysis.RunParameters = cms.PSet(' >> $configMenu
echo '   isData = cms.untracked.bool(True))' >> $configMenu
echo 'process.hltBitAnalysis = cms.EndPath(process.hltbitanalysis)' >> $configMenu
echo 'process.TFileService = cms.Service("TFileService",' >> $configMenu
echo '   fileName=cms.string("openHLT.root"))' >> $configMenu

## syntax fixes for HLT_PbPb2018_FullTrackv2_v23
#sed -i "s/*(process.HLT_HIFullTracks2018_HighPt8_v1/(process.HLT_HIFullTracks2018_HighPt8_v1/g" $configMenu

configMenuLOG="${configMenu/.py/.log}"
echo "# run the config via"
echo "myRun cmsRun $configMenu &> $configMenuLOG &"
#echo "myRun cmsRun $configMenu 2>&1 | tee $configMenuLOG &"

## dump the full config
configMenuFULL="${configMenu/.py/_FULL.py}"
edmConfigDump $configMenu > $configMenuFULL
echo "# Full config is also created : $configMenuFULL"

cp $configMenuFULL "${configMenuFULL/.py/.BACKUP.py}"
## need to fix some lines in the full config
sed -i "s/L1T INFO/#L1T INFO/g" $configMenuFULL
sed -i "s/process.hgcalTriggerPrimitives = cms.Sequence/#process.hgcalTriggerPrimitives = cms.Sequence/g" $configMenuFULL
sed -i "s/process.hgcalTriggerPrimitives_reproduce = cms.Sequence/#process.hgcalTriggerPrimitives_reproduce = cms.Sequence/g" $configMenuFULL

configMenuFULLLOG="${configMenuFULL/.py/.log}"
echo "# run the FULL config via"
echo "myRun cmsRun $configMenuFULL &> $configMenuFULLLOG &"

## NOTES
# HLT Egamma paths require matching to L1 objects. If there is no L1 object, then HLT paths always fail. This matching can be bypassed by changing HLTEgammaL1TMatchFilterRegional.cc as follows
#$> git diff --unified=0 HLTrigger/Egamma/plugins/HLTEgammaL1TMatchFilterRegional.cc
# diff --git a/HLTrigger/Egamma/plugins/HLTEgammaL1TMatchFilterRegional.cc b/HLTrigger/Egamma/plugins/HLTEgammaL1TMatchFilterRegional.cc
# index 6a31c1c933f..3ea64c7d9bd 100644
# --- a/HLTrigger/Egamma/plugins/HLTEgammaL1TMatchFilterRegional.cc
# +++ b/HLTrigger/Egamma/plugins/HLTEgammaL1TMatchFilterRegional.cc
# @@ -139 +139 @@ HLTEgammaL1TMatchFilterRegional::hltFilter(edm::Event& iEvent, const edm::EventS
# -      if(matchedSCEG || matchedSCJet || matchedSCTau) {
# +      if(matchedSCEG || matchedSCJet || matchedSCTau || true) {
# @@ -164 +164 @@ HLTEgammaL1TMatchFilterRegional::hltFilter(edm::Event& iEvent, const edm::EventS
# -       if(matchedSCEG || matchedSCJet || matchedSCTau) {
# +       if(matchedSCEG || matchedSCJet || matchedSCTau || true) {

