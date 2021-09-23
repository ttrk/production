### HiForest Configuration
# Input: miniAOD
# Type: data

import FWCore.ParameterSet.Config as cms
from Configuration.Eras.Era_Run2_2018_pp_on_AA_cff import Run2_2018_pp_on_AA
from Configuration.ProcessModifiers.run2_miniAOD_pp_on_AA_103X_cff import run2_miniAOD_pp_on_AA_103X
process = cms.Process('HiForest', Run2_2018_pp_on_AA,run2_miniAOD_pp_on_AA_103X)

###############################################################################

# HiForest info
process.load("HeavyIonsAnalysis.EventAnalysis.HiForestInfo_cfi")
process.HiForestInfo.info = cms.vstring("HiForest, miniAOD, 112X, data")

# import subprocess, os
# version = subprocess.check_output(
#     ['git', '-C', os.path.expandvars('$CMSSW_BASE/src'), 'describe', '--tags'])
# if version == '':
#     version = 'no git info'
# process.HiForestInfo.HiForestVersion = cms.string(version)

###############################################################################

# input files
process.source = cms.Source("PoolSource",
    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
    fileNames = cms.untracked.vstring(
        "/store/hidata/HIRun2018A/HIHardProbes/MINIAOD/PbPb18_MiniAODv1-v1/00000/034807c1-0ae5-4540-bb81-80ab2f3bc01d.root"
    ),
)
#input file produced from:
#"file:/afs/cern.ch/work/r/rbi/public/forest/HIHardProbes_HIRun2018A-PromptReco-v2_AOD.root"

# number of events to process, set to -1 to process all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(5000)
    )

###############################################################################

# load Global Tag, geometry, etc.
process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')


from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data_promptlike_hi', '')
process.HiForestInfo.GlobalTagLabel = process.GlobalTag.globaltag

centralityTag = "CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run2v1031x02_offline"
process.HiForestInfo.info.append(centralityTag)

print('\n')
print('\033[31m~*~ CENTRALITY TABLE FOR 2018 PBPB DATA ~*~\033[0m')
print('\033[36m~*~ TAG: ' + centralityTag + ' ~*~\033[0m')
print('\n')
process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")
process.GlobalTag.toGet.extend([
    cms.PSet(
        record = cms.string("HeavyIonRcd"),
        tag = cms.string(centralityTag),
        label = cms.untracked.string("HFtowers"),
        connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
        ),
    ])

process.GlobalTag.toGet.extend([
    cms.PSet(
        record = cms.string("BTagTrackProbability3DRcd"),
        tag = cms.string("JPcalib_Data103X_2018PbPb_v1"),
        connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
        )
    ])

###############################################################################

# root output
process.TFileService = cms.Service("TFileService",
    fileName = cms.string("HiForestMiniAOD.root"))

# # edm output for debugging purposes
# process.output = cms.OutputModule(
#     "PoolOutputModule",
#     fileName = cms.untracked.string('HiForestEDM.root'),
#     outputCommands = cms.untracked.vstring(
#         'keep *',
#         )
#     )

# process.output_path = cms.EndPath(process.output)

###############################################################################

# event analysis
process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.hievtanalyzer_data_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.skimanalysis_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.hltobject_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.l1object_cfi')

from HeavyIonsAnalysis.EventAnalysis.hltobject_cfi import trigger_list_data
process.hltobject.triggerNames = trigger_list_data

process.load('HeavyIonsAnalysis.EventAnalysis.particleFlowAnalyser_cfi')
process.particleFlowAnalyser.absEtaMax = cms.double(10.0)
process.particleFlowAnalyser.ptMin = cms.double(0.0)
################################
# electrons, photons, muons
SSHIRun2018A = "HeavyIonsAnalysis/EGMAnalysis/data/SSHIRun2018A.dat"
process.load('HeavyIonsAnalysis.EGMAnalysis.correctedElectronProducer_cfi')
process.correctedElectrons.correctionFile = SSHIRun2018A

process.load('HeavyIonsAnalysis.MuonAnalysis.unpackedMuons_cfi')
process.load('HeavyIonsAnalysis.EGMAnalysis.ggHiNtuplizer_cfi')
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")

process.ggHiNtuplizer.doGenParticles = False
process.ggHiNtuplizer.doEffectiveAreas = cms.bool(True)
process.ggHiNtuplizer.doRecHitsEB = cms.bool(True)
process.ggHiNtuplizer.doRecHitsEE = cms.bool(True)
process.ggHiNtuplizer.recHitsEB = cms.untracked.InputTag("reducedEgamma","reducedEBRecHits")
process.ggHiNtuplizer.recHitsEE = cms.untracked.InputTag("reducedEgamma","reducedEERecHits")
process.ggHiNtuplizer.doPhoERegression = cms.bool(True)
process.ggHiNtuplizer.doSuperClusters = cms.bool(True)
process.ggHiNtuplizer.electronSrc = "correctedElectrons"

################################
# jet reco sequence
process.load('HeavyIonsAnalysis.JetAnalysis.akCs4PFJetSequence_pponPbPb_data_cff')
################################
# tracks
process.load("HeavyIonsAnalysis.TrackAnalysis.TrackAnalyzers_cff")
###############################################################################



###############################################################################
# main forest sequence
process.forest = cms.Path(
    process.HiForestInfo +
    process.hltanalysis +
    process.hltobject +
    process.l1object +
    process.trackSequencePbPb +
    process.particleFlowAnalyser +
    process.hiEvtAnalyzer +
    process.unpackedMuons +
    process.correctedElectrons +
    process.ggHiNtuplizer +
    process.akCs4PFJetAnalyzer
    )

#customisation

addR3Jets = False

if addR3Jets :
    process.load("HeavyIonsAnalysis.JetAnalysis.extraJets_cff")
    from HeavyIonsAnalysis.JetAnalysis.clusterJetsFromMiniAOD_cff import setupHeavyIonJets
    setupHeavyIonJets('akCs3PF', process.extraJetsData, process, 0)
    process.akCs3PFpatJetCorrFactors.levels = ['L2Relative','L2L3Residual']
    process.akCs3PFJetAnalyzer = process.akCs4PFJetAnalyzer.clone(
        jetTag = "akCs3PFpatJets",
    )

    process.forest += process.extraJetsData * process.akCs3PFJetAnalyzer




addCandidateTagging = True

if addCandidateTagging:
    process.load("HeavyIonsAnalysis.JetAnalysis.candidateBtaggingMiniAOD_cff")

    from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection
    updateJetCollection(
        process,
        jetSource = cms.InputTag('slimmedJets'),
        jetCorrections = ('AK4PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'None'),
        btagDiscriminators = ['pfCombinedSecondaryVertexV2BJetTags', 'pfDeepCSVDiscriminatorsJetTags:BvsAll', 'pfDeepCSVDiscriminatorsJetTags:CvsB', 'pfDeepCSVDiscriminatorsJetTags:CvsL'], ## to add discriminators,
        btagPrefix = 'TEST',
    )

    process.updatedPatJets.addJetCorrFactors = False
    process.updatedPatJets.discriminatorSources = cms.VInputTag(
        cms.InputTag('pfDeepCSVJetTags:probb'),
        cms.InputTag('pfDeepCSVJetTags:probc'),
        cms.InputTag('pfDeepCSVJetTags:probudsg'),
        cms.InputTag('pfDeepCSVJetTags:probbb'),
    )

    process.akCs4PFJetAnalyzer.jetTag = "updatedPatJets"

    process.forest.insert(1,process.candidateBtagging*process.updatedPatJets)

    process.akCs4PFJetAnalyzer.addDeepCSV = True

#########################
# Event Selection -> add the needed filters here
#########################

process.load('HeavyIonsAnalysis.EventAnalysis.collisionEventSelection_cff')
process.pclusterCompatibilityFilter = cms.Path(process.clusterCompatibilityFilter)
process.pprimaryVertexFilter = cms.Path(process.primaryVertexFilter)
process.load('HeavyIonsAnalysis.EventAnalysis.hffilter_cfi')
process.pphfCoincFilter2Th4 = cms.Path(process.phfCoincFilter2Th4)
process.pAna = cms.EndPath(process.skimanalysis)

# Customization
## KT : Attempt to add event plane info
#process.hiEvtPlane.caloTag = cms.InputTag("packedPFCandidates")
# hiEvtPlane Plane worflow currently fails due to
##   [2] Calling method for module EvtPlaneProducer/'hiEvtPlane'
##Exception Message:
##Principal::getByToken: Found zero products matching all criteria
##Looking for type: edm::SortedCollection<CaloTower,edm::StrictWeakOrdering<CaloTower> >
##Looking for module label: packedPFCandidates
##Looking for productInstanceName
## KT : Attempt to add event plane info - END

## KT : filter events on dielectrons
process.dielectronFilter = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("slimmedElectrons"),
#    ptMin = cms.double(8.0),
    minNumber = cms.uint32(2)
)

process.electronSelector = cms.EDFilter("CandPtrSelector",
                                src = cms.InputTag("slimmedElectrons"),
                                cut = cms.string('pt > 8.0'),
                                filter = cms.bool(True)                                
)

process.dielectronCand = cms.EDProducer("CandViewShallowCloneCombiner",
    checkCharge = cms.bool(False),
    cut = cms.string('40 < mass < 140'),
    decay = cms.string("electronSelector electronSelector")
)

process.dielectronCandFilter = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("dielectronCand"),
    minNumber = cms.uint32(1)
)

process.filterSequence = cms.Sequence(
#    process.dielectronFilter *
    process.electronSelector *
    process.dielectronCand *
    process.dielectronCandFilter
)

process.superFilterPath = cms.Path(process.filterSequence)
process.skimanalysis.superFilters = cms.vstring("superFilterPath")

##filter all path with the production filter sequence
for path in process.paths:
  getattr(process,path)._seq = process.filterSequence * getattr(process,path)._seq
## KT : filter events on dielectrons - END
