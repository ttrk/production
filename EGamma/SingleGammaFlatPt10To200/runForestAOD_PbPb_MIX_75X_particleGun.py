### HiForest Configuration
# Collisions: PbPb
# Type: MonteCarlo
# Input: AOD

import FWCore.ParameterSet.Config as cms
process = cms.Process('HiForest')
process.options = cms.untracked.PSet()

#####################################################################################
# HiForest labelling info
#####################################################################################

process.load("HeavyIonsAnalysis.JetAnalysis.HiForest_cff")
process.HiForest.inputLines = cms.vstring("HiForest V3",)
import subprocess
version = subprocess.Popen(["(cd $CMSSW_BASE/src && git describe --tags)"], stdout=subprocess.PIPE, shell=True).stdout.read()
if version == '':
    version = 'no git info'
process.HiForest.HiForestVersion = cms.string(version)

#####################################################################################
# Input source
#####################################################################################

process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                            fileNames = cms.untracked.vstring(
                                "file:/afs/cern.ch/work/k/katatar/public/EGamma/CMSSW_7_5_8_patch3/src/SingleGammaFlatPt10To200/step3_RAW2DIGI_L1Reco_RECO.root"
                                )
                            )

# Number of events we want to process, -1 = all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)


#####################################################################################
# Load Global Tag, Geometry, etc.
#####################################################################################

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '75X_mcRun2_HeavyIon_v13', '') #for now track GT manually, since centrality tables updated ex post facto
process.HiForest.GlobalTagLabel = process.GlobalTag.globaltag

from HeavyIonsAnalysis.Configuration.CommonFunctions_cff import overrideJEC_PbPb5020
process = overrideJEC_PbPb5020(process)

process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
# process.centralityBin.Centrality = cms.InputTag("hiCentrality")
# process.centralityBin.centralityVariable = cms.string("HFtowers")
#process.centralityBin.nonDefaultGlauberModel = cms.string("HydjetDrum5")

#####################################################################################
# Define tree output
#####################################################################################

process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("HiForestAOD.root"))

#####################################################################################
# Additional Reconstruction and Analysis: Main Body
#####################################################################################

####################################################################################

#############################
# Jets
#############################
# full gen jets followed by filters to select signal-only genjets
process.load('HeavyIonsAnalysis.JetAnalysis.GenJetSequence')
process.load('HeavyIonsAnalysis.JetAnalysis.hiSignalGenFilters')


# nominal jet reco sequence
process.load('HeavyIonsAnalysis.JetAnalysis.FullJetSequence_nominalPbPb')
# replace above with this one for JEC:
#process.load('HeavyIonsAnalysis.JetAnalysis.FullJetSequence_JECPbPb')
##### notes on 2016.10.05
# https://github.com/CmsHI/cmssw/blob/forest_CMSSW_7_5_8_patch3/HeavyIonsAnalysis/JetAnalysis/python/FullJetSequence_nominalPbPb.py#L47-L115
# removing some jet sequences to save space. remove VS jets and jets with dR=0.2, 0.5.
# decreases file by size by ~50%
process.jetSequences = cms.Sequence(
    process.voronoiBackgroundPF+
    process.voronoiBackgroundCalo+
    process.kt2PFJets +
    process.kt4PFJets +
    process.hiFJRhoProducer +
    process.hiFJGridEmptyAreaCalculator +

    process.akPu3CaloJets +
    process.akPu3PFJets +
#    process.akVs3CaloJets +
#    process.akVs3PFJets +
    process.akCs3PFJets +

    process.akPu4CaloJets +
    process.akPu4PFJets +
#    process.akVs4CaloJets +
#    process.akVs4PFJets +
    process.akCs4PFJets +

#    process.akPu5CaloJets +
#    process.akPu5PFJets +
#    process.akVs5CaloJets +
#    process.akVs5PFJets +
#    process.akCs5PFJets +

    process.akCsFilter4PFJets +
#    process.akCsFilter5PFJets +
    process.akCsSoftDrop4PFJets +
#    process.akCsSoftDrop5PFJets +

    process.highPurityTracks +
    process.offlinePrimaryVertices +

#    process.akPu2CaloJetSequence +
#    process.akVs2CaloJetSequence +
#    process.akVs2PFJetSequence +
#    process.akPu2PFJetSequence +
#    process.akCs2PFJetSequence +

    process.akPu3CaloJetSequence +
#    process.akVs3CaloJetSequence +
#    process.akVs3PFJetSequence +
    process.akPu3PFJetSequence +
    process.akCs3PFJetSequence +

    process.akPu4CaloJetSequence +
#    process.akVs4CaloJetSequence +
#    process.akVs4PFJetSequence +
    process.akPu4PFJetSequence +
    process.akCs4PFJetSequence +

#    process.akPu5CaloJetSequence +
#    process.akVs5CaloJetSequence +
#    process.akVs5PFJetSequence +
#    process.akPu5PFJetSequence +
#    process.akCs5PFJetSequence +

    process.akCsFilter4PFJetSequence +
#    process.akCsFilter5PFJetSequence +
    process.akCsSoftDrop4PFJetSequence 
#    process.akCsSoftDrop5PFJetSequence
)
##### notes on 2016.10.05 - END

#rho analyzer
process.load('HeavyIonsAnalysis.JetAnalysis.hiFJRhoAnalyzer_cff')

####################################################################################

#############################
# Gen Analyzer
#############################
process.load('HeavyIonsAnalysis.EventAnalysis.HiMixAnalyzerRECO_cff')
process.load('GeneratorInterface.HiGenCommon.HeavyIon_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.HiGenAnalyzer_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.runanalyzer_cff')
process.HiGenParticleAna.genParticleSrc = cms.untracked.InputTag("genParticles")
# Temporary disactivation - until we have DIGI & RECO in CMSSW_7_5_7_patch4
process.HiGenParticleAna.doHI = False


#####################################################################################

############################
# Event Analysis
############################
process.load('HeavyIonsAnalysis.EventAnalysis.hievtanalyzer_mc_cfi')
process.hiEvtAnalyzer.doMC = cms.bool(True) #general MC info
process.hiEvtAnalyzer.doHiMC = cms.bool(True) #HI specific MC info
process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cff')
process.load("HeavyIonsAnalysis.JetAnalysis.pfcandAnalyzer_cfi")
process.pfcandAnalyzer.skipCharged = False
process.pfcandAnalyzer.pfPtMin = 0
process.load("HeavyIonsAnalysis.JetAnalysis.pfcandAnalyzerCS_cfi")
process.pfcandAnalyzerCS.skipCharged = False
process.pfcandAnalyzerCS.pfPtMin = 0

#####################################################################################

#########################
# Track Analyzer
#########################
process.load('HeavyIonsAnalysis.JetAnalysis.ExtraTrackReco_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.TrkAnalyzers_cff')

# Use this instead for track corrections
## process.load('HeavyIonsAnalysis.JetAnalysis.TrkAnalyzers_Corr_cff')

#####################################################################################

#####################
# Photons
#####################

process.load('HeavyIonsAnalysis.PhotonAnalysis.ggHiNtuplizer_cfi')
process.ggHiNtuplizer.runOnParticleGun = cms.bool(True)
process.ggHiNtuplizerGED = process.ggHiNtuplizer.clone(recoPhotonSrc = cms.InputTag('gedPhotonsTmp'),
                                                       recoPhotonHiIsolationMap = cms.InputTag('photonIsolationHIProducerGED')
)

#####################################################################################


#####################
# tupel and necessary PAT sequences
#####################

process.load("HeavyIonsAnalysis.VectorBosonAnalysis.tupelSequence_PbPb_mc_cff")

#####################################################################################

#########################
# Main analysis list
#########################

process.ana_step = cms.Path(
# Temporary disactivation - until we have DIGI & RECO in CMSSW_7_5_7_patch4
# process.mixAnalyzer *
                            process.runAnalyzer *
                            process.hltanalysis *
                            process.centralityBin *
                            process.hiEvtAnalyzer*
                            process.HiGenParticleAna*
                            process.akHiGenJets +
                            process.hiSignalGenFilters + 
                            process.jetSequences +
                            process.hiFJRhoAnalyzer +
                            process.ggHiNtuplizer +
                            process.ggHiNtuplizerGED +
                            process.pfcandAnalyzer +
                            process.pfcandAnalyzerCS +
                            process.HiForest +
                            process.trackSequencesPbPb #+
                            #process.tupelPatSequence
                            )

#####################################################################################

#########################
# Event Selection
#########################

process.load('HeavyIonsAnalysis.JetAnalysis.EventSelection_cff')
process.pcollisionEventSelection = cms.Path(process.collisionEventSelectionAOD)
process.pHBHENoiseFilterResultProducer = cms.Path( process.HBHENoiseFilterResultProducer )
process.HBHENoiseFilterResult = cms.Path(process.fHBHENoiseFilterResult)
process.HBHENoiseFilterResultRun1 = cms.Path(process.fHBHENoiseFilterResultRun1)
process.HBHENoiseFilterResultRun2Loose = cms.Path(process.fHBHENoiseFilterResultRun2Loose)
process.HBHENoiseFilterResultRun2Tight = cms.Path(process.fHBHENoiseFilterResultRun2Tight)
process.HBHEIsoNoiseFilterResult = cms.Path(process.fHBHEIsoNoiseFilterResult)
process.pprimaryVertexFilter = cms.Path(process.primaryVertexFilter )

process.load('HeavyIonsAnalysis.Configuration.hfCoincFilter_cff')
process.phfCoincFilter1 = cms.Path(process.hfCoincFilter)
process.phfCoincFilter2 = cms.Path(process.hfCoincFilter2)
process.phfCoincFilter3 = cms.Path(process.hfCoincFilter3)
process.phfCoincFilter4 = cms.Path(process.hfCoincFilter4)
process.phfCoincFilter5 = cms.Path(process.hfCoincFilter5)

process.pclusterCompatibilityFilter = cms.Path(process.clusterCompatibilityFilter)

process.pAna = cms.EndPath(process.skimanalysis)

# Customization
##########################################UE##########################################
from CondCore.DBCommon.CondDBSetup_cfi import *
process.uetable = cms.ESSource("PoolDBESSource",
      DBParameters = cms.PSet(
        messageLevel = cms.untracked.int32(0)
        ),
      timetype = cms.string('runnumber'),
      toGet = cms.VPSet(
          cms.PSet(record = cms.string("JetCorrectionsRecord"),
                   tag = cms.string("UETableCompatibilityFormat_PF_HYDJET_5020GeV_754_38T_v02_mc"),
                   label = cms.untracked.string("UETable_PF")
          ),
          cms.PSet(record = cms.string("JetCorrectionsRecord"),
                   tag = cms.string("UETableCompatibilityFormat_Calo_HYDJET_5020GeV_754_38T_v02_mc"),
                   label = cms.untracked.string("UETable_Calo")
          )
      ),
      connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
)
process.es_prefer_uetable = cms.ESPrefer('PoolDBESSource','uetable')
##########################################UE##########################################
