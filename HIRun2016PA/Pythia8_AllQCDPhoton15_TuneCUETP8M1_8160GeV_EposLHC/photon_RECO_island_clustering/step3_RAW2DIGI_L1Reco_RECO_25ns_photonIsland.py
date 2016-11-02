# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --mc --datatier GEN-SIM-RECO --conditions 80X_mcRun2_asymptotic_v15 -s RAW2DIGI,L1Reco,RECO --eventcontent RECOSIM --era Run2_2016 --customise RecoHI/Configuration/customise_PPwithHI.customisePPrecoforPPb --customise_commands process.bunchSpacingProducer.bunchSpacingOverride=cms.uint32(25)\nprocess.bunchSpacingProducer.overrideBunchSpacing=cms.bool(True) -n 10 --no_exec --filein=file:step2_DIGI_L1_DIGI2RAW_HLT_PU.root --fileout=file:step3_RAW2DIGI_L1Reco_RECO_25ns.root --python_filename=step3_RAW2DIGI_L1Reco_RECO_25ns.py
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('RECO',eras.Run2_2016)

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
    fileNames = cms.untracked.vstring('file:/afs/cern.ch/work/k/katatar/public/HIRun2016PA/CMSSW_8_0_15/src/Pythia8_AllQCDPhoton15_TuneCUETP8M1_8160GeV/step2_DIGI_L1_DIGI2RAW_HLT_PU.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('file:step3_RAW2DIGI_L1Reco_RECO_25ns_photonIsland.root'),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_asymptotic_v15', '')


##KT##
process.RECOSIMEventContent.outputCommands.extend(['keep recoCaloClusters_islandBasicClusters_*_*',
                                                   'keep *_islandSuperClusters_*_*',
                                                   'keep *_correctedIslandBarrelSuperClusters_*_*',
                                                   'keep *_correctedIslandEndcapSuperClusters_*_*'
])
##from RecoHI.HiEgammaAlgos.HiIslandClusteringSequence_cff import *
process.load('RecoHI.HiEgammaAlgos.HiIslandClusteringSequence_cff')

## # Island BasicCluster producer
process.load('RecoEcal.EgammaClusterProducers.islandBasicClusters_cfi')
# Island SuperCluster producer
process.load('RecoHI.HiEgammaAlgos.HiIslandSuperClusters_cfi')
# Energy scale correction for Island SuperClusters
process.load('RecoHI.HiEgammaAlgos.HiCorrectedIslandBarrelSuperClusters_cfi')
process.load('RecoHI.HiEgammaAlgos.HiCorrectedIslandEndcapSuperClusters_cfi')

#process.islandClusteringSequencePP = cms.Sequence(process.islandClusteringSequence)
process.hybridClusteringSequence *= process.islandClusteringSequence

# use island for the moment
process.photonCore.scHybridBarrelProducer = cms.InputTag("correctedIslandBarrelSuperClusters")
process.photonCore.scIslandEndcapProducer = cms.InputTag("correctedIslandEndcapSuperClusters")
process.photonCore.minSCEt = cms.double(8.0)
process.photons.minSCEtBarrel = cms.double(5.0)
process.photons.minSCEtEndcap = cms.double(15.0)
process.photons.minR9Barrel = cms.double(10.)  #0.94
process.photons.minR9Endcap = cms.double(10.)   #0.95
process.photons.maxHoverEEndcap = cms.double(0.5)  #0.5
process.photons.maxHoverEBarrel = cms.double(0.99)  #0.5
#process.photons.primaryVertexProducer = cms.InputTag('hiSelectedVertex') # replace the primary vertex
#process.photons.isolationSumsCalculatorSet.trackProducer = process.isolationInputParameters.track # cms.InputTag("highPurityTracks")

##KT##

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.RECOSIMoutput_step)

# customisation of the process.

# Automatic addition of the customisation function from RecoHI.Configuration.customise_PPwithHI
from RecoHI.Configuration.customise_PPwithHI import customisePPrecoforPPb 

#call to customisation function customisePPrecoforPPb imported from RecoHI.Configuration.customise_PPwithHI
process = customisePPrecoforPPb(process)

# End of customisation functions

# Customisation from command line
process.bunchSpacingProducer.bunchSpacingOverride=cms.uint32(25)
process.bunchSpacingProducer.overrideBunchSpacing=cms.bool(True)

# Customisation from command line
process.bunchSpacingProducer.bunchSpacingOverride=cms.uint32(25)
process.bunchSpacingProducer.overrideBunchSpacing=cms.bool(True)
