#!/bin/bash

# software : CMSSW_10_3_1
# no L1 tag

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"

#inputFile="file:/eos/cms/store/group/phys_heavyions/abaty/Nov11_2018PbPbRun_HLTCrashErrorStreams_Run326547/ErrorDump1_run326547.root"
inputFile="file:/afs/cern.ch/work/k/katatar/public/forest/CMSSW_10_3_1/src/skim_HIHardProbes_RAW/skim_RAW.root"

menu="/users/katatar/HI2018PbPb/hltTestEgamma/V74"
configFile="hltConfig.py"
GLOBALTAG="103X_dataRun2_HLT_v1"
SETUP="/dev/CMSSW_10_3_0/GRun"
PROCESS="MyHLT"
nEvents="20"
DATAMC="--data"
CUSTOMISE=""
PRESCALEOPT="--unprescale"
#PRESCALEOPT="--prescale HI10kHz"
L1EMU="--l1-emulator Full"
## L1 menu v4 : https://hypernews.cern.ch/HyperNews/CMS/get/hi-general/5380/2/1/1.html
#L1XML="L1Menu_CollisionsHeavyIons2018_v4.xml"
L1XML="L1Menu_CollisionsHeavyIons2018_v4_0_0-d1_xml"

#L1MENU="--l1Xml ${L1XML}" # search xml file in local path
L1MENU="--l1 ${L1XML}" # search xml file in database

## https://twiki.cern.ch/twiki/bin/view/CMS/HiHighPtTrigger2018?rev=47#Instructions_as_of_2018_10_26_in
hltGetConfiguration $menu --globaltag $GLOBALTAG --input $inputFile --setup $SETUP --process $PROCESS \
--full --offline $DATAMC --no-output $PRESCALEOPT $L1EMU $L1MENU $CUSTOMISE \
--timing --max-events $nEvents > $configFile
# --l1-emulator Full : runs full L1 emulator, avoids L1 prescales

#beamspot customization
echo "" >> $configFile
echo "import CalibTracker.Configuration.Common.PoolDBESSource_cfi" >> $configFile
echo "process.newBS = CalibTracker.Configuration.Common.PoolDBESSource_cfi.poolDBESSource.clone(connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'), toGet = cms.VPSet(cms.PSet(record = cms.string('BeamSpotObjectsRcd'), tag = cms.string('BeamSpotObjects_Realistic25ns_13TeVCollisions_Early2017_v1_mc'))))" >> $configFile
echo "process.prefer_PreferNewBS = cms.ESPrefer('PoolDBESSource', 'newBS')" >> $configFile

#Remove DQMIO output
sed -i -e "s@process.DQMOutput @#process.DQMOutput @g" $configFile

echo 'process.options.numberOfThreads=cms.untracked.uint32(4)' >> $configFile
echo 'process.DQMStore.enableMultiThread = cms.untracked.bool(False)' >> $configFile

# Add hltBitAnalyzer
echo '' >> $configFile
echo 'process.load("HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi")' >> $configFile
echo 'process.hltbitanalysis.HLTProcessName = cms.string("'${PROCESS}'")' >> $configFile
echo 'process.hltbitanalysis.hltresults = cms.InputTag("TriggerResults", "", "'${PROCESS}'")' >> $configFile
echo 'process.hltbitanalysis.l1results = cms.InputTag("hltGtStage2Digis", "", "'${PROCESS}'")' >> $configFile
echo 'process.hltbitanalysis.UseTFileService = cms.untracked.bool(True)' >> $configFile
echo 'process.hltbitanalysis.RunParameters = cms.PSet(isData = cms.untracked.bool(True))' >> $configFile
echo 'process.hltBitAnalysis = cms.EndPath(process.hltbitanalysis)' >> $configFile
echo 'process.TFileService = cms.Service("TFileService", fileName=cms.string("openHLT.root"))' >> $configFile

# Add hltobject
echo 'process.load("HeavyIonsAnalysis.EventAnalysis.hltobject_PbPb_cfi")' >> $configFile
echo 'process.hltobject.processName = cms.string("'${PROCESS}'")' >> $configFile
echo 'process.hltobject.triggerResults = cms.InputTag("TriggerResults", "", "'${PROCESS}'")' >> $configFile
echo 'process.hltobject.triggerEvent = cms.InputTag("hltTriggerSummaryAOD", "", "'${PROCESS}'")' >> $configFile
echo 'process.hltobject.triggerNames = cms.vstring(
"HLT_HIGEDPhoton10_L1Seeded",
"HLT_HIGEDPhoton15_L1Seeded",
"HLT_HIGEDPhoton20_L1Seeded",
"HLT_HIGEDPhoton30_L1Seeded",
"HLT_HIGEDPhoton40_L1Seeded",
"HLT_HIGEDPhoton50_L1Seeded",
"HLT_HIGEDPhoton60_L1Seeded",
"HLT_HIGEDPhoton10_HECut_L1Seeded",
"HLT_HIGEDPhoton15_HECut_L1Seeded",
"HLT_HIGEDPhoton20_HECut_L1Seeded",
"HLT_HIGEDPhoton30_HECut_L1Seeded",
"HLT_HIGEDPhoton40_HECut_L1Seeded",
"HLT_HIGEDPhoton50_HECut_L1Seeded",
"HLT_HIGEDPhoton60_HECut_L1Seeded",
"HLT_HIGEDPhoton10_EB_L1Seeded",
"HLT_HIGEDPhoton15_EB_L1Seeded",
"HLT_HIGEDPhoton20_EB_L1Seeded",
"HLT_HIGEDPhoton30_EB_L1Seeded",
"HLT_HIGEDPhoton40_EB_L1Seeded",
"HLT_HIGEDPhoton50_EB_L1Seeded",
"HLT_HIGEDPhoton60_EB_L1Seeded",
"HLT_HIGEDPhoton10_EB_HECut_L1Seeded",
"HLT_HIGEDPhoton15_EB_HECut_L1Seeded",
"HLT_HIGEDPhoton20_EB_HECut_L1Seeded",
"HLT_HIGEDPhoton30_EB_HECut_L1Seeded",
"HLT_HIGEDPhoton40_EB_HECut_L1Seeded",
"HLT_HIGEDPhoton50_EB_HECut_L1Seeded",
"HLT_HIGEDPhoton60_EB_HECut_L1Seeded",
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
"HLT_HIIslandPhoton10_Eta2p4",
"HLT_HIIslandPhoton20_Eta2p4",
"HLT_HIIslandPhoton30_Eta2p4",
"HLT_HIIslandPhoton40_Eta2p4",
"HLT_HIIslandPhoton50_Eta2p4",
"HLT_HIIslandPhoton60_Eta2p4",
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
echo "# Config created : $configFile"
echo "# Do NOT run $configFile. Run the FULL config that will appear below."
#echo "# run the config via"
#echo "myRun cmsRun $configFile &> $configFileLOG &"

## dump the full config
configFileFULL="${configFile/.py/_FULL.py}"
edmConfigDump $configFile > $configFileFULL
echo "# Full config is also created : $configFileFULL"

cp $configFileFULL "${configFileFULL/.py/.BACKUP.py}"
## need to fix some lines in the full config
sed -i "s/L1T INFO/#L1T INFO/g" $configFileFULL
sed -i "s/process.hgcalTriggerPrimitives = cms.Sequence/#process.hgcalTriggerPrimitives = cms.Sequence/g" $configFileFULL
sed -i "s/process.hgcalTriggerPrimitives_reproduce = cms.Sequence/#process.hgcalTriggerPrimitives_reproduce = cms.Sequence/g" $configFileFULL

cp $configFileFULL "${configFileFULL/.py/.rawDataCollector.BACKUP.py}"

## back up original rawDataRepacker and replace rawDataCollector with rawDataRepacker
## If this is not done correctly, then it can happen that the config runs, but never stops.
sed -i "s;rawDataRepacker;rawDataRepackerOrig;g" $configFileFULL
sed -i "s;rawDataCollector;rawDataRepacker;g" $configFileFULL

configFileFULLLOG="${configFileFULL/.py/.log}"
echo "# run the FULL config via"
echo "myRun cmsRun $configFileFULL &> $configFileFULLLOG &"

