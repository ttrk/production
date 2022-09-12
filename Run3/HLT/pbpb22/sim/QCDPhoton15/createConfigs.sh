#!/bin/bash

### instructions : https://twiki.cern.ch/twiki/bin/view/CMS/HIRunPreparations2021HLT?rev=83#HLT_trees_CMSSW_12_3_X_Version_w
### software : CMSSW_12_3_0
## software and environment setup
#cmsrel CMSSW_12_3_0
#cd CMSSW_12_3_0/src
#cmsenv
## For HLT analyzers
#git cms-addpkg HLTrigger/Configuration
#git cms-addpkg L1Trigger/L1TGlobal
#mkdir -p L1Trigger/L1TGlobal/data/Luminosity/startup/ && cd L1Trigger/L1TGlobal/data/Luminosity/startup/
#wget https://raw.githubusercontent.com/mitaylor/HIMenus/main/Menus/L1Menu_CollisionsHeavyIons2022_v0_0_0.xml
#cd $CMSSW_BASE/src
#git cms-merge-topic denerslemos:HLTBitAna_CMSSW_12_3_X
## Build
#scram b -j 8
#cd HLTrigger/Configuration/test && mkdir workstation && cd workstation

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"
# This script is based on its ancestor : https://github.com/ttrk/production/blob/master/HIRun2018PbPb/HLT/Pythia8_AllQCDPhoton15_Hydjet_Quenched_Cymbal5Ev8/createConfigs.sh
####

MENU="/users/katatar/run3/pbpb22/hltTest/cmssw_12_3_0_HIon/V5"
# V1 : copy of /dev/CMSSW_12_3_0/HIon/V84
# V2 : clean-up of unnecessary/unrelated paths
# V3 : remove UPC Muon and Castor paths
# V5 : add version of GEDPhoton40 w/o L1 EG seed, seeded by L1 ZeroBias actually
configFile="hltConfig.py"
GLOBALTAG="auto:phase1_2021_realistic_hi"
SETUP="/dev/CMSSW_10_3_0/GRun"
PROCESS="MyHLT"
nEvents="20"
DATAMC="--mc"
# pick up customization for L1 Calo as shown in https://twiki.cern.ch/twiki/bin/view/CMS/L1HITaskForce2022?rev=55#Instructions_to_run_the_L1Emulat
## this is necessary to run L1 EGs with correct parameters
CUSTOMISE="--customise L1Trigger/Configuration/customiseSettings.L1TSettingsToCaloParams_2018_v1_4_1"
L1EMU="FullMC"  # "uGT"
ERA="Run3_pp_on_PbPb"
L1XML="L1Menu_CollisionsHeavyIons2022_v0_0_0.xml"
inputFile="/store/user/mnguyen/Run3MC/QCDPhoton_pThat15_Run3_HydjetEmbedded/QCDPhoton_pThat15_Run3_HydjetEmbedded_DIGI/220301_130050/0001/step2_DIGI_L1_DIGI2RAW_HLT_PU_1293.root"
#inputFile="file:/eos/cms/store/group/phys_heavyions_ops/katatar/EWJTA-out/event/run3/pbpb22/sp22/edmCPM_QCDPhoton_pThat15_Run3_HydjetEmbedded_DIGI.root"

hltGetConfiguration ${MENU} --globaltag ${GLOBALTAG} --l1Xml ${L1XML} --l1-emulator ${L1EMU} --era ${ERA} --input ${inputFile} --process ${PROCESS} --full ${DATAMC} ${CUSTOMISE} --unprescale --no-output --max-events ${nEvents} > ${configFile}
# --l1-emulator Full : runs full L1 emulator, avoids L1 prescales

outputEDMEvent=0
if [ ${outputEDMEvent} -gt 0 ]; then
  echo '
# Define the output
process.output = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring("drop *", "keep *_TriggerResults_*_*", "keep *_hltTriggerSummaryAOD_*_*", "keep *_hltGtStage2Digis_*_*", "keep *_hltGtStage2ObjectMap_*_*"),
    fileName = cms.untracked.string("output.root"),
)
process.output_path = cms.EndPath(process.output)
process.schedule.append( process.output_path )  # enable this line if you want to get an output containing trigger info to be used for further analysis, e.g. "TriggerResults", digis etc
' >> ${configFile}
fi

echo 'process.options.numberOfThreads=cms.untracked.uint32(1)' >> $configFile

removeDQM=1
if [ ${removeDQM} -gt 0 ]; then
  #process.DQMOutput = cms.FinalPath( process.dqmOutput )
  #process.schedule.append( process.DQMOutput )

  sed -i -e "s/process.DQMOutput = cms.FinalPath( process.dqmOutput )/#process.DQMOutput = cms.FinalPath( process.dqmOutput )/g" $configFile
  sed -i -e "s/process.schedule.append( process.DQMOutput )/#process.schedule.append( process.DQMOutput )/g" $configFile
fi

removeCustomHLTLines=1
if [ ${removeCustomHLTLines} -gt 0 ]; then
  ### Line removal ###
  ##open ExportedMenu.py and remove/comment the following lines. See TriggerDevelopmentWithGPUs
  #_customInfo = {}
  #_customInfo['menuType'  ]= "GRun"
  #_customInfo['globalTags']= {}
  #_customInfo['globalTags'][True ] = "auto:run3_hlt_GRun"
  #_customInfo['globalTags'][False] = "auto:run3_mc_GRun"
  #_customInfo['inputFiles']={}
  #_customInfo['inputFiles'][True]  = "file:RelVal_Raw_GRun_DATA.root"
  #_customInfo['inputFiles'][False] = "file:RelVal_Raw_GRun_MC.root"
  #_customInfo['maxEvents' ]=  -1
  #_customInfo['globalTag' ]= "auto:phase1_2021_realistic_hi"
  #_customInfo['inputFile' ]=  ['root://cmsxrootd.fnal.gov//store/user/mnguyen/Run3MC/QCDPhoton_pThat15_Run3_HydjetEmbedded/QCDPhoton_pThat15_Run3_HydjetEmbedded_DIGI/211126_120712/0000/step2_DIGI_L1_DIGI2RAW_HLT_PU_177.root']
  #_customInfo['realData'  ]=  True
  #from HLTrigger.Configuration.customizeHLTforALL import customizeHLTforAll
  #process = customizeHLTforAll(process,"GRun",_customInfo)

  lineToRemove="_customInfo"
  sed -i -e "s/"${lineToRemove}"/#"${lineToRemove}"/g" $configFile
  #lineRemove="process = customizeHLTforAll(process"
  sed -i -e "s/process = customizeHLTforAll(process/#process = customizeHLTforAll(process/g" $configFile
  ### Line removal - END ###
fi

addHLTObjs=1
if [ ${addHLTObjs} -gt 0 ]; then
  # Add hltBitAnalyzer and HLT objects
  echo '
#import FWCore.ParameterSet.Config as cms
#process = cms.Process("HLTANA")

# Input source
#process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
#process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring("file:output.root"))

#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, "auto:run2_hlt_relval", "")

# add HLTBitAnalyzer
process.load("HeavyIonsAnalysis.EventAnalysis.hltanalysis_cfi")
process.hltanalysis.hltResults = cms.InputTag("TriggerResults::'${PROCESS}'")
process.hltanalysis.l1tAlgBlkInputTag = cms.InputTag("hltGtStage2Digis::'${PROCESS}'")
process.hltanalysis.l1tExtBlkInputTag = cms.InputTag("hltGtStage2Digis::'${PROCESS}'")

process.load("HeavyIonsAnalysis.EventAnalysis.hltobject_cfi")
process.hltobject.triggerResults = cms.InputTag("TriggerResults::'${PROCESS}'")
process.hltobject.triggerEvent = cms.InputTag("hltTriggerSummaryAOD::'${PROCESS}'")

process.hltAnalysis = cms.EndPath(process.hltanalysis + process.hltobject)
process.schedule.append( process.hltAnalysis ) # need this command to actually run the new processes
process.TFileService = cms.Service("TFileService", fileName=cms.string("openHLT.root"))
' >> $configFile
fi

#### Add hltobject
###echo 'process.load("HeavyIonsAnalysis.EventAnalysis.hltobject_PbPb_cfi")' >> $configFile
###echo 'process.hltobject.processName = cms.string("'${PROCESS}'")' >> $configFile
###echo 'process.hltobject.triggerResults = cms.InputTag("TriggerResults", "", "'${PROCESS}'")' >> $configFile
###echo 'process.hltobject.triggerEvent = cms.InputTag("hltTriggerSummaryAOD", "", "'${PROCESS}'")' >> $configFile
###echo 'process.hltobject.triggerNames = cms.vstring(
###"HLT_HIGEDPhoton40",
###"HLT_HIGEDPhoton40_EB",
###)'>> $configFile
###echo 'process.hltObject = cms.EndPath(process.hltobject)' >> $configFile

configFileLOG="${configFile/.py/.log}"
echo "# run the config via"
echo "myRun cmsRun $configFile &> $configFileLOG &"

## dump the full config
configFileFULL="${configFile/.py/_FULL.py}"
edmConfigDump $configFile > $configFileFULL
echo "# Full config is also created : $configFileFULL"

cp $configFileFULL "${configFileFULL/.py/.BACKUP.py}"

configFileFULLLOG="${configFileFULL/.py/.log}"
echo "# run the FULL config via"
echo "myRun cmsRun $configFileFULL &> $configFileFULLLOG &"

