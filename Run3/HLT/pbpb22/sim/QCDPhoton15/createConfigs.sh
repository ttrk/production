#!/bin/bash

### instructions : https://twiki.cern.ch/twiki/bin/view/CMS/HLT_HIon_Run3?rev=9#CMSSW_12_4_X
### software : CMSSW_12_4_8
## software and environment setup
#cmsrel CMSSW_12_4_8
#cd CMSSW_12_4_8/src
#cmsenv
## For HLT analyzers
#git cms-addpkg HLTrigger/Configuration
#git cms-addpkg L1Trigger/L1TGlobal
#mkdir -p L1Trigger/L1TGlobal/data/Luminosity/startup/ && cd L1Trigger/L1TGlobal/data/Luminosity/startup/
#wget https://raw.githubusercontent.com/mitaylor/HIMenus/main/Menus/L1Menu_CollisionsHeavyIons2022_v0_0_0.xml
#cd $CMSSW_BASE/src
#git cms-merge-topic denerslemos:HLTBitAna_CMSSW_12_4_X
## Build
#scram b -j 8
#cd HLTrigger/Configuration/test && mkdir workstation && cd workstation

#### merge setup with the L1T emulation
### L1T instructions : https://twiki.cern.ch/twiki/bin/view/CMS/L1HITaskForce2022?rev=83#Instructions_to_run_the_L1Emulat
#git remote add cms-l1t-offline git@github.com:cms-l1t-offline/cmssw.git
#git fetch cms-l1t-offline l1t-integration-CMSSW_12_4_0
#git cms-merge-topic -u cms-l1t-offline:l1t-integration-v134
#git clone https://github.com/cms-l1t-offline/L1Trigger-L1TCalorimeter.git L1Trigger/L1TCalorimeter/data
#git cms-merge-topic -u kakwok:CLCT_thresholds

runCmd="/afs/cern.ch/user/k/katatar/code/scripts/myRun.sh"
# This script is based on its ancestor : https://github.com/ttrk/production/blob/master/HIRun2018PbPb/HLT/Pythia8_AllQCDPhoton15_Hydjet_Quenched_Cymbal5Ev8/createConfigs.sh
####

MENU="/users/katatar/run3/pbpb22/hltTest/dev_HIon/V1" # release cmssw_12_4_0
#MENU="/users/katatar/run3/pbpb22/hltTest/cmssw_12_3_0_HIon/V8"
# V1 : copy of /dev/CMSSW_12_3_0/HIon/V84
# V2 : clean-up of unnecessary/unrelated paths
# V3 : remove UPC Muon and Castor paths
## failure when saving some intermediate versions
# V8 : GEDPhoton30 and 40 w/o L1 EG seed, seeded by L1 ZeroBias actually
configFile="hltConfig.py"
GLOBALTAG="auto:phase1_2022_realistic_hi"
PROCESS="MyHLT"
nEvents="20"
DATAMC="--mc"
# pick up customization for L1 Calo as shown in https://twiki.cern.ch/twiki/bin/view/CMS/L1HITaskForce2022?rev=55#Instructions_to_run_the_L1Emulat
## this is necessary to run L1 EGs with correct parameters
#CUSTOMISE="--customise L1Trigger/Configuration/customiseSettings.L1TSettingsToCaloParamsHI_2022_v0_4_1" # not available in code
CUSTOMISE="--customise L1Trigger/Configuration/customiseSettings.L1TSettingsToCaloParamsHI_2022_v0_4"
L1EMU="FullMC"  # "uGT"
ERA="Run3" # "Run3_pp_on_PbPb"
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

# where L1 EG Spike Killer is activated :
# https://github.com/cms-sw/cmssw/blob/master/SimCalorimetry/EcalTrigPrimAlgos/src/EcalFenixTcpFormat.cc#L72-L75
# https://github.com/cms-sw/cmssw/blob/edb9f982c877bb0c568704d3383ede9ea099ec3a/SimCalorimetry/EcalTrigPrimAlgos/src/EcalFenixTcpFormat.cc#L72-L75
# change Spike Killer WP
# WP 12_12 : EcalTPGFineGrainStrip_12, EcalTPGSpike_12
# WP 12_7  : EcalTPGFineGrainStrip_7 , EcalTPGSpike_12
# WP 16_16 : EcalTPGFineGrainStrip_16, EcalTPGSpike_16
mod_ECAL_SK=1 # set to 1 in order to modify the spike killer parameters
TPG_FG=7
TPG_Spike=12

if [ ${mod_ECAL_SK} -gt 0 ]; then

  echo "" >> ${configFile}
  echo "process.simEcalTriggerPrimitiveDigis = cms.EDProducer('EcalTrigPrimProducer', BarrelOnly = cms.bool(False), Debug = cms.bool(False), Famos = cms.bool(False), InstanceEB = cms.string('ebDigis'), InstanceEE = cms.string('eeDigis'), Label = cms.string('unpackEcal'), TcpOutput = cms.bool(False), binOfMaximum = cms.int32(6))" >> ${configFile}
  echo "" >> ${configFile}
  echo "process.simCaloStage2Layer1Digis.ecalToken = cms.InputTag('simEcalTriggerPrimitiveDigis')" >> ${configFile}
  echo "" >> ${configFile}
  echo "process.SimL1TGlobal = cms.Sequence(process.SimL1TGlobalTask)" >> ${configFile} # need to redefine SimL1TGlobal, originally defined in https://cmssdt.cern.ch/lxr/source/L1Trigger/L1TGlobal/python/simDigis_cff.py#0026
  # otherwise one gets AttributeError: 'Process' object has no attribute 'SimL1TGlobal'
  echo "process.SimL1Emulator = cms.Sequence(process.unpackRPC+process.unpackDT+process.unpackCSC+process.unpackEcal+process.unpackHcal+process.simHcalTriggerPrimitiveDigis+process.simEcalTriggerPrimitiveDigis+((process.simCaloStage2Layer1Digis+process.simCaloStage2Digis)+((process.simDtTriggerPrimitiveDigis+process.simCscTriggerPrimitiveDigis)+process.simTwinMuxDigis+process.simBmtfDigis+process.simEmtfDigis+process.simOmtfDigis+process.simGmtCaloSumDigis+process.simGmtStage2Digis)+(process.simGtExtFakeStage2Digis)+process.SimL1TGlobal)+process.packCaloStage2+process.packGmtStage2+process.packGtStage2+process.rawDataCollector)" >> ${configFile}

  echo "
process.GlobalTag.toGet = cms.VPSet(
    cms.PSet(record = cms.string('EcalTPGFineGrainStripEERcd'),
             tag = cms.string('EcalTPGFineGrainStrip_"${TPG_FG}"'),
             connect =cms.string('frontier://FrontierProd/CMS_CONDITIONS')
                                                                 ),

    cms.PSet(record = cms.string('EcalTPGSpikeRcd'),
             tag = cms.string('EcalTPGSpike_"${TPG_Spike}"'),
             connect =cms.string('frontier://FrontierProd/CMS_CONDITIONS')
                                                                 )
    )" >> ${configFile}
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

