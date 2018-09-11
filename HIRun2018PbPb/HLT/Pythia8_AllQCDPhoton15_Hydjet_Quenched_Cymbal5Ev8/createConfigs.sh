#!/bin/bash

# instructions : https://twiki.cern.ch/twiki/bin/view/CMS/HIRunPreparations2018HLT?rev=15
# software : CMSSW_10_1_2
# L1 tag : cms-l1t-offline:l1t-integration-v97.27.1-CMSSW_10_1_2

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

inputFile="root://xrootd.cmsaf.mit.edu//store/user/clindsey/Pythia8_AllQCDPhoton15_Hydjet_Quenched_Cymbal5Ev8/RAWSIM_20180630/180630_163544/0000/step1_DIGI_L1_DIGI2RAW_HLT_PU_1.root"

menu="/users/katatar/HI2018PbPb/hltTestEgamma/V34"
configFile="hltConfig.py"
GLOBALTAG="auto:run2_mc_GRun"
SETUP="/dev/CMSSW_10_1_0/GRun"
PROCESS="MyHLT"
nEvents="100"
DATAMC="--mc"
CUSTOMISE="--customise HLTrigger/Configuration/customizeHLTforCMSSW.customiseFor2017DtUnpacking"
L1EMU="--l1-emulator FullMC"

## https://twiki.cern.ch/twiki/bin/view/CMS/HIRunPreparations2018HLT?rev=26#Testing_new_paths_with_PbPb_MC
hltGetConfiguration $menu --globaltag $GLOBALTAG --input $inputFile --setup $SETUP --process $PROCESS \
--full --offline $DATAMC --unprescale $L1EMU $CUSTOMISE \
--max-events $nEvents > $configFile
# --l1Xml L1Menu_CollisionsHeavyIons2018_v1.xml
# --l1-emulator Full : runs full L1 emulator, avoids L1 prescales

echo 'process.options.numberOfThreads=cms.untracked.uint32(1)' >> $configFile

## MOD : loose hltRechitInRegionsECAL for PF clustering
#echo 'process.hltRechitInRegionsECAL.l1InputRegions[0].minEt = cms.double(0.5)' >> $configFile

## MOD : use unfiltered rechit collection for PF clustering, not hltRechitInRegionsECAL
#echo 'process.hltParticleFlowRecHitECALL1Seeded.producers[0].src = cms.InputTag("hltEcalRecHit","EcalRecHitsEB")' >> $configFile
#echo 'process.hltParticleFlowRecHitECALL1Seeded.producers[1].src = cms.InputTag("hltEcalRecHit","EcalRecHitsEE")' >> $configFile

# Add hltBitAnalyzer
echo '' >> $configFile
echo 'process.load("HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi")' >> $configFile
echo 'process.hltbitanalysis.HLTProcessName = cms.string("'${PROCESS}'")' >> $configFile
echo 'process.hltbitanalysis.hltresults = cms.InputTag("TriggerResults", "", "'${PROCESS}'")' >> $configFile
echo 'process.hltbitanalysis.l1results = cms.InputTag("hltGtStage2Digis", "", "'${PROCESS}'")' >> $configFile
echo 'process.hltbitanalysis.UseTFileService = cms.untracked.bool(True)' >> $configFile
echo 'process.hltbitanalysis.RunParameters = cms.PSet(' >> $configFile
echo '   isData = cms.untracked.bool(True))' >> $configFile
echo 'process.hltBitAnalysis = cms.EndPath(process.hltbitanalysis)' >> $configFile
echo 'process.TFileService = cms.Service("TFileService",' >> $configFile
echo '   fileName=cms.string("openHLT.root"))' >> $configFile

# Add hltobject
echo 'process.load("HeavyIonsAnalysis.EventAnalysis.hltobject_PbPb_cfi")' >> $configFile
echo 'process.hltobject.processName = cms.string("'${PROCESS}'")' >> $configFile
echo 'process.hltobject.triggerResults = cms.InputTag("TriggerResults", "", "'${PROCESS}'")' >> $configFile
echo 'process.hltobject.triggerEvent = cms.InputTag("hltTriggerSummaryAOD", "", "'${PROCESS}'")' >> $configFile
echo 'process.hltobject.triggerNames = cms.vstring(
"HLT_GEDPhoton10",
"HLT_GEDPhoton15",
"HLT_GEDPhoton20",
"HLT_GEDPhoton30",
"HLT_GEDPhoton40",
"HLT_GEDPhoton50",
"HLT_GEDPhoton60",
"HLT_GEDPhoton10_HECut",
"HLT_GEDPhoton15_HECut",
"HLT_GEDPhoton20_HECut",
"HLT_GEDPhoton30_HECut",
"HLT_GEDPhoton40_HECut",
"HLT_GEDPhoton50_HECut",
"HLT_GEDPhoton60_HECut",
"HLT_GEDPhoton10_EB",
"HLT_GEDPhoton15_EB",
"HLT_GEDPhoton20_EB",
"HLT_GEDPhoton30_EB",
"HLT_GEDPhoton40_EB",
"HLT_GEDPhoton50_EB",
"HLT_GEDPhoton60_EB",
"HLT_EG10UM",
"HLT_EG15UM",
"HLT_EG20UM",
"HLT_EG30UM",
"HLT_EG40UM",
"HLT_EG50UM",
"HLT_EG60UM",
"HLT_EG10HEUM",
"HLT_EG15HEUM",
"HLT_EG20HEUM",
"HLT_EG30HEUM",
"HLT_EG40HEUM",
"HLT_EG50HEUM",
"HLT_EG60HEUM",
"HLT_EG10EBUM",
"HLT_EG15EBUM",
"HLT_EG20EBUM",
"HLT_EG30EBUM",
"HLT_EG40EBUM",
"HLT_EG50EBUM",
"HLT_EG60EBUM",
"HLT_HISinglePhoton10_Eta3p1",
"HLT_HISinglePhoton15_Eta3p1",
"HLT_HISinglePhoton20_Eta3p1",
"HLT_HISinglePhoton30_Eta3p1",
"HLT_HISinglePhoton40_Eta3p1",
"HLT_HISinglePhoton50_Eta3p1",
"HLT_HISinglePhoton60_Eta3p1",
"HLT_HISinglePhoton10_Eta1p5",
"HLT_HISinglePhoton15_Eta1p5",
"HLT_HISinglePhoton20_Eta1p5",
"HLT_HISinglePhoton30_Eta1p5",
"HLT_HISinglePhoton40_Eta1p5",
"HLT_HISinglePhoton50_Eta1p5",
"HLT_HISinglePhoton60_Eta1p5"
)'>> $configFile
echo 'process.hltObject = cms.EndPath(process.hltobject)' >> $configFile

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

