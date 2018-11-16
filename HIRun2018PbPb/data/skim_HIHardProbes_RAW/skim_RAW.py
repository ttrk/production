import FWCore.ParameterSet.Config as cms
process = cms.Process('SKIM')

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring ('file:/eos/cms/store/hidata/HIRun2018A/HIHardProbes/RAW/v1/000/326/392/00000/073F2A08-E175-D94E-99B1-49EC9B94CBE9.root'),
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

import HLTrigger.HLTfilters.hltHighLevel_cfi
process.hltFilter = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hltFilter.HLTPaths = ['HLT_HIGEDPhoton40_v*', 'HLT_HIGEDPhoton40_EB_v*', 'HLT_HIIslandPhoton40_Eta2p4_v*', 'HLT_HIIslandPhoton40_Eta1p5_v*']
process.hltFilter.throw = False
process.hltFilter.andOr = True

process.skimHLTSequence = cms.Sequence(
    process.hltFilter
)

process.filterstep = cms.Path(process.skimHLTSequence)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string ("skim_RAW.root"),
    outputCommands = cms.untracked.vstring('keep *'),
    SelectEvents = cms.untracked.PSet(
         SelectEvents = cms.vstring(
             'filterstep')
    ),
)

process.outputstep = cms.EndPath(process.out)
