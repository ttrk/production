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
                                "root://cms-xrd-global.cern.ch//store/user/katatar/EGamma/Pythia8_AllQCDPhoton30_Hydjet_Cymbal_MB/HiFall15-75X_mcRun2_HeavyIon_v14-v1_RAW2DIGI_L1Reco_RECO_extendEC_pfSC_phiWidth0p20/170902_003418/0000/step3_RAW2DIGI_L1Reco_RECO_extendEC_pfSC_phiWidth0p20_1.root"
#                                "file:samples/PbPb_MC_RECODEBUG.root"
                                )
                            )

# Number of events we want to process, -1 = all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

process.output = cms.OutputModule("PoolOutputModule",
                                  outputCommands = cms.untracked.vstring('drop *',
                                                                         'keep *_particleFlow_*_*',
                                                                         'keep *_particleFlowTmp_*_*',
                                                                         'keep *_mapEtaEdges_*_*',
                                                                         'keep *_*_*_HiForest'),
                                  fileName       = cms.untracked.string ("OutputMC.root")
)
#process.outpath  = cms.EndPath(process.output)

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

#overwrite GT for centrality table for Cymbal5Ev8 tune
process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")
process.GlobalTag.toGet.extend([
   cms.PSet(record = cms.string("HeavyIonRcd"),
      tag = cms.string("CentralityTable_HFtowers200_HydjetCymbal5Ev8_v758x01_mc"),
      connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
      label = cms.untracked.string("HFtowersHydjetCymbal5Ev8")
   ),
])

from HeavyIonsAnalysis.Configuration.CommonFunctions_cff import overrideJEC_PbPb5020
process = overrideJEC_PbPb5020(process)

process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
process.centralityBin.Centrality = cms.InputTag("hiCentrality")
process.centralityBin.centralityVariable = cms.string("HFtowers")
process.centralityBin.nonDefaultGlauberModel = cms.string("HydjetCymbal5Ev8")
#process.centralityBin.nonDefaultGlauberModel = cms.string("HydjetDrum5")

#####################################################################################
# Define tree output
#####################################################################################

process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("HiForestAOD_ggHi_doRecHits.root"))

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


#PU minimal tower cut reco sequence
process.load('HeavyIonsAnalysis.JetAnalysis.FullJetSequence_puLimitedPbPb')
# nominal jet reco sequence
#process.load('HeavyIonsAnalysis.JetAnalysis.FullJetSequence_nominalPbPb')
# replace above with this one for JEC:
#process.load('HeavyIonsAnalysis.JetAnalysis.FullJetSequence_JECPbPb')

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
# KT - START
# change gen particle pt and eta cuts : 5 -> 0.75, 2 -> 2.5
process.HiGenParticleAna.ptMin = cms.untracked.double(0.75)
process.HiGenParticleAna.etaMax = cms.untracked.double(2.5)
# KT - END

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
process.ggHiNtuplizer.doRecHitsEB = cms.bool(True)
process.ggHiNtuplizer.doRecHitsEE = cms.bool(True)
process.ggHiNtuplizer.recHitsEB = cms.untracked.InputTag("ecalRecHit","EcalRecHitsEB")
process.ggHiNtuplizer.recHitsEE = cms.untracked.InputTag("ecalRecHit","EcalRecHitsEE")
process.ggHiNtuplizerGED = process.ggHiNtuplizer.clone(recoPhotonSrc = cms.InputTag('gedPhotonsTmp'),
                                                       recoPhotonHiIsolationMap = cms.InputTag('photonIsolationHIProducerGED')
)

#####################################################################################


#####################
# tupel and necessary PAT sequences
#####################

process.load("HeavyIonsAnalysis.VectorBosonAnalysis.tupelSequence_PbPb_mc_cff")

#####################################################################################

#replace pp CSVv2 with PbPb CSVv2 (positive and negative taggers unchanged!)
process.load('RecoBTag.CSVscikit.csvscikitTagJetTags_cfi')
process.load('RecoBTag.CSVscikit.csvscikitTaggerProducer_cfi')
process.akPu4PFCombinedSecondaryVertexV2BJetTags = process.pfCSVscikitJetTags.clone()
process.akPu4PFCombinedSecondaryVertexV2BJetTags.tagInfos=cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"), cms.InputTag("akPu4PFSecondaryVertexTagInfos"))

process.akCs4PFCombinedSecondaryVertexV2BJetTags = process.pfCSVscikitJetTags.clone()
process.akCs4PFCombinedSecondaryVertexV2BJetTags.tagInfos=cms.VInputTag(cms.InputTag("akCs4PFImpactParameterTagInfos"), cms.InputTag("akCs4PFSecondaryVertexTagInfos"))

process.akPu4CaloCombinedSecondaryVertexV2BJetTags = process.pfCSVscikitJetTags.clone()
process.akPu4CaloCombinedSecondaryVertexV2BJetTags.tagInfos=cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"), cms.InputTag("akPu4CaloSecondaryVertexTagInfos"))
#process.CSVscikitTags.weightFile=cms.FileInPath('HeavyIonsAnalysis/JetAnalysis/data/bTagCSVv2PbPb_758p3_Jan2017_BDTG_weights.xml')
#trained on CS jets
process.CSVscikitTags.weightFile=cms.FileInPath('HeavyIonsAnalysis/JetAnalysis/data/TMVA_Btag_CsJets_PbPb_BDTG.weights.xml')

# KT - START
#####################
# Rechit analyzer
#####################
process.load('HeavyIonsAnalysis.JetAnalysis.rechitanalyzer_cfi')
process.rechitanalyzer.doEcal = cms.untracked.bool(True)
process.rechitanalyzer.doHcal = cms.untracked.bool(False)
process.rechitanalyzer.doHF = cms.untracked.bool(False)
process.rechitanalyzer.doTowers = cms.untracked.bool(True)
process.rechitanalyzer.doBasicClusters = cms.untracked.bool(True)
process.rechitanalyzer.BasicClusterSrc1 = cms.untracked.InputTag("islandBasicClusters","islandBarrelBasicClusters")
process.rechitanalyzer.HBHETreePtMin = cms.untracked.double(0.5)
process.rechitanalyzer.HFTreePtMin = cms.untracked.double(0.5)
process.rechitanalyzer.EBTreePtMin = cms.untracked.double(0.5)
process.rechitanalyzer.EETreePtMin = cms.untracked.double(0.5)
process.rechitanalyzer.doCASTOR = cms.untracked.bool(False)
process.rechitanalyzer.doZDCRecHit = cms.untracked.bool(False)
process.rechitanalyzer.doZDCDigi = cms.untracked.bool(False)
process.rechitanalyzer.doVS = cms.untracked.bool(False)
#process.rechitanalyzerBCEE = process.rechitanalyzer.clone()
#process.rechitanalyzerBCEE.doVS = cms.untracked.bool(False)
#process.rechitanalyzerBCEE.doEcal = cms.untracked.bool(False)
#process.rechitanalyzerBCEE.doHcal = cms.untracked.bool(False)
#process.rechitanalyzerBCEE.doHF = cms.untracked.bool(False)
#process.rechitanalyzerBCEE.doTowers = cms.untracked.bool(False)
#process.rechitanalyzerBCEE.doBasicClusters = cms.untracked.bool(True)
#process.rechitanalyzerBCEE.BasicClusterSrc1 = cms.untracked.InputTag("islandBasicClusters","islandEndcapBasicClusters")
# KT - END

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
                            process.ak2GenNjettiness +
                            process.ak3GenNjettiness +
                            process.ak4GenNjettiness +
                            process.ak5GenNjettiness *
                            process.jetSequences +
                            process.hiFJRhoAnalyzer +
                            process.ggHiNtuplizer +
                            process.ggHiNtuplizerGED +
                            process.pfcandAnalyzer +
                            process.pfcandAnalyzerCS +
                            process.HiForest +
                            process.trackSequencesPbPb +
                            process.rechitanalyzer
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
