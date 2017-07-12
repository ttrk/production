# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --pileup_input dbs:/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV/HiFall15-75X_mcRun2_HeavyIon_v14_75X_mcRun2_HeavyIon_v14-v1/GEN-SIM --mc --eventcontent RAWSIM --pileup HiMix --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1_HI --datatier GEN-SIM-RAW --conditions 75X_mcRun2_HeavyIon_v14 --step DIGI:pdigi_hi,L1,DIGI2RAW,HLT:HIon --scenario HeavyIons -n 20 --no_exec --filein file:SingleGammaFlatPt10To100_pythia8_Hydjet_GEN_SIM_PU.root
import FWCore.ParameterSet.Config as cms

process = cms.Process('HLT')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')
process.load('SimGeneral.MixingModule.HiMix_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_HIon_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(20)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:SingleGammaFlatPt10To100_pythia8_Hydjet_GEN_SIM_PU.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2 nevts:20'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RAW'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('step2_DIGI_L1_DIGI2RAW_HLT_PU.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.fileNames = cms.untracked.vstring(['/store/himc/HiFall15/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v14_75X_mcRun2_HeavyIon_v14-v1/100000/005F5115-9BD4-E611-AB73-0025905C431C.root', '/store/himc/HiFall15/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v14_75X_mcRun2_HeavyIon_v14-v1/100000/0062542B-A7D4-E611-BDA2-0025905C2CD0.root', '/store/himc/HiFall15/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v14_75X_mcRun2_HeavyIon_v14-v1/100000/006B6A2A-D4D4-E611-91D0-00269E95B1B8.root', '/store/himc/HiFall15/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v14_75X_mcRun2_HeavyIon_v14-v1/100000/00839502-96D4-E611-B666-02163E013EEB.root', '/store/himc/HiFall15/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v14_75X_mcRun2_HeavyIon_v14-v1/100000/009B5A74-CED4-E611-8F43-20CF3019DEEF.root', '/store/himc/HiFall15/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v14_75X_mcRun2_HeavyIon_v14-v1/100000/00A04E07-D4D4-E611-B9D5-0090FAA58544.root', '/store/himc/HiFall15/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v14_75X_mcRun2_HeavyIon_v14-v1/100000/00B28404-D0D4-E611-907C-001E68862A40.root', '/store/himc/HiFall15/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v14_75X_mcRun2_HeavyIon_v14-v1/100000/00DA17A4-C0D4-E611-885F-1866DAEA7A40.root', '/store/himc/HiFall15/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v14_75X_mcRun2_HeavyIon_v14-v1/100000/00EAE9E5-BFD4-E611-B094-FA163E71C1CA.root', '/store/himc/HiFall15/Hydjet_Quenched_Cymbal5Ev8_PbPbMinBias_5020GeV/GEN-SIM/75X_mcRun2_HeavyIon_v14_75X_mcRun2_HeavyIon_v14-v1/100000/00FF50B2-DBD4-E611-B55F-0025904C63F8.root'])
process.mix.digitizers = cms.PSet(process.theDigitizersValid)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '75X_mcRun2_HeavyIon_v14', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi_hi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.RAWSIMoutput_step])

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1_HI 

#call to customisation function customisePostLS1_HI imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1_HI(process)

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforFullSim 

#call to customisation function customizeHLTforFullSim imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforFullSim(process)

# End of customisation functions

