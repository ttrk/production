# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --mc --eventcontent RAWSIM --pileup HiMixNoPU --datatier GEN-SIM-DIGI-RAW --conditions 103X_upgrade2018_realistic_HI_v7 --step DIGI:pdigi_hi_nogen,L1,DIGI2RAW,HLT:@fake2 --geometry DB:Extended --era Run2_2018_pp_on_AA --filein root://xrootd.cmsaf.mit.edu//store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10_ext1-v1/40001/FE23B1BC-8CA8-E811-861C-AC1F6B23C94A.root,root://xrootd.cmsaf.mit.edu//store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10_ext1-v1/40001/F857A1AA-94A8-E811-8746-A0369FD0B366.root --fileout file:step2_DIGI_L1_DIGI2RAW_HLT_PU.root -n 50 --no_exec --python_filename step2_DIGI_L1_DIGI2RAW_HLT_PU.py
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT',eras.Run2_2018_pp_on_AA)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.HiMixNoPU_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_Fake2_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(50)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'root://xrootd.cmsaf.mit.edu//store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10_ext1-v1/40001/FE23B1BC-8CA8-E811-861C-AC1F6B23C94A.root', 
        'root://xrootd.cmsaf.mit.edu//store/himc/HINPbPbSpring18GS/Hydjet_Quenched_Drum5Ev8_PbPbMinBias_5020GeV_2018/GEN-SIM/100X_upgrade2018_realistic_v10_ext1-v1/40001/F857A1AA-94A8-E811-8746-A0369FD0B366.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2 nevts:50'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(1),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('file:step2_DIGI_L1_DIGI2RAW_HLT_PU.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '103X_upgrade2018_realistic_HI_v7', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi_hi_nogen)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.RAWSIMoutput_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
