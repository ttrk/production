import FWCore.ParameterSet.Config as cms
process = cms.Process('SKIM')

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring ('file:C88B56BC-ED91-E511-BA84-02163E01423E.root'),
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.muonSelectorForZMM = cms.EDFilter("MuonSelector",
    src = cms.InputTag("muons"),
    cut = cms.string("(isTrackerMuon && isGlobalMuon) && pt > 8."),
    filter = cms.bool(True)
    )

process.muonFilterForZMM = cms.EDFilter("MuonCountFilter",
    src = cms.InputTag("muonSelectorForZMM"),
    minNumber = cms.uint32(2)
    )

process.dimuonMassCutForZMM = cms.EDProducer("CandViewShallowCloneCombiner",
    checkCharge = cms.bool(False),
    cut = cms.string(' 40 < mass '),
    decay = cms.string("muonSelectorForZMM@+ muonSelectorForZMM@-")
    )

process.dimuonMassCutFilterForZMM = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("dimuonMassCutForZMM"),
    minNumber = cms.uint32(1)
    )

process.zMMSkimSequence = cms.Sequence(
    process.muonSelectorForZMM *
    process.muonFilterForZMM *
    process.dimuonMassCutForZMM *
    process.dimuonMassCutFilterForZMM
    )

process.filterstep = cms.Path(process.zMMSkimSequence)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string ("dimuon_skim.root"),
    outputCommands = cms.untracked.vstring('keep *'),
    SelectEvents = cms.untracked.PSet(
         SelectEvents = cms.vstring(
             'filterstep')
    ),
)

process.outputstep = cms.EndPath(process.out)

# derived from : https://github.com/azsigmon/UserCode/blob/b895cad63f142ea452220cf6202aefe0703742b0/skim_dimuon_mass_40_AOD.py
