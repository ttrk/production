# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3_pp --mc --conditions 92X_upgrade2017_realistic_v11 -s RAW2DIGI,L1Reco,RECO --datatier GEN-SIM-RECO --geometry DB:Extended --era Run2_2017 --eventcontent AODSIM -n 400 --filein=file:step2_pp_DIGI_L1_DIGI2RAW_HLT_1.root --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('RECO',eras.Run2_2017)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('root://cms-xrd-global.cern.ch//store/user/gsfs/Pythia8_MinBias_pp_CUETP8M1_5020GeV/RAW_20171002/171003_010838/0000/step2_pp_DIGI_L1_DIGI2RAW_HLT_1.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3_pp nevts:400'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fileName = cms.untracked.string('step3_pp_RAW2DIGI_L1Reco_RECO_phoIso.root'),
    outputCommands = process.AODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '92X_upgrade2017_realistic_v11', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.AODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

# Customize process to run HI-style photon isolation in the pp RECO sequences
# https://github.com/cms-sw/cmssw/blob/CMSSW_7_5_X/RecoHI/Configuration/python/customise_PPwithHI.py#L4-L77
process.load('RecoHI.HiEgammaAlgos.photonIsolationHIProducer_cfi')
process.load('RecoEcal.EgammaClusterProducers.islandBasicClusters_cfi')

process.photonIsolationHISequencePP = cms.Sequence(process.islandBasicClusters 
                                                   * process.photonIsolationHIProducerpp 
                                                   * process.photonIsolationHIProducerppGED)
    
process.reconstruction *= process.photonIsolationHISequencePP
    
# extend RecoEgammaAOD content
process.AODEventContent.outputCommands.extend(['keep recoHIPhotonIsolationedmValueMap_photonIsolationHIProducerppGED_*_*',
                                               'keep recoHIPhotonIsolationedmValueMap_photonIsolationHIProducerpp_*_*'
                                                  ])

process.AODSIMEventContent.outputCommands.extend(['keep recoHIPhotonIsolationedmValueMap_photonIsolationHIProducerppGED_*_*',
                                                  'keep recoHIPhotonIsolationedmValueMap_photonIsolationHIProducerpp_*_*'
])


