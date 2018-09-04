#!/bin/bash

# instructions : https://twiki.cern.ch/twiki/bin/view/CMS/HIRunPreparations2018HLT?rev=15
# software : CMSSW_10_1_2
# L1 tag : cms-l1t-offline:l1t-integration-v97.27.1-CMSSW_10_1_2

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

inputFile="root://xrootd.cmsaf.mit.edu//store/user/clindsey/Pythia8_AllQCDPhoton15_Hydjet_Quenched_Cymbal5Ev8/RAWSIM_20180630/180630_163544/0000/step1_DIGI_L1_DIGI2RAW_HLT_PU_1.root"

menu="/users/katatar/HI2018PbPb/hltTestEgamma/V29"
configFile="hltConfig.py"
nEvents="100"

hltGetConfiguration $menu --globaltag auto:run2_mc_GRun --input $inputFile --setup /dev/CMSSW_10_1_0/GRun --process MyHLT --full --offline --mc --unprescale --l1-emulator FullMC --max-events $nEvents > $configFile
# --l1-emulator Full : runs full L1 emulator, avoids L1 prescales

echo 'process.options.numberOfThreads=cms.untracked.uint32(1)' >> $configFile

# Add hltBitAnalyzer
echo '' >> $configFile
echo 'process.load("HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi")' >> $configFile
echo 'process.hltbitanalysis.HLTProcessName = cms.string("MyHLT")' >> $configFile
echo 'process.hltbitanalysis.hltresults = cms.InputTag("TriggerResults", "", "MyHLT")' >> $configFile
echo 'process.hltbitanalysis.l1results = cms.InputTag("hltGtStage2Digis", "", "MyHLT")' >> $configFile
echo 'process.hltbitanalysis.UseTFileService = cms.untracked.bool(True)' >> $configFile
echo 'process.hltbitanalysis.RunParameters = cms.PSet(' >> $configFile
echo '   isData = cms.untracked.bool(True))' >> $configFile
echo 'process.hltBitAnalysis = cms.EndPath(process.hltbitanalysis)' >> $configFile
echo 'process.TFileService = cms.Service("TFileService",' >> $configFile
echo '   fileName=cms.string("openHLT.root"))' >> $configFile

configFileLOG="${configFile/.py/.log}"
echo "# run the config via"
echo "myRun cmsRun $configFile &> $configFileLOG &"

## dump the full config
configFileFULL="${configFile/.py/_FULL.py}"
edmConfigDump $configFile > $configFileFULL
echo "# Full config is also created : $configFileFULL"

cp $configFileFULL "${configFileFULL/.py/.BACKUP.py}"
## need to fix some lines in the full config
sed -i "s/L1T INFO/#L1T INFO/g" $configFileFULL
sed -i "s/process.hgcalTriggerPrimitives = cms.Sequence/#process.hgcalTriggerPrimitives = cms.Sequence/g" $configFileFULL
sed -i "s/process.hgcalTriggerPrimitives_reproduce = cms.Sequence/#process.hgcalTriggerPrimitives_reproduce = cms.Sequence/g" $configFileFULL

configFileFULLLOG="${configFileFULL/.py/.log}"
echo "# run the FULL config via"
echo "myRun cmsRun $configFileFULL &> $configFileFULLLOG &"

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

