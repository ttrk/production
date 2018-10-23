#!/bin/bash

# instructions : https://twiki.cern.ch/twiki/bin/view/CMS/HiHighPtTrigger2018?rev=32#Instructions_as_of_2018_10_14_in
## obsolete instructions : https://twiki.cern.ch/twiki/bin/view/CMS/HIRunPreparations2018HLT?rev=26
# software : CMSSW_10_3_0_pre6
# L1 tag : l1t-integration-v101.0 with CMSSW_10_2_1

## Download the L1T Calo calibration and LUT files via
# git clone https://github.com/cms-l1t-offline/L1Trigger-L1TCalorimeter.git L1Trigger/L1TCalorimeter/data

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

## sample with DIGI earlier than 103Xpre4
#inputFile="root://xrootd.cmsaf.mit.edu//store/user/clindsey/Pythia8_AllQCDPhoton15_Hydjet_Quenched_Cymbal5Ev8/RAWSIM_20180630/180630_163544/0000/step1_DIGI_L1_DIGI2RAW_HLT_PU_1.root"
## sample with DIGI made with or after 103Xpre4
inputFile="/store/user/mnguyen/AllQCDPhoton30_Hydjet_Quenched_Cymbal5Ev8_5020GeV_DIGI2RAW_103X_upgrade2018_realistic_HI_v4/Pythia8_AllQCDPhoton30_Hydjet_Quenched_Cymbal5Ev8/crab_AllQCDPhoton30_Hydjet_Quenched_Cymbal5Ev8_5020GeV_DIGI2RAW_103X_upgrade2018_realistic_HI_v4/181013_203555/0000/step1_private_DIGI_L1_DIGI2RAW_HLT_PU_99.root"

# menu V9 was used in the first jira ticket for PbPb 2018 photon paths : https://its.cern.ch/jira/browse/CMSHLT-2008
menu="/dev/CMSSW_10_3_0/HIon/V7"
configFile="hltConfig.py"
GLOBALTAG="103X_upgrade2018_realistic_HI_v6"
SETUP="/dev/CMSSW_10_3_0/GRun"
PROCESS="MyHLT"
nEvents="100"
DATAMC="--mc"
CUSTOMISE="--customise L1Trigger/Configuration/customiseSettings.L1TSettingsToCaloParams_2018_v1_4"
L1EMU="--l1-emulator FullMC"
## L1 menu v4 : https://hypernews.cern.ch/HyperNews/CMS/get/hi-general/5380/2/1/1.html
L1XML="L1Menu_CollisionsHeavyIons2018_v4.xml"
## L1 menu v3 : https://hypernews.cern.ch/HyperNews/CMS/get/hi-general/5290.html
#L1XML="L1Menu_CollisionsHeavyIons2018_v3.xml"

isXeXeData=0
if [ $isXeXeData -gt 0 ]; then
  inputFile="/store/hidata/XeXeRun2017/HIMinimumBias8/RAW/v1/000/304/906/00000/FA373F85-ACAF-E711-A6F2-02163E01A6EA.root"
  GLOBALTAG="auto:run2_data_GRun"
  nEvents="500"
  DATAMC="--data"
  CUSTOMISE="--customise FWCore/ParameterSet/MassReplace.massReplaceInputTag,L1Trigger/Configuration/customiseSettings.L1TSettingsToCaloParams_2018_v1_4"
  L1EMU="--l1-emulator Full"
fi

## https://twiki.cern.ch/twiki/bin/view/CMS/HiHighPtTrigger2018?rev=28#Instructions_as_of_2018_10_14_in
hltGetConfiguration $menu --globaltag $GLOBALTAG --input $inputFile --setup $SETUP --process $PROCESS \
--full --offline $DATAMC --unprescale $L1EMU --l1Xml $L1XML $CUSTOMISE \
--max-events $nEvents > $configFile
# --l1-emulator Full : runs full L1 emulator, avoids L1 prescales

#beamspot customization
echo "" >> $configFile
echo "import CalibTracker.Configuration.Common.PoolDBESSource_cfi" >> $configFile
echo "process.newBS = CalibTracker.Configuration.Common.PoolDBESSource_cfi.poolDBESSource.clone(connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'), toGet = cms.VPSet(cms.PSet(record = cms.string('BeamSpotObjectsRcd'), tag = cms.string('BeamSpotObjects_Realistic25ns_13TeVCollisions_Early2017_v1_mc'))))" >> $configFile
echo "process.prefer_PreferNewBS = cms.ESPrefer('PoolDBESSource', 'newBS')" >> $configFile

#muon customization (via Emilien)
echo "" >> $configFile
echo "process.simEmtfDigis.CSCInputBXShift = cms.int32(-6)" >> $configFile

#Jet customization (via Chris)
echo "" >> $configFile
echo "process.caloStage2Params.hiMode = cms.uint32(1)" >> $configFile
echo "process.caloStage2Params.jetPUSType = cms.string('PhiRing2')" >> $configFile
echo "process.caloStage2Params.jetPUSUseChunkySandwich = cms.uint32(False)" >> $configFile

# Centrality customization (via Jing)
echo "" >> $configFile
echo "process.caloStage2Params.etSumCentralityLower = cms.vdouble(0.0, 1.35, 7.15, 71.0, 219.5, 583.4, 1310.6, 65535.0)" >> $configFile
echo "process.caloStage2Params.etSumCentralityUpper = cms.vdouble(4.15, 13.6, 110.95, 302.1, 713.35, 1464.35, 2664.05, 65535.0)" >> $configFile

#EG Spike killer customization (via Chris/Kaya)
echo "" >> $configFile
echo "process.simEcalTriggerPrimitiveDigis = cms.EDProducer('EcalTrigPrimProducer', BarrelOnly = cms.bool(False), Debug = cms.bool(False), Famos = cms.bool(False), InstanceEB = cms.string('ebDigis'), InstanceEE = cms.string('eeDigis'), Label = cms.string('unpackEcal'), TcpOutput = cms.bool(False), binOfMaximum = cms.int32(6))" >> $configFile
echo "" >> $configFile
echo "process.simCaloStage2Layer1Digis.ecalToken = cms.InputTag('simEcalTriggerPrimitiveDigis')" >> $configFile
echo "" >> $configFile
echo "process.SimL1Emulator = cms.Sequence(process.unpackRPC+process.unpackDT+process.unpackCSC+process.unpackEcal+process.unpackHcal+process.simHcalTriggerPrimitiveDigis+process.simEcalTriggerPrimitiveDigis+((process.simCaloStage2Layer1Digis+process.simCaloStage2Digis)+((process.simDtTriggerPrimitiveDigis+process.simCscTriggerPrimitiveDigis)+process.simTwinMuxDigis+process.simBmtfDigis+process.simEmtfDigis+process.simOmtfDigis+process.simGmtCaloSumDigis+process.simGmtStage2Digis)+(process.simGtExtFakeStage2Digis)+process.SimL1TGlobal)+process.packCaloStage2+process.packGmtStage2+process.packGtStage2+process.rawDataCollector)" >> $configFile
strGTtoGet1="cms.PSet(record = cms.string('EcalTPGFineGrainStripEERcd'), tag = cms.string('EcalTPGFineGrainStrip_12'), connect =cms.string('frontier://FrontierPrep/CMS_CONDITIONS')), cms.PSet(record = cms.string('EcalTPGSpikeRcd'), tag = cms.string('EcalTPGSpike_12'), connect =cms.string('frontier://FrontierPrep/CMS_CONDITIONS'))"
strGTtoGet=$strGTtoGet1

#Fix for hcal electroics map running on old digi
#believe this is related to issues running pre5 reco on digi from pre4 or earlier
#see twiki here: https://twiki.cern.ch/twiki/bin/view/CMS/HiHighPtRecoValidation2018#Starting_from_other_CMSSW_10_3_p
#DO NOT DO THE NEXT TWO LINES IF YOUR RAW/DIGI is 1030pre5 OR LATER
#strGTtoGet2="cms.PSet(record = cms.string('HcalElectronicsMapRcd'), tag = cms.string('HcalElectronicsMap_2018_v3.0_mc'), connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'), globaltag=cms.string('103X_upgrade2018_realistic_v4'))" #IF YOU FAIL PROCESSING RAW/DIGI 1030pre5 OR LATER THIS IS THE LIKELY CAUSE
#strGTtoGet=$strGTtoGet1", "$strGTtoGet2

## custom GT for Spike Killer and/or Hcal electronics map
echo "" >> $configFile
echo "process.GlobalTag.toGet = cms.VPSet(${strGTtoGet})" >> $configFile

#Remove dQMIO output
sed -i -e "s@process.DQMOutput @#process.DQMOutput @g" $configFile

## L1TSettingsToCaloParams_2018_v1_4 is now available in CMSSW_10_3_0_pre5
## settings for L1 EG : https://twiki.cern.ch/twiki/bin/view/CMS/HIRunPreparations2018HLT#How_to_run_L1_EGs
echo "process.caloStage2Params.egEtaCut = cms.int32(24)" >> $configFile  # ignore all the EGs with ieta > 24

echo 'process.options.numberOfThreads=cms.untracked.uint32(1)' >> $configFile

if [ $isXeXeData -gt 0 ]; then
  oldStr="process\s=\smassReplaceInputTag(process)"
  # process = massReplaceInputTag(process, "rawDataCollector", "rawDataRepacker", False, True)
  # process.rawDataRepacker = process.rawDataCollector.clone()
  # process.SimL1Emulator.replace(process.rawDataCollector, process.rawDataRepacker)
  newStr1="process = massReplaceInputTag(process, \"rawDataCollector\", \"rawDataRepacker\", False, True)"
  newStr2="process.rawDataRepacker = process.rawDataCollector.clone()"
  newStr3="process.SimL1Emulator.replace(process.rawDataCollector, process.rawDataRepacker)"
  newStr=$newStr1"\n"$newStr2"\n"$newStr3
  sed -i "s/${oldStr}/${newStr}/g" $configFile
fi

## MOD : loose hltRechitInRegionsECAL eta-phi Margin for PF clustering
#echo 'process.hltRechitInRegionsECAL.l1InputRegions[0].regionEtaMargin = cms.double(1.4)' >> $configFile
#echo 'process.hltRechitInRegionsECAL.l1InputRegions[0].regionPhiMargin = cms.double(2.4)' >> $configFile

## MOD : loose hltRechitInRegionsECAL for PF clustering
#echo 'process.hltRechitInRegionsECAL.l1InputRegions[0].minEt = cms.double(1.0)' >> $configFile

## MOD : change Rechit threshold test
#echo "process.hltParticleFlowRecHitECALL1Seeded.producers[0].qualityTests[0] = cms.PSet(applySelectionsToAllCrystals = cms.bool(True), name = cms.string('PFRecHitQTestDBThreshold'))" >> $configFile
#echo "process.hltParticleFlowRecHitECALL1Seeded.producers[1].qualityTests[0] = cms.PSet(applySelectionsToAllCrystals = cms.bool(True), name = cms.string('PFRecHitQTestDBThreshold'))" >> $configFile

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
"HLT_HIGEDPhoton10",
"HLT_HIGEDPhoton15",
"HLT_HIGEDPhoton20",
"HLT_HIGEDPhoton30",
"HLT_HIGEDPhoton40",
"HLT_HIGEDPhoton50",
"HLT_HIGEDPhoton60",
"HLT_HIGEDPhoton10_HECut",
"HLT_HIGEDPhoton15_HECut",
"HLT_HIGEDPhoton20_HECut",
"HLT_HIGEDPhoton30_HECut",
"HLT_HIGEDPhoton40_HECut",
"HLT_HIGEDPhoton50_HECut",
"HLT_HIGEDPhoton60_HECut",
"HLT_HIGEDPhoton10_EB",
"HLT_HIGEDPhoton15_EB",
"HLT_HIGEDPhoton20_EB",
"HLT_HIGEDPhoton30_EB",
"HLT_HIGEDPhoton40_EB",
"HLT_HIGEDPhoton50_EB",
"HLT_HIGEDPhoton60_EB",
"HLT_HIGEDPhoton10_EB_HECut",
"HLT_HIGEDPhoton15_EB_HECut",
"HLT_HIGEDPhoton20_EB_HECut",
"HLT_HIGEDPhoton30_EB_HECut",
"HLT_HIGEDPhoton40_EB_HECut",
"HLT_HIGEDPhoton50_EB_HECut",
"HLT_HIGEDPhoton60_EB_HECut",
"HLT_HIIslandPhoton10_Eta3p1",
"HLT_HIIslandPhoton15_Eta3p1",
"HLT_HIIslandPhoton20_Eta3p1",
"HLT_HIIslandPhoton30_Eta3p1",
"HLT_HIIslandPhoton40_Eta3p1",
"HLT_HIIslandPhoton50_Eta3p1",
"HLT_HIIslandPhoton60_Eta3p1",
"HLT_HIIslandPhoton10_Eta1p5",
"HLT_HIIslandPhoton15_Eta1p5",
"HLT_HIIslandPhoton20_Eta1p5",
"HLT_HIIslandPhoton30_Eta1p5",
"HLT_HIIslandPhoton40_Eta1p5",
"HLT_HIIslandPhoton50_Eta1p5",
"HLT_HIIslandPhoton60_Eta1p5"
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

