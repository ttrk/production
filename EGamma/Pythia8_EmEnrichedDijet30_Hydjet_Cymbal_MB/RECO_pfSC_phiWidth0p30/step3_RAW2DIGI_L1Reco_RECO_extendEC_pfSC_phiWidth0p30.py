# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --mc --eventcontent AODSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1_HI --datatier AODSIM --conditions 75X_mcRun2_HeavyIon_v14 --step RAW2DIGI,L1Reco,RECO --scenario HeavyIons -n 20 --no_exec --filein file:step2_DIGI_L1_DIGI2RAW_HLT_PU.root
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(20)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:step2_DIGI_L1_DIGI2RAW_HLT_PU.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:20'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('AODSIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fileName = cms.untracked.string('step3_RAW2DIGI_L1Reco_RECO_extendEC_pfSC_phiWidth0p30.root'),
    outputCommands = process.AODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '75X_mcRun2_HeavyIon_v14', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstructionHeavyIons)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.AODSIMoutput_step)

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1_HI 

#call to customisation function customisePostLS1_HI imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1_HI(process)

# End of customisation functions

# use narrower phi window for GED photon SC
process.particleFlowSuperClusterECAL.useDynamicDPhiWindow = cms.bool(False)
process.particleFlowSuperClusterECAL.phiwidth_SuperClusterBarrel = cms.double(0.30)
process.particleFlowSuperClusterECAL.phiwidth_SuperClusterEndcap = cms.double(0.30)

# extend AOD content
process.load('Configuration.EventContent.EventContent_cff')
myNewEventContent = cms.untracked.vstring(['keep recoCaloClusters_islandBasicClusters*_*_*',
                                           'keep recoCaloClusters_multi5x5BasicClusters*_*_*',
                                           # add "uncorrected" SC, note that AOD contains final "corrected" SC
                                           'keep recoSuperClusters_islandSuperClusters*_*_*',
                                           'keep recoCaloClusters_hybridSuperClusters_*_*',
                                           'keep recoCaloClusters_*HybridSuperClusters_*_*',
                                           'keep recoCaloClusters_multi5x5SuperClusters*_*_*',
                                           'keep recoSuperClusters_*Multi5x5SuperClusters*_*_*',
                                           # PF
                                           'keep recoCaloClusteredmPtredmValueMap_particleFlowSuperClusterECAL_*_*',
                                           'keep recoPFCandidates_particleFlowEGamma_*_*',
                                           # RecHits
                                           'keep EcalRecHitsSorted_ecalRecHit_*_*',
                                           'keep EcalRecHitsSorted_ecalPreshowerRecHit_*_*'
                                           ])
process.AODEventContent.outputCommands.extend(myNewEventContent)

process.AODSIMEventContent.outputCommands.extend(myNewEventContent)

