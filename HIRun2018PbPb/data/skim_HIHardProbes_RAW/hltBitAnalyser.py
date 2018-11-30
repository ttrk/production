import FWCore.ParameterSet.Config as cms
process = cms.Process('MyHLT')

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring ('file:skim_RAW.root'),
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(500) )

process.GlobalTag.toGet = cms.VPSet(cms.PSet(record = cms.string('L1TUtmTriggerMenuRcd'), tag = cms.string('L1Menu_CollisionsHeavyIons2018_v4_0_0-d1_xml'), connect =cms.string('frontier://FrontierProd/CMS_CONDITIONS')), cms.PSet(record = cms.string('L1TGlobalPrescalesVetosRcd'), tag = cms.string('L1TGlobalPrescalesVetos_Stage2v0_hlt'), connect =cms.string('frontier://FrontierProd/CMS_CONDITIONS')))

#process.L1TriggerMenu = cms.ESProducer("L1TUtmTriggerMenuESProducer",
#    L1TriggerMenuFile = cms.string('L1Menu_CollisionsHeavyIons2018_v4.xml')
#)
#process.prefer("L1TriggerMenu")
#process.pathL1TriggerMenu = cms.Path(process.L1TriggerMenu)

process.hltGtStage2Digis = cms.EDProducer("L1TRawToDigi",
    CTP7 = cms.untracked.bool(False),
    DmxFWId = cms.uint32(0),
    FWId = cms.uint32(0),
    FWOverride = cms.bool(False),
    FedIds = cms.vint32(1404),
    InputLabel = cms.InputTag("rawDataRepacker"),
    MTF7 = cms.untracked.bool(False),
    MinFeds = cms.uint32(0),
    Setup = cms.string('stage2::GTSetup'),
    TMTCheck = cms.bool(True),
    debug = cms.untracked.bool(False),
    lenAMC13Header = cms.untracked.int32(8),
    lenAMC13Trailer = cms.untracked.int32(8),
    lenAMCHeader = cms.untracked.int32(8),
    lenAMCTrailer = cms.untracked.int32(0),
    lenSlinkHeader = cms.untracked.int32(8),
    lenSlinkTrailer = cms.untracked.int32(8)
)
#process.HLTSchedule = cms.Schedule( process.hltGtStage2Digis )

process.load("HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi")
process.hltbitanalysis.HLTProcessName = cms.string("HLT")
process.hltbitanalysis.l1GtObjectMapRecord = cms.InputTag("hltGtStage2ObjectMap::HLT")
process.hltbitanalysis.hltresults = cms.InputTag("TriggerResults", "", "HLT")
process.hltbitanalysis.l1results = cms.InputTag("hltGtStage2Digis")
process.hltbitanalysis.UseTFileService = cms.untracked.bool(True)
process.hltbitanalysis.RunParameters = cms.PSet(isData = cms.untracked.bool(True))
process.hltBitAnalysis = cms.EndPath(process.hltGtStage2Digis+process.hltbitanalysis)
process.TFileService = cms.Service("TFileService", fileName=cms.string("openHLT.root"))
