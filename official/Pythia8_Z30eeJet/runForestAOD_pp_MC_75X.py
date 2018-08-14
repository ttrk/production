### HiForest Configuration
# Collisions: pp
# Type: MC
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
                                "/store/himc/HINppWinter16DR/Pythia8_Ze10e10/AODSIM/75X_mcRun2_asymptotic_ppAt5TeV_v3_ext1-v1/70000/E250857A-300F-E611-A82A-0090FAA57CB4.root"
                            )
)

# Number of events we want to process, -1 = all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100))


#####################################################################################
# Load Global Tag, Geometry, etc.
#####################################################################################

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '75X_mcRun2_asymptotic_ppAt5TeV_v3', '')
process.HiForest.GlobalTagLabel = process.GlobalTag.globaltag


# Customization
from HeavyIonsAnalysis.Configuration.CommonFunctions_cff import overrideJEC_pp5020
process = overrideJEC_pp5020(process)

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

process.load("HeavyIonsAnalysis.JetAnalysis.FullJetSequence_nominalPP")

# Include this to turn on storing the jet constituents and new jet variables for q/g separation
#process.ak4PFJetAnalyzer.doJetConstituents = cms.untracked.bool(True)
#process.ak4PFJetAnalyzer.doNewJetVars = cms.untracked.bool(True)
# Use this version for JEC
#process.load("HeavyIonsAnalysis.JetAnalysis.FullJetSequence_JECPP")

#####################################################################################

############################
# Event Analysis
############################
process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cff')
process.load('HeavyIonsAnalysis.EventAnalysis.hltobject_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.hievtanalyzer_data_cfi') #use data version to avoid PbPb MC
process.hiEvtAnalyzer.Vertex = cms.InputTag("offlinePrimaryVertices")
process.hiEvtAnalyzer.doCentrality = cms.bool(False)
process.hiEvtAnalyzer.doEvtPlane = cms.bool(False)
process.hiEvtAnalyzer.doMC = cms.bool(True) #general MC info
process.hiEvtAnalyzer.doHiMC = cms.bool(False) #HI specific MC info

process.load('HeavyIonsAnalysis.JetAnalysis.HiGenAnalyzer_cfi')
process.HiGenParticleAna.genParticleSrc = cms.untracked.InputTag("genParticles")
process.HiGenParticleAna.doHI = False
process.load('HeavyIonsAnalysis.EventAnalysis.runanalyzer_cff')
process.load("HeavyIonsAnalysis.JetAnalysis.pfcandAnalyzer_pp_cfi")
process.pfcandAnalyzer.skipCharged = False
process.pfcandAnalyzer.pfPtMin = 0
process.pfcandAnalyzer.pfCandidateLabel = cms.InputTag("particleFlow")
process.pfcandAnalyzer.doVS = cms.untracked.bool(False)
process.pfcandAnalyzer.doUEraw_ = cms.untracked.bool(False)
process.pfcandAnalyzer.genLabel = cms.InputTag("genParticles")

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
# photons
######################
process.load('HeavyIonsAnalysis.PhotonAnalysis.ggHiNtuplizer_cfi')
process.ggHiNtuplizer.gsfElectronLabel   = cms.InputTag("gedGsfElectrons")
process.ggHiNtuplizer.recoPhotonHiIsolationMap = cms.InputTag('photonIsolationHIProducerpp')
process.ggHiNtuplizer.VtxLabel           = cms.InputTag("offlinePrimaryVertices")
process.ggHiNtuplizer.particleFlowCollection = cms.InputTag("particleFlow")
process.ggHiNtuplizer.doVsIso            = cms.bool(False)
process.ggHiNtuplizer.doElectronVID      = cms.bool(True)
process.ggHiNtuplizerGED = process.ggHiNtuplizer.clone(recoPhotonSrc = cms.InputTag('gedPhotons'),
                                                       recoPhotonHiIsolationMap = cms.InputTag('photonIsolationHIProducerppGED'))

####################################################################################
#####################
# Electron ID
#####################

from PhysicsTools.SelectorUtils.tools.vid_id_tools import *
# turn on VID producer, indicate data format to be processed
# DataFormat.AOD or DataFormat.MiniAOD
dataFormat = DataFormat.AOD
switchOnVIDElectronIdProducer(process, dataFormat)

# define which IDs we want to produce. Check here https://twiki.cern.ch/twiki/bin/viewauth/CMS/CutBasedElectronIdentificationRun2#Recipe_for_regular_users_for_7_4
my_id_modules = ['RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Spring15_25ns_V1_cff']

#add them to the VID producer
for idmod in my_id_modules:
    setupAllVIDIdsInModule(process,idmod,setupVIDElectronSelection)
####################################################################################


#####################
# tupel and necessary PAT sequences
#####################

process.load("HeavyIonsAnalysis.VectorBosonAnalysis.tupelSequence_pp_mc_cff")

#####################################################################################


####B-TAGGING#####

process.load('RecoBTag.CSVscikit.csvscikitTagJetTags_cfi')
process.load('RecoBTag.CSVscikit.csvscikitTaggerProducer_cfi')

process.ak4PFCombinedSecondaryVertexV2BJetTags = process.pfCSVscikitJetTags.clone()
process.ak4PFCombinedSecondaryVertexV2BJetTags.tagInfos=cms.VInputTag(cms.InputTag("ak4PFImpactParameterTagInfos"), cms.InputTag("ak4PFSecondaryVertexTagInfos"))
process.CSVscikitTags.weightFile=cms.FileInPath('HeavyIonsAnalysis/JetAnalysis/data/TMVA_Btag_pp_BDTG.weights.xml')

################

#########################
# Main analysis list
#########################
process.ana_step = cms.Path(process.hltanalysis *
                            process.hltobject *
                            process.hiEvtAnalyzer *
                            process.HiGenParticleAna*
                            process.jetSequences +
                            process.egmGsfElectronIDSequence + #Should be added in the path for VID module
                            process.ggHiNtuplizer +
                            process.ggHiNtuplizerGED +
                            process.pfcandAnalyzer +
                            process.HiForest +
			    process.trackSequencesPP +
                            process.runAnalyzer +
                            process.tupelPatSequence
)

#####################################################################################

#########################
# Event Selection
#########################

process.load('HeavyIonsAnalysis.JetAnalysis.EventSelection_cff')
process.pHBHENoiseFilterResultProducer = cms.Path( process.HBHENoiseFilterResultProducer )
process.HBHENoiseFilterResult = cms.Path(process.fHBHENoiseFilterResult)
process.HBHENoiseFilterResultRun1 = cms.Path(process.fHBHENoiseFilterResultRun1)
process.HBHENoiseFilterResultRun2Loose = cms.Path(process.fHBHENoiseFilterResultRun2Loose)
process.HBHENoiseFilterResultRun2Tight = cms.Path(process.fHBHENoiseFilterResultRun2Tight)
process.HBHEIsoNoiseFilterResult = cms.Path(process.fHBHEIsoNoiseFilterResult)

process.PAprimaryVertexFilter = cms.EDFilter("VertexSelector",
    src = cms.InputTag("offlinePrimaryVertices"),
    cut = cms.string("!isFake && abs(z) <= 25 && position.Rho <= 2 && tracksSize >= 2"),
    filter = cms.bool(True), # otherwise it won't filter the events
)

process.NoScraping = cms.EDFilter("FilterOutScraping",
 applyfilter = cms.untracked.bool(True),
 debugOn = cms.untracked.bool(False),
 numtrack = cms.untracked.uint32(10),
 thresh = cms.untracked.double(0.25)
)

process.pPAprimaryVertexFilter = cms.Path(process.PAprimaryVertexFilter)
process.pBeamScrapingFilter=cms.Path(process.NoScraping)

process.load("HeavyIonsAnalysis.VertexAnalysis.PAPileUpVertexFilter_cff")

process.pVertexFilterCutG = cms.Path(process.pileupVertexFilterCutG)
process.pVertexFilterCutGloose = cms.Path(process.pileupVertexFilterCutGloose)
process.pVertexFilterCutGtight = cms.Path(process.pileupVertexFilterCutGtight)
process.pVertexFilterCutGplus = cms.Path(process.pileupVertexFilterCutGplus)
process.pVertexFilterCutE = cms.Path(process.pileupVertexFilterCutE)
process.pVertexFilterCutEandG = cms.Path(process.pileupVertexFilterCutEandG)

process.pAna = cms.EndPath(process.skimanalysis)

# Customization

process.hltobject.triggerNames = cms.vstring(
#"digitisation_step",
#"L1simulation_step",
#"digi2raw_step",
#"HLTriggerFirstPath",
"HLT_Physics_v2",
"DST_Physics_v1",
"HLT_Random_v1",
"HLT_ZeroBias_v2",
"HLT_PixelTracks_Multiplicity60ForPPRef_v1",
"HLT_PixelTracks_Multiplicity85ForPPRef_v1",
"HLT_PixelTracks_Multiplicity110ForPPRef_v1",
"HLT_PixelTracks_Multiplicity135ForPPRef_v1",
"HLT_PixelTracks_Multiplicity160ForPPRef_v1",
"HLT_AK4CaloJet40_Eta5p1ForPPRef_v1",
"HLT_AK4CaloJet60_Eta5p1ForPPRef_v1",
"HLT_AK4CaloJet80_Eta5p1ForPPRef_v1",
"HLT_AK4CaloJet100_Eta5p1ForPPRef_v1",
"HLT_AK4CaloJet110_Eta5p1ForPPRef_v1",
"HLT_AK4CaloJet120_Eta5p1ForPPRef_v1",
"HLT_AK4CaloJet150ForPPRef_v1",
"HLT_AK4PFJet40_Eta5p1ForPPRef_v1",
"HLT_AK4PFJet60_Eta5p1ForPPRef_v1",
"HLT_AK4PFJet80_Eta5p1ForPPRef_v1",
"HLT_AK4PFJet100_Eta5p1ForPPRef_v1",
"HLT_AK4PFJet110_Eta5p1ForPPRef_v1",
"HLT_AK4PFJet120_Eta5p1ForPPRef_v1",
"HLT_AK4CaloJet80_Jet35_Eta1p1ForPPRef_v1",
"HLT_AK4CaloJet80_Jet35_Eta0p7ForPPRef_v1",
"HLT_AK4CaloJet100_Jet35_Eta1p1ForPPRef_v1",
"HLT_AK4CaloJet100_Jet35_Eta0p7ForPPRef_v1",
"HLT_AK4CaloJet80_45_45_Eta2p1ForPPRef_v1",
"HLT_HISinglePhoton10_Eta1p5ForPPRef_v1",
"HLT_HISinglePhoton15_Eta1p5ForPPRef_v1",
"HLT_HISinglePhoton20_Eta1p5ForPPRef_v1",
"HLT_HISinglePhoton30_Eta1p5ForPPRef_v1",
"HLT_HISinglePhoton40_Eta1p5ForPPRef_v1",
"HLT_HISinglePhoton50_Eta1p5ForPPRef_v1",
"HLT_HISinglePhoton60_Eta1p5ForPPRef_v1",
"HLT_HISinglePhoton10_Eta3p1ForPPRef_v1",
"HLT_HISinglePhoton15_Eta3p1ForPPRef_v1",
"HLT_HISinglePhoton20_Eta3p1ForPPRef_v1",
"HLT_HISinglePhoton30_Eta3p1ForPPRef_v1",
"HLT_HISinglePhoton40_Eta3p1ForPPRef_v1",
"HLT_HISinglePhoton50_Eta3p1ForPPRef_v1",
"HLT_HISinglePhoton60_Eta3p1ForPPRef_v1",
"HLT_HIDoublePhoton15_Eta1p5_Mass50_1000ForPPRef_v1",
"HLT_HIDoublePhoton15_Eta1p5_Mass50_1000_R9HECutForPPRef_v1",
"HLT_HIDoublePhoton15_Eta2p1_Mass50_1000_R9CutForPPRef_v1",
"HLT_HIDoublePhoton15_Eta2p5_Mass50_1000_R9SigmaHECutForPPRef_v1",
"HLT_HIL2Mu3Eta2p5_AK4CaloJet40Eta2p1ForPPRef_v1",
"HLT_HIL2Mu3Eta2p5_AK4CaloJet60Eta2p1ForPPRef_v1",
"HLT_HIL2Mu3Eta2p5_AK4CaloJet80Eta2p1ForPPRef_v1",
"HLT_HIL2Mu3Eta2p5_AK4CaloJet100Eta2p1ForPPRef_v1",
"HLT_HIL2Mu3Eta2p5_HIPhoton10Eta1p5ForPPRef_v1",
"HLT_HIL2Mu3Eta2p5_HIPhoton15Eta1p5ForPPRef_v1",
"HLT_HIL2Mu3Eta2p5_HIPhoton20Eta1p5ForPPRef_v1",
"HLT_HIL2Mu3Eta2p5_HIPhoton30Eta1p5ForPPRef_v1",
"HLT_HIL2Mu3Eta2p5_HIPhoton40Eta1p5ForPPRef_v1",
"HLT_HIL1DoubleMu0ForPPRef_v1",
"HLT_HIL1DoubleMu10ForPPRef_v1",
"HLT_HIL2DoubleMu0_NHitQForPPRef_v1",
"HLT_HIL3DoubleMu0_OS_m2p5to4p5ForPPRef_v1",
"HLT_HIL3DoubleMu0_OS_m7to14ForPPRef_v1",
"HLT_HIL2Mu3_NHitQ10ForPPRef_v1",
"HLT_HIL3Mu3_NHitQ15ForPPRef_v1",
"HLT_HIL2Mu5_NHitQ10ForPPRef_v1",
"HLT_HIL3Mu5_NHitQ15ForPPRef_v1",
"HLT_HIL2Mu7_NHitQ10ForPPRef_v1",
"HLT_HIL3Mu7_NHitQ15ForPPRef_v1",
"HLT_HIL2Mu15ForPPRef_v1",
"HLT_HIL3Mu15ForPPRef_v1",
"HLT_HIL2Mu20ForPPRef_v1",
"HLT_HIL3Mu20ForPPRef_v1",
"HLT_FullTrack18ForPPRef_v1",
"HLT_FullTrack24ForPPRef_v1",
"HLT_FullTrack34ForPPRef_v1",
"HLT_FullTrack45ForPPRef_v1",
"HLT_FullTrack53ForPPRef_v1",
"HLT_HIUPCL1DoubleMuOpenNotHF2ForPPRef_v1",
"HLT_HIUPCDoubleMuNotHF2Pixel_SingleTrackForPPRef_v1",
"HLT_HIUPCL1MuOpen_NotMinimumBiasHF2_ANDForPPRef_v1",
"HLT_HIUPCMuOpen_NotMinimumBiasHF2_ANDPixel_SingleTrackForPPRef_v1",
"HLT_HIUPCL1NotMinimumBiasHF2_ANDForPPRef_v1",
"HLT_HIUPCNotMinimumBiasHF2_ANDPixel_SingleTrackForPPRef_v1",
"HLT_HIUPCL1ZdcOR_BptxANDForPPRef_v1",
"HLT_HIUPCZdcOR_BptxANDPixel_SingleTrackForPPRef_v1",
"HLT_HIUPCL1ZdcXOR_BptxANDForPPRef_v1",
"HLT_HIUPCZdcXOR_BptxANDPixel_SingleTrackForPPRef_v1",
"HLT_HIUPCL1NotZdcOR_BptxANDForPPRef_v1",
"HLT_HIUPCNotZdcOR_BptxANDPixel_SingleTrackForPPRef_v1",
"HLT_HIL1CastorMediumJetForPPRef_v1",
"HLT_HICastorMediumJetPixel_SingleTrackForPPRef_v1",
"HLT_DmesonPPTrackingGlobal_Dpt8ForPPRef_v1",
"HLT_DmesonPPTrackingGlobal_Dpt15ForPPRef_v1",
"HLT_DmesonPPTrackingGlobal_Dpt20ForPPRef_v1",
"HLT_DmesonPPTrackingGlobal_Dpt30ForPPRef_v1",
"HLT_DmesonPPTrackingGlobal_Dpt40ForPPRef_v1",
"HLT_DmesonPPTrackingGlobal_Dpt50ForPPRef_v1",
"HLT_DmesonPPTrackingGlobal_Dpt60ForPPRef_v1",
"HLT_AK4PFBJetBCSV60_Eta2p1ForPPRef_v1",
"HLT_AK4PFBJetBCSV80_Eta2p1ForPPRef_v1",
"HLT_AK4PFDJet60_Eta2p1ForPPRef_v1",
"HLT_AK4PFDJet80_Eta2p1ForPPRef_v1",
"HLT_AK4PFBJetBSSV60_Eta2p1ForPPRef_v1",
"HLT_AK4PFBJetBSSV80_Eta2p1ForPPRef_v1",
#"HLT_EcalCalibration_v2",
#"HLT_HcalCalibration_v1",
#"AlCa_EcalPhiSym_v3",
#"HLT_L1Tech6_BPTX_MinusOnly_v1",
#"HLT_L1Tech5_BPTX_PlusOnly_v2",
#"HLT_L1Tech7_NoBPTX_v1",
#"HLT_L1TOTEM1_MinBias_v1",
#"HLT_L1TOTEM2_ZeroBias_v1",
"HLT_L1MinimumBiasHF1OR_v1",
"HLT_L1MinimumBiasHF2OR_v1",
"HLT_L1MinimumBiasHF2ORNoBptxGating_v1",
"HLT_L1MinimumBiasHF1AND_v1",
"HLT_L1MinimumBiasHF2AND_v1",
#"AlCa_LumiPixels_Random_v1",
#"AlCa_LumiPixels_ZeroBias_v2",
#"HLTriggerFinalPath"
)
## NOTES
# how to check the HLT paths in the input file
#$> git diff --unified=0  HeavyIonsAnalysis/EventAnalysis/src/TriggerObjectAnalyzer.cc
# diff --git a/HeavyIonsAnalysis/EventAnalysis/src/TriggerObjectAnalyzer.cc b/HeavyIonsAnalysis/EventAnalysis/src/TriggerObjectAnalyzer.cc
# index 1ffcafc..886b38b 100644
# --- a/HeavyIonsAnalysis/EventAnalysis/src/TriggerObjectAnalyzer.cc
# +++ b/HeavyIonsAnalysis/EventAnalysis/src/TriggerObjectAnalyzer.cc
# @@ -217,0 +218,3 @@ TriggerObjectAnalyzer::beginRun(edm::Run const& iRun, edm::EventSetup const& iSe
# +
# +         std::cout << "activeHLTPathInThisEvent = " << (*iHLT).c_str() << std::endl;
# +
