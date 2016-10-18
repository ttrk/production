# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --conditions 80X_mcRun2_asymptotic_v15 --pileup_input das:/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/pPb816Spring16GS-80X_mcRun2_asymptotic_v17-v1/GEN-SIM --eventcontent FEVTDEBUG -s DIGI,L1,DIGI2RAW,HLT:@fake --datatier GEN-SIM-DIGI-RAW-HLTDEBUG --pileup HiMix --era Run2_2016 -n 10 --no_exec --filein=file:Pythia8_AllQCDPhoton30_TuneCUETP8M1_8160GeV_cff_py_GEN_SIM_PU.root
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT',eras.Run2_2016)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.HiMix_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_Fake_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring('file:Pythia8_AllQCDPhoton30_TuneCUETP8M1_8160GeV_cff_py_GEN_SIM_PU.root'),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop *_genParticles_*_*', 
        'drop *_genParticlesForJets_*_*', 
        'drop *_kt4GenJets_*_*', 
        'drop *_kt6GenJets_*_*', 
        'drop *_iterativeCone5GenJets_*_*', 
        'drop *_ak4GenJets_*_*', 
        'drop *_ak7GenJets_*_*', 
        'drop *_ak8GenJets_*_*', 
        'drop *_ak4GenJetsNoNu_*_*', 
        'drop *_ak8GenJetsNoNu_*_*', 
        'drop *_genCandidatesForMET_*_*', 
        'drop *_genParticlesForMETAllVisible_*_*', 
        'drop *_genMetCalo_*_*', 
        'drop *_genMetCaloAndNonPrompt_*_*', 
        'drop *_genMetTrue_*_*', 
        'drop *_genMetIC5GenJs_*_*'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW-HLTDEBUG'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('step2_DIGI_L1_DIGI2RAW_HLT_PU.root'),
    outputCommands = process.FEVTDEBUGEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.fileNames = cms.untracked.vstring(['/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0015599B-5671-E611-A11A-008CFAFC043A.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0032A97D-6671-E611-ADED-848F69FD2826.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0039E374-6071-E611-AD5B-047D7B2E84EC.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0050A418-7171-E611-887D-14187741013C.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/00618F48-5971-E611-A74A-0CC47A4DEE00.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/0071D8A7-5F71-E611-884D-0025905C3DD0.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/00C10B26-6D71-E611-B92D-848F69FD28E3.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/00F467B1-6B71-E611-BBC7-901B0E5427B0.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/00F72BC0-6871-E611-8A98-B499BAAC054A.root', '/store/himc/pPb816Spring16GS/ReggeGribovPartonMC_EposLHC_pPb_4080_4080/GEN-SIM/80X_mcRun2_asymptotic_v17-v1/90000/023D4492-6871-E611-8987-002590D6004A.root'])
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_asymptotic_v15', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGoutput_step = cms.EndPath(process.FEVTDEBUGoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.FEVTDEBUGoutput_step])

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforFullSim 

#call to customisation function customizeHLTforFullSim imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforFullSim(process)

# End of customisation functions

